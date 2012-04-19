from pySpider import PySpider
if __name__ == '__main__':
    spider = PySpider()
    spider.limit=20
    spider.crawl("http://python.org")