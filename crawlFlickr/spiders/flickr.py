from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request  

from crawlFlickr.items import CrawlflickrItem

import json

class flickrSpider(CrawlSpider):
    name = "flickr"
    allowed_domains = ["www.flickr.com"]
    # start_urls = [
    #     # "https://www.flickr.com/explore/2014/01/01",
    # ]

    # rules = (
    #     Rule(LinkExtractor(allow=('/photos/\w+/\d+/in/\w+-\d+-\d+', )), callback='parse_photo'),
    # )

    def __init__(self, inputFile, *args, **kwargs):
        super(flickrSpider, self).__init__(*args, **kwargs)
        self.inputFile = inputFile

    def start_requests(self):
        inFile = open(self.inputFile,'r')
        for line in inFile:
            photo = json.loads(line)
            yield Request(photo['url'].replace('http','https'), callback=self.parse, meta={'identifier':photo['identifier'], 'User_tags':photo['User tags']})  


    def parse(self, response):
        
        sel = Selector(response)
        item = CrawlflickrItem()

        site = sel.xpath('//li[@id="fave-count"]')
        item['faves'] = site.xpath('a/text()').extract()[0].replace(',',"").replace(u'\xa0',u'0')

        site = sel.xpath('//li[@id="comment-count"]')
        item['comments'] = site.xpath('a/text()').extract()[0].replace(',',"").replace(u'\xa0',u'0')

        site = sel.xpath('//span[@class="story-icon story-views"]/following-sibling::*')
        item['views'] = site.xpath('text()').re('[\d,]+')[0].replace(',',"")

        item['identifier'] = response.meta['identifier']
        item['User_tags'] = response.meta['User_tags']
        yield item

