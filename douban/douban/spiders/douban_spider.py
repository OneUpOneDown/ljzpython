# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'douban_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']

    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        # pass
        print('.................................')
        print(response.css('title'))
        print('.................................')
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
        	print(i_item)
