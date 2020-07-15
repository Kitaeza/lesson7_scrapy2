# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeroymerlinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    unit = scrapy.Field()
    spec_keys = scrapy.Field()
    spec_vals = scrapy.Field()
    specifications = scrapy.Field()
    photos = scrapy.Field()
    pass
