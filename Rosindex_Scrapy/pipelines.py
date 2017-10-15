# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class RosindexScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if format(item['url']) in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(format(item['url']))
            return item
"""
import csv
class CSVPipeline(object):
    def __init__(self):
        self.file = open('items.csv', 'w')
    def process_item(self, item, spider):
        line = csv.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
"""

import csv
#from Rosindex_Scrapy import settings

#   def write_to_csv(item):
#      writer = csv.writer(open(settin.csv_file_path, 'a'), lineterminator='\n')
#       writer.writerow([item[key] for key in item.keys()])

class UrlsToCsv(object):
    def __init__(self):
        self.csvfile = open('package_links.csv', 'a+')

    def process_item(self, item, spider):
        writer = csv.writer(self.csvfile)
        writer.writerow([format(item['url'])])

    def spider_closed(self, spider):
        self.csvfile.close()


from scrapy.exporters import CsvItemExporter
class CsvPipeline(object):
    def __init__(self):
        self.file = open("repos_links.csv", 'a+')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item