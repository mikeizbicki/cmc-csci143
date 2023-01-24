# Lab: War Dialing

**Description:**

You will "war dial" ALL web servers located in the DPRK (i.e. North Korea),
and count how many web servers they have connected to the internet.

**Ethics Note:**

War dialing sounds scary,
and so muggles often think that it is a bad thing to do.
(They think war dialing is a type of cracking or black hat hacking.)
But in the computer science world,
war dialing is considered perfectly normal and white hat.
It consists of just connecting to all computers in a certain area of the internet and asking for a webpage.
Search engines like Google are constantly war dialing the entire internet to find new websites to put in their search results.
To make the war dialing sound more "friendly" to muggles,
the generation of search engines before Google (Yahoo!, AltaVista, etc.) renamed war dialing to "spidering",
and that's still the terminology [Google uses today](https://www.google.com/search/howsearchworks/how-search-works/organizing-information/) when they describe their war dialing process.
But in this assignment, we'll continue calling the process war dialing.

Many security companies will give reports to their customers about how many times they've been scanned in this way.
This is one of the easiest way to scare customers into paying for overpriced security projects.
The reality of the modern internet is that all computers connected to the internet are regularly scanned

**Learning Objectives:**

1. Review using the `requests` library
1. Review working with exceptions
1. Learn how to circumvent anti-scraping measures
1. Learn how to monitor the internet connectivity of a country/organization

## Background

**What is War Dialing?**

War dialing is the process of scanning a segment of the internet to list all the computers in that segment.
The [name comes from the WarGames movie](https://en.wikipedia.org/wiki/Wardialing#Etymology),
where David Lightman (the main character) uses war dialing to discover a US military nuclear control computer in this scene:

<img src=wargames.jpg width=600px />

There's a great [stack overflow discussion of how realistic this movie is](https://scifi.stackexchange.com/questions/66882/how-does-david-lightman-in-wargames-manage-to-hack-a-computer-by-dialing-a-numbe/66899).
Basically, all the technical details of war dialing in the movie are correct,
but the US has never connected nuclear command and control computers to the internet precisely to prevent them from getting hacked.

Actually, you can find lots of information online about US networks for classified information like the:
- [SIPRNet](https://blog.securestrux.com/siprnet-a-brief-introduction-to-the-secret-router-network) (used for organizing military operations classified as SECRET),
- [JWICS](https://en.wikipedia.org/wiki/Joint_Worldwide_Intelligence_Communications_System) (used for organizing military operations classified as TOP SECRET),
- and [NSANet](https://en.wikipedia.org/wiki/National_Security_Agency#NSANet) (used for sharing intelligence information classified as TOP SECRET/SCI).
Nuclear secrets are allowed to be shared on some of these networks,
but [nuclear command and control (NC2)](https://en.wikipedia.org/wiki/Nuclear_command_and_control) infrastructure is required to be [air gapped](https://en.wikipedia.org/wiki/Air_gap_(networking)) from all networks---even the most exclusive and top secret ones like NSANet---in order to prevent a scenario like in the WarGames movie.

**History of the Internet:**

The WarGames movie was released in 1983,
and the internet didn't exist yet.
At the time, computers connected to each other by calling each other over ordinary telephone lines using ordinary telephone numbers.
(This is different than dialup internet.)
David Lightman therefore scans all the telephone numbers of different geographic regions in order to find all the "online" computers in those geographic regions.

Today, computers on the internet use the IPv4 protocol to connect to each other.
Incidentally, [IPv4 was first deployed](https://en.wikipedia.org/wiki/IPv4#cite_ref-:0_1-0) to an early version of the internet called the [ARPANET](https://en.wikipedia.org/wiki/ARPANET) in 1983, the year that WarGames was released.
"Dial up" internet, which connects ordinary telephone lines to the IPv4 internet was [invented in 1992](https://en.wikipedia.org/wiki/Dial-up_Internet_access).

**IP Addresses vs Domain Names:**

Recall that an IP address is a series of 4 8-bit numbers separated by periods.
IP addresses, just like domain names, can host websites.
To see this, visit the webpage <https://142.250.68.14>.

Notice that you get redirected to <https://google.com>.
That's because this is Google's IP address.
You can connect to any server by specifying either the IP address directly or by using the more human-readable domain name format.

Whenever you use a domain name,
the browser under the hood uses the [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System) to convert that domain name into an IP address for making the actual connection.
<!--
There are many human-friendly online tools for viewing DNS information like <https://whois.domaintools.com/>.
-->
The IP address is needed to contact a computer because it is related to the physical location of the server.
Your ISP needs to know the physical location of every website you connect to in order to route your requests to the correct location.
The website <https://www.geolocation.com> provides a nice human-readable view of an IP address's location.
If you visit <https://www.geolocation.com/?ip=142.250.68.14>,
you'll see that Google's server is located in Mountain View, CA (i.e. silicon valley).

**Finding your IP address:**

For this assignment, you will need to know your own IP address.
Visit the website <https://whatismyipaddress.com/> to find out your IP address.
If you are connecting to the internet from the campus wireless,
your IP address is probably `134.173.192.64`.
The Claremont Colleges use a technology called [Network Access Translation (NAT)](https://avinetworks.com/glossary/network-address-translation/) to allow many computers to share the same IP address.
This is necessary because there's only a limited supply of IP addresses;
we're [running out](https://en.wikipedia.org/wiki/IPv4_address_exhaustion) and so new IP addresses are [becoming increasingly expensive](https://therecord.media/price-of-ipv4-addresses-one-of-the-internets-hottest-commodities-reaches-all-time-high/).

> **HINT:**
> 
> For muggle-style internet usage,
> NAT usually works okay,
> but it's likely to cause you problems for this assignment.
> Later on, you're going to intentionally get your IP address temporarily banned from accessing certain DPRK webpages.
> If you're working on the campus wireless,
> that means you're going to cause *everyone on campus to get banned*!
> That's not too big of a deal since most people don't access DPRK webpages on a regular basis.
> But it means that two people from this class can't be working on the same IP address at the same time,
> or you'll interfere with each other.
> 
> In order to complete this assignment,
> I recommend working with a different IP address than the campus wifi.
> You can get a different IP address by any of the following methods:
> 1. plugging your computer directly into the wall of your dorm (or if you're living off-campus, just use your off-campus internet),
> 1. using any of the lab computers (since they're plugged into the walls, they are assigned their own unique IPs),
> 1. use wifi tethering with your cellphone (completing this lab should use up less than 100MB of data since we'll only be downloading text documents),
> 1. or working at a coffee shop out in town.
> Or, you can use the campus wifi but just work at an off-time when no one else will be working on this assignment.
 
**Finding an organization's IP addresses:**
 
In order to war dial an organization,
we need to know all of their IP addresses.
This information is all public knowledge,
and the website <https://ipinfo.io> can tell us which IP addresses an organization owns.

An [Autonomous System Number (ASN)](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) is associated with every organization on the internet, and
given an organization's ASN, you can find all of its IP addresses.
For example, you can find all the IP addresses for
1. Google at <https://ipinfo.io/AS15169>, and
1. the Claremont Colleges at <https://ipinfo.io/AS3659>.

In order to find all of the IP addresses for a country,
you can visit the webpage <https://ipinfo.io/countries> and click on a country.
It will list all of the ASNs (i.e. organizations connected to the internet) associated with that country.
The [United States](https://ipinfo.io/countries/us) has 30200 ASNs, the most of any country;
The [DPRK](https://ipinfo.io/countries/kp) has only 1 ASN, the least of any country.

**The DPRK's IP Addresses:**

The DPRK's lone ASN is associated with the Ryugyong-dong ISP,
and you can find it's information at <https://ipinfo.io/AS131279>.

The IP addresses are listed under the field `netblock` in the "IP Address Ranges" table.
For Ryugyong-dong, the table looks something like:

| Netblock         |  Company       | Num of IPs |
| ---------------- | -------------- | ---------- |
| 175.45.176.0/24  |  Ryugyong-dong | 256        |
| 175.45.177.0/24  |  Ryugyong-dong | 256        |
| 175.45.178.0/24  |  Ryugyong-dong | 256        |
| 175.45.179.0/24  |  Ryugyong-dong | 256        |

Recall that each number in an IP address is 8 bits,
so the smallest value is 0 and the largest value is 255.
The `/24` in the netblock is a [subnetmask](https://en.wikipedia.org/wiki/Subnetwork),
which indicates how many IP addresses that Ryugyong-dong owns.
Fully understanding a subnetmask requires a bit of discrete math (MATH055 at CMC),
but basically the `/24` indicates that Ryung-dong owns the next 256 IP addresses (or every IP where the last digit ranges from 0-255).
With all four netblocks, Ryungyong-dong owns every IP starting at `175.45.176.0` up to `175.45.179.255`,
which is 1024 IP addresses in total.
Since the DPRK only owns 1024 IP addresses, and each computer on the internet requires an IP address, only 1024 computers from the DPRK can be connected to the internet at any one time.

In the remainder of this lab, you will write a python program that connects to each of these IP addresses to see if they are currently hosting a webpage.

## Programming Instructions

1. We'll start by working with the website <http://kcna.kp>.
   KCNA stands for the [Korean Central News Agency](https://en.wikipedia.org/wiki/Korean_Central_News_Agency), 
   and is the official newspaper of the DPRK.
   The `.kp` is the [ccTLD](https://en.wikipedia.org/wiki/Country_code_top-level_domain) for the DPRK,
   and all web pages that end in `.kp` are somehow owned by the DPRK.

   Whenever you're scraping a webpage,
   you should always view it in firefox before working with python.
   This will ensure that there are no connectivity issues preventing you from connecting to the webpage. 
   That way, if there's any errors in python,
   you know they're python errors and not internet connection problems.
   Go ahead and visit <http://kcna.kp> in firefox.

   > **NOTE:**
   > 
   > Notice that the scheme in the URLs above is `http://` and not `https://`.
   > If you visit the webpage <https://kcna.kp> you will get a scary warning message about a potential security risk.
   > This is because the KCNA webpage uses an old standard for encrypting the contents of their `https://` webpages which lets other people monitor your communications with the webpage.
   > 
   > Unfortunately, the DPRK does not have the technical know-how in order to implement encryption with the more modern standards.
   > One of the things I teach to North Korean students is how to properly implement this type of encryption so that their internet communications cannot be monitored.
   > Organizations like [Amnesty International](https://www.amnestyusa.org/reports/encryption-a-matter-of-human-rights/) and [Human Rights Watch](https://www.hrw.org/tag/encryption) define strong encryption to be a "human right",
   > and the DPRK actively wants their citizens to learn about encryption.
   > Unfortunately, President Trump signed an executive order banning Americans from traveling to the DPRK (and Biden has reaffirmed this executive order),
   > so current US policy is effectively stopping me from increasing access to human rights in the DPRK.
   > 
   > For the purposes of this assignment,
   > the takeaway of all this discussion is that if you're getting error messages,
   > you should always double check that you used `http://` instead of `https://`.

   Now, let's make sure we can connect to this website from python.
   Run the following code:
   ```
   import requests
   r = requests.get('http://kcna.kp')
   print('r.status_code=', r.status_code)
   ```
   If everything worked correctly, you should get the output
   ```
   r.status_code= 200
   ```

2. Our next step is to connect via IP address instead of domain name.
   To find the IP address for <http://kcna.kp>,
   visit the URL <https://whatismyip.live/dns/kcna.kp>.
   The IP address will look something like `175.45.176.XXX`,
   but with the `XXX` replaced by some numbers.

   Let's connect to this IP address from Python by running the following command (replacing `XXX` with the appropriate number from above):
   ```
   import requests
   r = requests.get('http://175.45.176.XXX')  
   print('r.status=', r.status)
   ```
   This command will probably take a long time to run (1-2 minutes),
   and then barf out a huge error ending in something like:
   ```
   requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))
   ```
   The DPRK's servers are configured so that whenever you connect directly to an IP address,
   rather than to the domain name,
   they servers don't respond.
   Additionally, they give you a 30 minute ban from connecting to that website.
   To verify that you're banned,
   try revisiting the webpage <http://kcna.kp> in firefox.
   You should get a "connection timed out" error message.

   This ban is only for that one website, however.
   Try visiting the website of this other North Korean newspaper in firefox: <http://pyongyangtimes.com.kp>.
   This should still work.
   But if you tried to find the IP address of this website and connect directly, you'd get another ban.

3. In order to scan the DPRK's ip addresses,
   we'll have to circumvent this ban.
   The easiest way to do it is to modify the [HTTP headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields) associated with our requests.
   These headers are a dictionary of key/value pairs that store lots of information about your computer and the type of connection you want.
   Most anti-bot technologies implemented by websites can be circumvented by changing the values of these headers.

   For our purposes, the most important header is the `host` header.
   This header stores the domain name that you are connecting to.
   When the requests library connects to a domain name (using a command like `requests.get('http://kcna.kp')`),
   it does two things:
   1. it looks up the IP address of the domain name using DNS,
   1. and then it connects to that IP address, setting the `host` header to the original domain name.
   When the requests library connects to an IP address (using a command like `requests.get('http://175.45.176.XXX')`, however, the requests library by default leaves the `host` header empty.
   As mentioned in [this stackoverflow question](https://stackoverflow.com/questions/43156023/what-is-http-host-header),
   the HTTP standard technically requires that you provide something in the `host` header.
   So the DPRK's web servers are technically behaving correctly by rejecting our download attempts when we connect directly over the IP address and do not specify a `host` header.

   In order to download the webpage, we must manually specify a value for the `host` header.
   The following command should successfully download the KCNA webpage (assuming your 30 minute ban is over):
   ```
   r = requests.get('http://175.45.176.XXX', headers={'host': 'kcna.kp'})
   print('r.status_code=', r.status_code)
   ```
   
   > **HINT:**
   > 
   > If your 30 minute ban is not over, try doing the above code for the webpage <http://dprkportal.kp> instead.

   The actual value in the `host` header doesn't matter, and can be anything you want.
   So the following will also work:
   ```
   r = requests.get('http://175.45.176.XXX', headers={'host': 'I am a l33t h4x0r'})
   print('r.status_code=', r.status_code)
   ```

4. We now know how to connect to a webserver given the IP address.
   But what if there is no webserver at a particular IP address?

   The IP address `175.45.176.10` is an example of a North Korean IP address with no web server running on it.
   Try connecting to it with the command
   ```
   r = requests.get('http://175.45.176.10', headers={'host': 'this can be anything :)'})
   ```
   After about a minute, you should get a big error message that ends with something like
   ```
   requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='175.45.176.10', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x7ff9719c25c0>, 'Connection to 175.45.176.10 timed out.
   ```
   By catching this exception, we can therefore determine whether a server exists at a given IP.
   For example, the following function does just this:
   ```
   def is_server_at_ip(ip):
       '''
       returns `True` if a server exists at the input IP address;
       otherwise returns `False`
       '''
       try:
           r = requests.get('http://'+ip, headers={'host': 'this can be anything :)'})
           return True
       except requests.exceptions.ConnectTimeout:
           return False
   ```
   This function is still less-than-optimal, however, because it takes a LONG time when there is no IP address on the server.
   (According to the docs, [`requests.get` can technically take forever](https://docs.python-requests.org/en/master/user/quickstart/#timeouts).)
   We can greatly speed up this function by specifying a `timeout` value,
   which is the maximum amount of time that python will wait for a server response.
   The `timeout` is specified in seconds, and 5 seconds is a reasonable amout of time to wait.
   Changing the above code to
   ```
   r = requests.get('http://'+ip, headers={'host': 'this can be anything :)'}, timeout=5)
   ```
   will greatly speed up your function.

5. We're finally ready to war dial.
   The file `war_dial.py` contains three `FIXME` statements.
   Fix those and run the program.
   The completed program will output a list of all IP addresses in the DPRK running web servers.

   > **HINT:**
   >
   > You can check that you've completed the task correctly because (as of 1 Dec 2021), there are 16 servers running in North Korea.
   > If your number is off by 1 or 2, that's probably because the server was down while you were scanning, and that's okay; you don't need to rerun your scan.)

   Upload your completed `war_dial.py` file and the list of all North Korean IP addresses running web servers to sakai.

## Shodan

**You must read this section, but following the links is optional.**

<https://shodan.io> is a search engine for IP addresses that can fully automate the war dialing done in this lab and lots of other "hacking" tasks.
You can find detailed a detailed list of all internet devices connected on North Korean IPs at <https://www.shodan.io/search?query=net%3A175.45.176.0%2F24>.
This list contains more than just web servers, so has a few more results than you'll get from the war dial in this lab.

One of the really trippy things about shodan is that they scan the servers for security vulnerabilities,
and looking at the results list for North Korea,
you can find several North Korean servers with known [remote code execution (RCE)](https://blog.sqreen.com/remote-code-execution-rce-explained/) exploits.
An RCE is one of the worst security vulnerabilities out there.
They allow anyone in the world (who knows the right incantation) to fully take over a remote server and make it do anything they want.
North Korea in the past has been accused of distributing malware on their websites,
but security research firm Kaspesky has found evidence that it was actually a non-North Korean actor who had taken over North Korean webpages.
For a technical analysis, see [Kaspersky's security report](https://securelist.com/whos-really-spreading-through-the-bright-star/68978/) and for a more policy-implications analysis see [the article from thehill.com](https://thehill.com/policy/cybersecurity/234704-did-hackers-plant-the-malware-on-north-koreas-news-site).

There's a good tutorial about shodan online at: <https://danielmiessler.com/study/shodan/>.
There's also some good video tutorials from a conference called DEFCON.
DEFCON is a hacking conference that has a weird mix of academic researchers, black hat criminals, and FBI agents all presenting and sharing their work.
Some shodan videos from the conference are:
1. https://www.youtube.com/watch?v=js840O9zHTE
1. https://www.youtube.com/watch?v=-T-3buBwMEQ
