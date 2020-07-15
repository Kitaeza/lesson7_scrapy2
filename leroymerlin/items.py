# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def specification_gen(keys, values):
    if not value: return []
    print(1)
    # item['price'] = item['price'].replace(' ', '')
    # item['spec_vals'] = [key.replace('\n', '').strip() for key in item['spec_vals']]
    # item['specifications'] = dict(zip(item['spec_keys'], item['spec_vals']))
    # del item['spec_keys']
    # del item['spec_vals']

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
    specifications = scrapy.Field(input_processor=MapCompose(specification_gen))
    photos = scrapy.Field()
    pass
