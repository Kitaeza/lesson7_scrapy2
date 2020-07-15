from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from leroymerlin import settings
from leroymerlin.spiders.lmru import LmruSpider

if __name__ == '__main__':
    unit = 'бассейн'

    crowler_settings = Settings()
    crowler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crowler_settings)
    process.crawl(LmruSpider, unit)

    process.start()
