import requests

# base_url = 'https://httpbin.org'
# param_data = {'user': 'xmu', 'password': '123456'}
# response = requests.get(base_url + '/get', params=param_data)
# print(response.url)
# print(response.status_code)

# url = 'https://www.bilibili.com'
# # 创建头部信息
# headers = {
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
# response = requests.get(url, headers=headers)
# print(response.content)

import requests
url='http://httpbin.org'
# 创建头部信息
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
response = requests.get(url,headers=headers)
print(response.content)

