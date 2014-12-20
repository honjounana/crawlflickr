# -*- coding: utf-8 -*-

# Scrapy settings for crawlFlickr project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawlFlickr'

SPIDER_MODULES = ['crawlFlickr.spiders']
NEWSPIDER_MODULE = 'crawlFlickr.spiders'

COOKIES_ENABLES=False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlFlickr (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'crawlFlickr.pipelines.CrawlflickrPipeline':300
}