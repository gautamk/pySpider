pySpider
========

#####Your friendly neighbourhood eight-legged crawler

####Requirements
 * Beautiful Soup 4

####Usage 
First import `PySpider` from `pySpider`

    from pySpider import PySpider

Then create a new instance of the crawler

    spider = PySpider

Set the maximum limit for the number of links to crawl, Set 0 for infinite

    spider.limit = 1

The start the crawl

    spider.crawl("http://python.org")
