###
#   Simple Web Crawler
#   Assumptions
#       * Urls to crawl are contained only in <a href="URL" >
#       * All Input to the program is error free
#       * 
#
###

import urllib2
from bs4 import BeautifulSoup
class PySpider:

    def __init__(self):
        self.crawl_queue=[]
        self.crawled = []
        return

    def get_url(self,url):
        response = urllib2.urlopen(url)
        return response.read()

    def get_all_links(self,html):
        soup = BeautifulSoup(html)
        return soup.find_all('a')

    def crawl(self,url):
        print "crawling:" + url
        links = self.get_all_links(self.get_url(url))
        self.crawled.insert(0,url)
        print self.crawled
        for link in links:
            try:
                self.crawl(link.get("href"))
            except(ValueError v):
                print V

if __name__ == '__main__':
    spider = PySpider()
    spider.crawl("http://gautamk.heroku.com")