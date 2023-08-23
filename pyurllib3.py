# urllib3是一个功能强大
# 条理清晰、用于HTTP客户端的Python库，许多Python的原生系统已经开始使用
# urllib3。urllib3提供了很多python标准库里所没有的重要特性，
# 包括:线程安全、连接池、客户端SSL/TLS
# 验证、文件分部编码上传、协助处理重复请求和HTTP重定位、支持压缩编码、支持HTTP和SOCKS代理
# 100%测试覆盖率等
# 在使用urllib3之前
# 需要打开一个cmd窗口使用如下命令进行安装
# > pip install urllib3

# import urllib3
# #需要一个PoolManager实例来生成请求，由该实例对象处理与线程池的连接以及线程安全的所有细节，不需要任何人为操作
# http = urllib3.PoolManager()
# response = http.request('GET','http://www.baidu.com')
# print(response.status)
# print(response.data)

import requests
import urllib3
import urllib3.response
import urllib3.request

http = urllib3.PoolManager()
response = http.request('POST',
                        'https://fanyi.baidu.com/sug'
                        , fields={'kw': '苹果', })
print(response.data)



response = requests.get('http://www.baidu.com')  # 对需要爬取的网页发送请求
print('状态码:', response.status_code)  # 打印状态码
print('url:', response.url)  # 打印请求url
print('header:', response.headers)  # 打印头部信息
print('cookie:', response.cookies)  # 打印cookie信息
print('text:', response.text)  # 以文本形式打印网页源码
print('content:', response.content)  # 以字节流形式打印网页源码
