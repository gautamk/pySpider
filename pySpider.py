###
#   Simple Web Crawler
#   Assumptions
#       * Urls to crawl are contained only in <a href="URL" >
#       * Only absolute URLS are valid, Relative Urls are not allowed
#       * Not checking for Duplicates because of increased time complexity
#       * Urls point for HTML documents 
#
###

import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse
class PySpider:

    def __init__(self):
        self.file_name="crawled.txt"
        self.crawled = open(self.file_name,'w')
        self.crawled.write("[crawled_links]\n")
        self.repo = [] # A repository of links
        self.limit = 0 # Limit the number of links visited. 0 means infinite

    def get_url(self,url):
        response = urllib2.urlopen(url)
        return response.read()

    def get_all_links(self,html):
        soup = BeautifulSoup(html)
        return soup.find_all('a')

    def is_valid_url(self,url):
        if url is None :return False
        url = urlparse(url)
        if url.scheme   is  ""  or  url.scheme   is None: return False
        if url.hostname is  ""  or  url.hostname is None: return False
        return True

    def enqueue(self,url):
        if self.is_valid_url(url): self.repo.insert(0,url)

    def dequeue(self):
        return self.repo.pop()

    def crawl(self,url):
        if not self.is_valid_url(url): return False
        self.enqueue(url)
        link_count = 0
        while self.repo.__len__() > 0:
            print link_count
            self.__crawl__()
            link_count+=1
            if link_count >= self.limit and self.limit > 0: break


    def __crawl__(self):
        url = self.dequeue()
        print "crawling "+url
        self.crawled.write(url+"\n")
        links = self.get_all_links(self.get_url(url))
        for link in links :
            self.enqueue(link.get("href"))

    def __del__(self):
        self.crawled.write("[un_crawled_links]\n")
        for link in self.repo:
            self.crawled.write(link+"\n")
        self.crawled.close()

