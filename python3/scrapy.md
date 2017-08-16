scrapy工作流程
===

1、以初始的URL初始化Request，并设置回调函数，当该request
下载完毕并返回时，将生成response，并作为参数传给回调函数
spider中初始的request是通过start_requests()来获取的。
start_requests获取start_urls中的url，并以parse以回调函数
生成request

2、在回调函数内分析返回的网页内容，可以返回item对象或者
dict或者request以及一个包含三者的可迭代的容器，返回的
request对象之后会经过scrapy处理，下载相应的内容，并调用设置的callback函数

3、在回调函数内，可以通过lxml bs4 xpath css等方法获取
想要的内容生产item

4、最后将item转递给pipeline处理

5、item pipeline的主要作用
	清理HTML数据
	验证爬取得数据
	去重并丢弃
	将爬取得结果保存到数据库中或文件中


spider内的一些常用属性
===

name:定义爬虫名字，通过命令启动的时携带此参数

allowed_domains:包含了spider允许爬取得域名列表。当

offsiteMiddleware启用时，域名不在列表中，URL不会被访问
所以在爬虫文件中，每次生成request请求时都会进行和这里的
域名进行判断

starturls:起始的URL列表，通过spider.Spider方法中会调用start_requests循环请求这个列表的每个地址

custom_settings:自定义配置，可以覆盖setttings的配置，参
树是以字典的方式设置:custom_settings = {}

from_crawler:可以通过crawler.settings.get方式获取settings配置文件中的信息，同时这个也可以在pipeline中使用

start_requests:返回一个可迭代对象，该对象包含了spider用
于爬取得第一个request请求。这个方法时在被继承的父类中
spider.Spider,默认是通过get请求，如果需要修改最开始的这
个请求，可以重写这个方法，比如通过post请求

make_requests_from_url(url):在父类中start_requests调用

parse(response):回调函数，处理response并返回处理的数据
以及跟进的URL，该方法以及其他的request回调函数必须返回
一个包含request或者item的可迭代对象