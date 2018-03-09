# -*- coding: utf-8 -*-
import scrapy
from news_spider.items import NewsSpiderItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.http import Request
import urllib
import urllib2
import re
'''
cd /Users/yuandarong/news_spider/news_spider

scrapy crawl news_spider -o news36kr4.json

'''
class NewsSpider(CrawlSpider):
    name = 'news_spider'
    def start_requests(self):
        sta_urls = 'http://36kr.com/p/'
        i = 5058805

        while i <= 5058805:
            sta_urlss=sta_urls
            sta_urlss+=str(i)
            sta_urlss+='.html'
            print(sta_urlss)
            i = i - 1
            yield scrapy.Request(url = sta_urlss,callback=self.parse_item)

    def parse_item(self,response):

        datePattern = re.compile(r'\"user_id\":\".*?\",\"published_at\":\"(.*?)\",\"created_at\"', re.S)
        date = re.findall(datePattern, response.body)
        date = date[0]
        titlePattern = re.compile(r'content=\"article\" /><meta property=\"og:title\" content=\"(.*?)\" />', re.S)
        title = re.findall(titlePattern,response.body)
        title = title[0]
        contentPattern = re.compile(r'\"content\":\"(.*?)</p>\",\"cover\":', re.S)
        content = re.findall(contentPattern, response.body)

        ''''
        url = response.url
        '''
        imgPattern = re.compile('<img.*?>')
        hTagPattern = re.compile('<h\d.*?>|<h>|</h\d>|</h>')
        brPattern = re.compile('<br>|</br>|<br/>')
        addrPattern = re.compile('<a.*?>|</a>')
        pTagPattern = re.compile('<p>|</p>|<p.*?>')
        spanTagPattern = re.compile('<span>|</span>')
        strongTagPattern = re.compile('<strong>|</strong>')
        url = response.url
        '''
        
        content = [n.encode('utf-8')for n in content]
        '''
        for i in range(len(content)):
            content[i] = re.sub(imgPattern, '[img]', content[i])
            content[i] = re.sub(brPattern, '\n', content[i])
            content[i] = re.sub(hTagPattern, '\n', content[i])
            content[i] = re.sub(addrPattern, '', content[i])
            content[i] = re.sub(spanTagPattern, '', content[i])
            content[i] = re.sub(pTagPattern, '', content[i])
            content[i] = re.sub(strongTagPattern, '', content[i])

        '''
        
        date =  sel.xpath('//abbr[@class="time"]/text()').extract()
        content = sel.xpath('//section[@class="textblock"]/text()').extract()
        
        item['title'] = [n.encode('utf-8')for n in title]
        item['url'] = [n.encode('utf-8') for n in url]
        
        item['date'] = [n.encode('utf-8') for n in date]
        item['content'] = [n.encode('utf-8') for n in content]
        '''
        yield {"title":title,
                "date": date,
                "content":content[0],
               "url":url


               }


