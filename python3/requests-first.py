#!/usr/bin/env python
import requests

response = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(response.content)
print(response.content.decode("utf-8"))