# 初始化的时候一般有三种传入方式：传入字符串，传入url,传入文件
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''

# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc)
# print(type(doc))
# print(doc('li'))

#URL初始化
# from pyquery import PyQuery as pq
# doc = pq(url="http://www.baidu.com",encoding='utf-8')
# # print(doc('head'))
# print(doc('href'))

# 子元素
# children,find
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('href')
# print(type(lis))
# print(lis)


# 兄弟元素 siblings
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())


#遍历元素
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)

# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(type(li))
#     print(li)


# 获取属性pyquery对象.attr(属性名) pyquery对象.attr.属性名
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)


# addClass、removeClass
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)


# remove taglib
htm = '''
<div class="wrap">
    hello python 
    <p>this is a paragraph</p>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(htm)
wrap = doc('.wrap')
# print(wrap.text())
wrap.find('p').remove()
print(wrap.text())









