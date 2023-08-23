# urllib是Python自带模块，该模块提供了一个urlopen()方法，通过该方法指定URL发送HTTP请求来获
# 取数据。urlib提供了多个子模块，具体的模块名称与功能如表3-1所示。
# 表3-1urllib中的子模块
# 模块名称
# urllib.request 该模块定义了打开URL(主要是HTTP)的方法和类，如身份验
# # 证、重定向和cookie等
# urllib.error 该模块中主要包含异常类，基本的异常类是URLError
# urllib.parse该模块定义的功能分为两大类: URL解析和URL引用
# urllib.robotparser该模块用于解析robots.txt文件


import urllib.request
import urllib.parse

response = urllib.request.urlopen("https://www.baidu.com/")

html = response.read()
print(html)



# 1.指定url
url = 'https://fanyi.baidu.com/sug'
# 2.发起POST请求之前，要处理POST请求携带的参数# 2.1 将POST请求封装到字典
data = {'kw': '苹果', }
data = urllib.parse.urlencode(data)
# 转换为byte
data = data.encode()
# 3.发起POST请求:urlopen函数的data参数表示的就是经过处理之后的POST请求携带的参数
response = urllib.request.urlopen(url = url, data =data)
data = response.read()
print(data)

