# Putting it all together: web search

Updated "Instagram architecture" diagram:

<img src='tech-stack.png' width=500px />

## Scaling

1. Vertical scaling: add more RAM/disk/cpu to the same machine
   
   Horizontal scaling: add more machines

   <a href=http://pudgylogic.blogspot.com/2016/01/horizontal-vs-vertical-scaling.html><img src=horizontal-vs-vertical-scaling-vertical-and-horizontal-scaling-explained-diagram.png /></a>

   Tradeoffs:

   1. vertical scaling cheaper, but has an upper limit

   1. horizontal scaling requires about 10x the resources as vertical scaling for the same performance

        but there's no upper limit

1. Stateless process
    1. Easy to scale to multiple machines: just change 1 line in the `docker-compose.yml`
    1. Applies to everything except postgres

1. Postgres
    1. Read only workloads
        1. OLAP = online analytics processing
        1. effectively stateless processes
        1. easy to scale horizontally
        1. search engines, data analytics, and most data science applications fall into this category
        1. just "replicate" your database many times 
            1. adjust the `docker-compose.yml` file
            1. requires some additional work to make sure all the instances get the right database info

    1. Write heavy workloads
        1. OLTP = online transactions processing
        1. difficult to scale to multiple machines
        1. how do you ensure that writes to one machine get *propogated* to the other machnines?
        1. requires extensive modifications to how the database is designed
        1. many possible ways to handle this, each with difference performance tradeoffs
           1. native postgres solutions: https://www.postgresql.org/docs/13/different-replication-solutions.html
           1. extensions: https://wiki.postgresql.org/wiki/Replication,_Clustering,_and_Connection_Pooling#Replication
               1. citus is very popular: https://www.citusdata.com/

1. Design goal
    1. Push as much work as possible into the "stateless processes" because these are easiest to scale horizontally

## Web scraping

Where to get data:

1. The [internet archive](https://archive.org/web/petabox.php)
    1. more than 50 petabytes as of 2014, data goes back into the 90s
    1. the best source of data for what the web looked like in the past
    1. average 40GB/sec (= 13PB/month) data transfer: <http://blog.archive.org/2020/05/11/thank-you-for-helping-us-increase-our-bandwidth/>
    1. the wayback machine is open source
        1. https://github.com/internetarchive/wayback
        1. lots of custom java programs
    1. <img src=AcientAliens-Archive.png width=400px />

1. The [common crawl](https://commoncrawl.org/)
    1. more than 1 petabyte, data goes back to 2008, but significantly more data for recent years
    1. standard archive for scientific research about how the web looks "now"
    1. hosted on Amazon S3
        1. standard method for storing/distributing large static files
        1. excellent record of high uptime, no data loss
        1. pricing: https://aws.amazon.com/s3/pricing/

            <img src=aws-bill.png width=400px />

            1. common crawl's storage fees: ($0.021/GB/month)*(10^6 GB/PB) = $21000/PB/month
            1. data transfer fees: ($0.05/GB)*(10^6 GB/PB) = $50000/PB

    1. example uses
        1. https://commoncrawl.org/the-data/examples/
        1. map discussion of congressional bills: https://github.com/awavering/CC-Bill-Tracker
        1. prevalence of RSS feeds: https://draft.li/blog/2016/03/21/rss-usage-on-the-web/

1. write a scraper manually
    1. not recommended unless you REALLY need fine-grained to control which web pages you get access to
        1. it's hard to do correctly
        1. history: Larry Page (Google co-founder) asking for coding help on a mailing list in 1996: <https://groups.google.com/g/comp.lang.java/c/aSPAJO05LIU/m/ushhUIQQ-ogJ>
    1. every domain has a robots.txt , which describes how a well-behaved spider will interact with the domain
        1. see: <https://developers.google.com/search/docs/advanced/robots/intro>
        1. if you don't obey robots.txt, you'll get banned from the website
        1. most domains favor facebook/googlebot
        1. even these major web companies make mistakes: 
            1. see: [A Facebook crawler was making 7M requests per day to my stupid website](https://news.ycombinator.com/item?id=23490367)
    1. in the US, it is legal to scrape anything that a browser can access normally
        1. see: <https://parsers.me/us-court-fully-legalized-website-scraping-and-technically-prohibited-it/>
        1. websites are free to block your scraper and not allow you to access data
        1. but if you can access it, you can do with it whatever you'd like

Crawl data stored in WARC (= Web ARChive) files

1. standard format for storing web crawl history
    1. invented by the internet archive
    1. evolved from older ARC file format
    1. official format of the library of congress: <https://www.loc.gov/preservation/digital/formats/fdd/fdd000236.shtml>
    1. basically used by everyone; if you write your own scraper, you should use the WARC format too
1. provides a complete history of the HTTP sessions
1. how HTTP works: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>
1. it is not enough to just store the downloaded content!!
    1. status codes: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>
    1. where is the encoding specified?
        1. html level
           ```
           <meta charset="utf-8"/>
           ```
           or
           ```
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
           ```
        1. header level: https://www.w3.org/International/articles/definitions-characters/#httpheader

           not included in the actual HTML file itself => we need to remember this as metadata

        <img src=unicode.jpg width=400px />

Extract information out of html

1. for our search engine, we need to extract
    1. the publication date
    1. title
    1. description
    1. text
1. semantic web

    <img src=beep-borp-semantic-web.jpg width=400px />

    1. google/microsoft/yahoo/yandex/w3c's schema.org: https://schema.org/docs/documents.html
    1. facebook's open graph protocol: https://ogp.me/
    1. twitter card markup: https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/markup
    1. dublin core metadata (dcterms): https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
    1. json-ld: https://json-ld.org/spec/latest/json-ld/
    1. ... and most webpages implement them wrong ...
       
       all international standards for publication date say the format should be `YYYY-MM-DD`,

       but many American websites insist on using `MM-DD-YYYY`
       
       ... and many websites decide to implement their own standard ...

       e.g. BBC, FoxNews

       <img src=standards.png />

1. metahtml: <https://github.com/mikeizbicki/metahtml>
    

**Open Research Task:**

1. How to crawl dynamic webpages?
    1. "obvious" problems
        1. Webpages behind a login (e.g. facebook pages) won't get archived
        1. Google search results won't get archived (we'll never know what results were getting returned for "coronavirus" in January 2020)
        1. Amazon doesn't get archived (dynamically change prices of items, but how can we track that?)
    1. less obvious:
        1. poorly designed webpages like the Korean Central News Agency (KCNA) 
            1. the main newspaper of the DPRK (North Korea)
            1. website is http://kcna.kp
            1. ~~it uses dynamic webpages (i.e. webpage generated by javascript), and so google doesn't index it at all~~

               ~~see: https://www.google.com/search?hl=en&q=site%3Akcna.kp%20united%20states~~

               ~~this issue is technical and not ideological, because Google does index other newspapers hosted in the DPRK, like Pyongyang Times:~~

               ~~see: https://www.google.com/search?q=site%3Apyongyangtimes.com.kp+united+states~~

               North Korea has actually fixed this problem.
               See my block post for more details <https://izbicki.me/blog/fixing-north-korea-kcna-webpage.html>

            1. specialized search engine https://kcnawatch.org exists for searching KCNA~~
                1. requires a subscription payment
                1. not as advanced as google search
        1. google has no incentive to fix this issue because advertisers don't care about these webpages
            1. therefore these webpages effectively don't exist for most people
            1. structural censorship
1. Given an HTML webpage, how can we extract the "article text" from the webpage?
    1. This is a hard problem because there are millions of domains, and each domain does it differently
    1. Not even Google has a good solution to this
    1. Existing solutions "somewhat" work for English, but basically don't work for any other language
        1. not clear if this is because of lack of research, some languages are just harder, or different web standards/design patterns are used in different languages

### Fast Access to Common Crawl/Internet Archive

The CC/IA databases are big... how can we find just specific webpages quickly?

<img src=index-all-the-things-meme.jpg width=400px />

These databases use a custom index format called [CDX](https://iipc.github.io/warc-specifications/specifications/cdx-format/cdx-2015/).

Custom index formats are common for petabyte scale data (actual big data).

1. Recall that postgres has a storage overhead of about 2x in the best case scenario due to its internal file formats.

1. At small/medium data scales, that's insignificant.

    But at real big data scales, that adds up.

    And makes your AWS bill huge.

1. Custom formats can reduce this overhead significantly.

Pre-built CDX indexes are publicly available online and can be queried manually:

1. The CC CDX index: <https://index.commoncrawl.org/>
1. Instructions for IA: <https://support.archive-it.org/hc/en-us/articles/115001790023-Access-Archive-It-s-Wayback-index-with-the-CDX-C-API>

The [cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) is an easy to use python library for accessing these indexes programmatically.

