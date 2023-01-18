import aiohttp
import asyncio
import logging


def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''
    if ip == '255.255.255.255':
        return '0.0.0.0'
    octets = [int(octet) for octet in ip.split('.')]
    working_octet = 3
    while True:
        octets[working_octet] += 1
        if octets[working_octet] > 255:
            octets[working_octet] = 0
            working_octet -= 1
        else:
            break
    return '.'.join([str(octet) for octet in octets])


def enumerate_ips(start_ip, n):
    '''
    Yield the next `n` ips beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']
    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    The following tests ensure that the correct number of ips get returned as a generator, and not a list.
    Ensuring that the return type is a generator is a proxy for testing for space efficiency of the function.

    >>> type(enumerate_ips('8.8.8.8', 10))
    <class 'generator'>
    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    ip = start_ip
    for i in range(n):
        yield ip
        ip = increment_ip(ip)


def netmask_to_ips(netmask):
    '''
    A netmask is a convenient shorthand for describing a range of consecutive ip addresses.
    For details on the format, see: <https://www.hacksplaining.com/glossary/netmasks>

    Google is assigned the following netblock (among many others as well):

    >>> len(list(netmask_to_ips('104.154.0.0/15')))
    131072

    The Claremont Colleges are assigned the following netblock:

    >>> len(list(netmask_to_ips('134.173.0.0/16')))
    65536

    North Korea is assigned the following netblock:

    >>> len(list(netmask_to_ips('175.45.176.0/22')))
    1024

    The following tests ensure that the ips returned match the correct range:

    >>> list(netmask_to_ips('134.173.0.0/16'))[0]
    '134.173.0.0'
    >>> list(netmask_to_ips('134.173.0.0/16'))[-1]
    '134.173.255.255'

    >>> list(netmask_to_ips('134.173.55.0/16'))[0]
    '134.173.0.0'
    >>> list(netmask_to_ips('134.173.55.0/16'))[-1]
    '134.173.255.255'

    >>> list(netmask_to_ips('134.173.0.55/16'))[0]
    '134.173.0.0'
    >>> list(netmask_to_ips('134.173.0.55/16'))[-1]
    '134.173.255.255'

    >>> list(netmask_to_ips('134.173.255.255/16'))[0]
    '134.173.0.0'
    >>> list(netmask_to_ips('134.173.255.255/16'))[-1]
    '134.173.255.255'

    >>> list(netmask_to_ips('208.97.177.235/24'))[0]
    '208.97.177.0'
    >>> list(netmask_to_ips('208.97.177.235/24'))[-1]
    '208.97.177.255'
    '''

    ip_str, mask_str = netmask.split('/')
    octets = ip_str.split('.')
    ip_32bit =  int(octets[0]) << 24
    ip_32bit += int(octets[1]) << 16
    ip_32bit += int(octets[2]) << 8
    ip_32bit += int(octets[3])

    mask = int(mask_str)
    mask_32bit = 0
    for i in range(32,32-mask-1,-1):
        mask_32bit += 1 << i

    base_ip = ip_32bit & mask_32bit
    octet0 = (base_ip >> 24) % 256
    octet1 = (base_ip >> 16) % 256
    octet2 = (base_ip >>  8) % 256
    octet3 = (base_ip      ) % 256

    start_ip = str(octet0) + '.' + str(octet1) + '.' + str(octet2) + '.' + str(octet3)
    num_ips = 2**(32-mask)

    return enumerate_ips(start_ip, num_ips)


async def is_server_at_host(session, host, schema='http'):
    '''
    Return True if a web server at `host` responds to the specified `schema`.
    The `session` variable is assumed to be a properly initialized `aiohttp.ClientSession` object.
    '''
    url = schema + '://' + host
    try:
        async with session.get(url, allow_redirects=False) as resp:
            logging.info('server at '+url)
            return True
    except ( aiohttp.client_exceptions.ClientConnectorError
           , asyncio.TimeoutError
           , aiohttp.client_exceptions.ServerDisconnectedError
           ) as e:
        logging.debug('no server at '+url)
        return False


async def _wardial_async(hosts, max_connections=500, timeout=10, schema='http'):
    '''
    '''
    connector = aiohttp.TCPConnector(
        limit=max_connections,
        limit_per_host=1,
        verify_ssl=False,
        )
    headers = {
        'host': 'placeholder', # some servers require a host value be set
        'user-agent': 'CMC WarDialer',
        }
    timeout = aiohttp.ClientTimeout(
        total=None,
        sock_connect=timeout,
        sock_read=timeout
        )
    async with aiohttp.ClientSession(
            headers=headers,
            timeout=timeout,
            connector=connector,
            ) as session:
        ops = [is_server_at_host(session, host) for host in hosts]
        return await asyncio.gather(*ops)


def wardial(hosts, **kwargs):
    '''

    >>> hosts = ['facebook.com', 'google.com', 'github.com', 'amazon.com', 'microsoft.com', 'netflix.com']
    >>> len(wardial(hosts)) >= len(hosts)-1

    >>> wardial(['208.97.176.235', '23.185.0.2', '142.250.72.174'])
    ['208.97.176.235', '23.185.0.2', '142.250.72.174']
    '''
    hosts = list(hosts)
    loop = asyncio.new_event_loop()
    statuses = loop.run_until_complete(_wardial_async(hosts, **kwargs))
    alive_hosts = [ host for (host,status) in zip(hosts,statuses) if status ]
    loop.close()
    return alive_hosts


if __name__=='__main__':

    # process the cmd line args
    import argparse
    parser = argparse.ArgumentParser(description='Scan a section of the internet for webservers')
    parser.add_argument('netmask')
    parser.add_argument('--timeout', type=int, default=10)
    parser.add_argument('--max_connections', type=int, default=500)
    parser.add_argument('--schema', default='http')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()

    # set the logging level
    if args.verbose:
        logging.basicConfig(level="DEBUG")
    elif args.quiet:
        logging.basicConfig(level="WARNING")
    else:
        logging.basicConfig(level="INFO")

    # run the wardial
    ips = netmask_to_ips(args.netmask)
    alive_ips = wardial(ips, timeout=args.timeout, max_connections=args.max_connections, schema=args.schema)
    print('total ips found =', len(alive_ips))
