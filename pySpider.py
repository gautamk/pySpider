###
#   Simple Web Crawler
#   Assumptions
#       * Urls to crawl are contained only in <a href="URL" >
#
###

import urllib2
from bs4 import BeautifulSoup
class PySpiderRecursive:

    def __init__(self):
        self.crawled = open("crawled.txt",'w')

    def get_url(self,url):
        response = urllib2.urlopen(url)
        return response.read()

    def get_all_links(self,html):
        soup = BeautifulSoup(html)
        return soup.find_all('a')

    def crawl(self,url):
        print "crawling:" + url
        links = self.get_all_links( self.get_url(url) )
        self.crawled.write(url+"\n")
        for link in links:
            try:
                self.crawl( link.get("href" ) )
            except ValueError:
                print "Ignoring="+link.get('href')
                pass
    def __del__(self):
        self.crawled.close()

if __name__ == '__main__':
    spider = PySpiderRecursive()
    spider.crawl("http://gautamk.heroku.com")