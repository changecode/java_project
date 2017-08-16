item pipeline
===

process_item(self,item,spider) 每个item piple组件是一个
独立Python类，必须实现以process_item(self,item,spider)
方法，每个item pipeline组件都需要调用该方法，该方法返回
一个具有数据的dict 或item对象或者抛出DropItem异常。被丢
弃的item将不会被之后的pipeline组件所出来

open_spider(self,spider):表示当spider被开启的时候调用
该方法

close_spider(self,spider)


一些使用例子
===

1、判断item中是否包含price以及price_excludes_vat，如果
存在则调整price属性，都让item['price'] = item['price'] *
self.vat_factor，如果不存在则返回DropItem

		from scrapy.exceptions import DropItem
		class PricePipeline(object):
			var_factor = 1.15
			def process_item(self,item,spider):
				if item['price']:
					if item['price_excludes_vat']:
						item['price'] = item['price'] *
						self.vat_factor
					return item
				else:
					raise DropItem("missing price in %s" %item)		

2、将item写入json文件中
		
		import json
		class JsonWriterPipeline(object):
			def __init__(self):
				self.file = open('items.j1','wb')
			def process_item(self,item,spider):
				line = json.dumps(dict(item)) + "\n"
				self.file.write(line)
				return item

3、将item写入到mongodb

		import pymongo
		class MongoPipeline(object):
			collection_name = 'scrapy_items'

			def __init__(self,mongo_uri,mongo_db):
				self.mongo_uri = mongo_uri
				self.mongo_db = mongo_db

			@classmethod
			def from_crawler(cls, crawler):
				return cls(
					mongo_uri = crawler.settings.get('MONGO_URI'),
					mongo_db = crawler.settings.get('MONGO_DATABASE','items')
				)										

			def open_spider(self,spider):
				self.client = pymongo.MongoClient(self.mongo_uri)
				self.db = self.client[self.mongo_db]

			def close_spider(self, spider):
				self.client.close()

			def process_item(self,item,spider):
				self.db[self.collection_name].insert(dict(item))
				return item

4、去重
		from scrapy.exceptions import DropItem
		class DuplicatesPipeline(object):

			def __init__(self):
				self.ids_seen = set()

			def process_item(self,item,spider):
				if item['id'] in self.ids_seen:
					raise DropItem("Duplicate item found: %s" %item)
				else:
					self.ids_seen.add(item['id'])
					return item								
启用一个item pipeline组件：在settings配置文件中
TEM_PIPELINES = {
    'myproject.pipelines.PricePipeline': 300,
    'myproject.pipelines.JsonWriterPipeline': 800,
}
每个pipeline后面有一个数值，这个数组的范围是0-1000，这个数值确定了他们的运行顺序，数字越小越优先
