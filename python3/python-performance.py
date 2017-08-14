#简单循环，最耗时
# import requests

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.ifeng.com'
# ]

# for url in url_list:
# 	result = requests.get(url)
# 	print(result.text)


#通过线程池方式
# import requests
# from concurrent.futures import ThreadPoolExecutor

# def fetch_request(url):
# 	result = requests.get(url)
# 	print(result.text)

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.ifeng.com'
# ]

# pool = ThreadPoolExecutor(10)

# for url in url_list:
# 	pool.submit(fetch_request,url)

# pool.shutdown(True)


#线程池加回调函数
# from concurrent.futures import ThreadPoolExecutor
# import requests

# def fetch_async(url):
# 	response = requests.get(url)
# 	return response

# def callback(future):
# 	print(future.result().text)

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.ifeng.com'
# ]		

# pool = ThreadPoolExecutor(3)

# for url in url_list:
# 	v = pool.submit(fetch_async,url)
# 	v.add_done_callback(callback)

# pool.shutdown()	


#进程池方式
# import requests
# from concurrent.futures import ProcessPoolExecutor

# def fetch_request(url):
# 	result = requests.get(url)
# 	print (result.text)

# url_list = [
# 	'http://www.baidu.com',
# 	'http://www.ifeng.com'
# ]	

# pool = ProcessPoolExecutor(10)

# for url in url_list:
# 	pool.submit(fetch_request,url)

# pool.shutdown()	


#主流的单线程实现并发的几种方式

#asyncio例子1
# import asyncio
# @asyncio.coroutine #通过这个装饰器装饰
# def func1():
#     print('before...func1......')
#     # 这里必须用yield from，并且这里必须是asyncio.sleep不能是time.sleep
#     yield from asyncio.sleep(2)
#     print('end...func1......')

# tasks = [func1(), func1()]

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

#asyncio例子2
# import asyncio

# @asyncio.coroutine
# def fetch_async(host, url='/'):
#     print("----",host, url)
#     reader, writer = yield from asyncio.open_connection(host, 80)

#     #构造请求头内容
#     request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
#     request_header_content = bytes(request_header_content, encoding='utf-8')
#     #发送请求
#     writer.write(request_header_content)
#     yield from writer.drain()
#     text = yield from reader.read()
#     print(host, url, text)
#     writer.close()

# tasks = [
#     fetch_async('www.cnblogs.com', '/zhaof/'),
#     fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
# ]

# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

# asyncio + aiohttp
# import aiohttp
# import asyncio

# @asyncio.coroutine
# def fetch_async(url):
#     print(url)
#     response = yield from aiohttp.request('GET', url)
#     print(url, response)
#     response.close()

# tasks = [fetch_async('http://baidu.com/'), fetch_async('http://www.chouti.com/')]

# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()

#asyncio+requests
# import asyncio
# import requests

# @asyncio.coroutine
# def fetch_async(func, *args):
#     loop = asyncio.get_event_loop()
#     future = loop.run_in_executor(None, func, *args)
#     response = yield from future
#     print(response.url, response.content)

# tasks = [
#     fetch_async(requests.get, 'http://www.cnblogs.com/wupeiqi/'),
#     fetch_async(requests.get, 'http://dig.chouti.com/pic/show?nid=4073644713430508&lid=10273091')
# ]

# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

#gevent+requests
import gevent

import requests
from gevent import monkey

monkey.patch_all()


def fetch_async(method, url, req_kwargs):
    print(method, url, req_kwargs)
    response = requests.request(method=method, url=url, **req_kwargs)
    print(response.url, response.content)

# ##### 发送请求 #####
gevent.joinall([
    gevent.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
    gevent.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
    gevent.spawn(fetch_async, method='get', url='https://github.com/', req_kwargs={}),
])

# ##### 发送请求（协程池控制最大协程数量） #####
# from gevent.pool import Pool
# pool = Pool(None)
# gevent.joinall([
#     pool.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
#     pool.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
#     pool.spawn(fetch_async, method='get', url='https://www.github.com/', req_kwargs={}),
# ])


#grequests代码例子
import grequests

request_list = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),
    grequests.get('http://fakedomain/'),
    grequests.get('http://httpbin.org/status/500')
]

# ##### 执行并获取响应列表 #####
# response_list = grequests.map(request_list)
# print(response_list)


# ##### 执行并获取响应列表（处理异常） #####
# def exception_handler(request, exception):
# print(request,exception)
#     print("Request failed")

# response_list = grequests.map(request_list, exception_handler=exception_handler)
# print(response_list)


#twisted代码例子
#getPage相当于requets模块，defer特殊的返回值，rector是做事件循环
from twisted.web.client import getPage, defer
from twisted.internet import reactor

def all_done(arg):
    reactor.stop()

def callback(contents):
    print(contents)

deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)
#这里就是进就行一种检测，判断所有的请求知否执行完毕
dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()


# tornado代码例子
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop


def handle_response(response):
    """
    处理返回值内容（需要维护计数器，来停止IO循环），调用 ioloop.IOLoop.current().stop()
    :param response: 
    :return: 
    """
    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)


def func():
    url_list = [
        'http://www.baidu.com',
        'http://www.bing.com',
    ]
    for url in url_list:
        print(url)
        http_client = AsyncHTTPClient()
        http_client.fetch(HTTPRequest(url), handle_response)


ioloop.IOLoop.current().add_callback(func)
ioloop.IOLoop.current().start()