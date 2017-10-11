# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RosindexScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PackageItem(scrapy.Item):
    name=scrapy.Field()
    repository=scrapy.Field()
    ROS_system=scrapy.Field()
    dependency_packages=scrapy.Field()
    dependant_packages=scrapy.Field()
    description=scrapy.Field()

class RepositoryItem(scrapy.Item):
    name=scrapy.Field()
    url= scrapy.Field()
    package_list=scrapy.Field()
    ROS_system=scrapy.Field()
    readme=scrapy.Field()

class ROS_systemItem(scrapy.Item):
    name=scrapy.Field()
    repository_list=scrapy.Field()
    package_list=scrapy.Field()

