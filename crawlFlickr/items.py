# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlflickrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    views = scrapy.Field()
    faves = scrapy.Field()
    comments = scrapy.Field()
    identifier = scrapy.Field()
    User_tags = scrapy.Field()
