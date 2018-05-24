# coding:utf8
import socket
import requests
import json

from urllib3.contrib import socks

page = 1
url = 'https://www.huobipro.com/-/x/hb/p/api/contents/pro/list_notice?page={}&limit=50&language=zh-cn'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 ' \
            'Safari/537.36'
headers = {'User-Agent': userAgent}

s = requests.Session()
response = s.request('GET', url.format(page), headers=headers)

print(response)
# print(response.text)
print(response.content.decode('utf-8'))  # 用context方法获取二进制内容再decode，防止乱码

content = response.content.decode('utf-8')
print(json.loads(content))
print(response.json())
print(type(response.json()))
# for page in range(0, response['data']['totalCount']):
#     print(page)


