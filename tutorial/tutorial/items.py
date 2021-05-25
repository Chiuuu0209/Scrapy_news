# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    article = scrapy.Field()
    keyword = scrapy.Field()
