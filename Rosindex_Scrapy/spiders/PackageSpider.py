# -*- coding: utf-8 -*-
import scrapy
from Rosindex_Scrapy.items import PackageItem

class PackageSpider(scrapy.Spider):
    name = 'PackageSpider'
    custom_settings = {
        'ITEM_PIPELINES': {
            #'app.MyPipeline': 400
        }
    }
    #allowed_domains = ['http://rosindex.github.io/p/agvs_common/']
    start_urls = ['http://http://rosindex.github.io/p/agvs_common//']
""""
    def parse(self, response):
        Package=PackageItem()
        Package['name']=
        Package['url']=
        Package['repository'] =
        Package['ROS_system'] =
        Package['dependency_packages'] =
        Package['dependant_packages'] =
        Package['description'] =
        """
