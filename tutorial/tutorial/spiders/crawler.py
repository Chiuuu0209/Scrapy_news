import scrapy
from tutorial.items import MyItem

import re
import requests

# 3rd lib
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup

from crawler_dev import parse

class GoogleNewsCrawler(scrapy.Spider):
    name = 'GoogleNews'
    start_urls = ['https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant']
    def parse(self,response):
        res = BeautifulSoup(response.body,features="lxml")
        url = ""
        for news in res.select('div .NiLAwe'):
            print("main",news.select('h3')[0].text,)
            yield MyItem(title=news.select('h3')[0].text)
            relative_url = response.urljoin(news.select('a')[0]['href'])
            page = requests.get(relative_url)
            yield MyItem(link=str(page.url))
            yield self.parse_detail(str(page.url))
    def parse_detail(self,url):
        gooleitem = MyItem()
        date, title, article, keyword, = parse(url)
        # gooleitem['date'] = date
        # gooleitem['title'] = title
        # gooleitem['article'] = article
        # gooleitem['keyword'] = keyword

        print(title)
        print(date)
        print(article)
        print(keyword)
        yield MyItem(date=date)
        yield MyItem(title=title)
        yield MyItem(article=article)
        yield MyItem(keyword=keyword)
        
