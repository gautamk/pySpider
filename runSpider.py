from pySpider import PySpider
if __name__ == '__main__':
    spider = PySpider()
    spider.limit=0
    spider.crawl("http://gautamk.github.com/pySpider/root.html")