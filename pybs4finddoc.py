#
#
#
# 搜索文档树是通过指定标签名来搜索元素，另外还可以通过指定标签的属性值来精确定位某个节点元素
# ，最常用的两个方法就是find()和find all()，
# 两个方法在BeatifulSoup和Tag对象上都可以被调用。

html_doc = """
<html><head><title>BigData Software</title></head>
<p class="title"><b>BigData Software</b></p>
<p class="bigdata">There are three famous bigdata softwares; and their names are
<a href="http://example.com/hadoop" class="software" id="link1">Hadoop</a>,
<a href="http://example.com/spark" class="software" id="link2">Spark</a> and
<a href="http://example.com/flink" class="software" id="link3">Flink</a>;
and they are widely used in real applications.</p>
<p class="bigdata">...</p>
"""
from bs4 import BeautifulSoup, element

soup = BeautifulSoup(html_doc, "lxml")

# name参数

# 1.find all()
# find_all()方法搜索当前Tag的所有Tag子节点，并判断是否符合过滤器的条件，它的函数原型是
# find all( name , attrs , recursive , text , **kwargs )
# find all()的返回值是一个Tag组成的列表，方法调用非常灵活，所有的参数都是可选的。

# 1. name
# name参数可以查找所有名字为name的Tag，字符串对象会被自动忽略掉
# 传
# 查找所有名字为a的Tag，代码如下:
print("# 1", soup.find_all('a'))

# 2. 传正则表达式
# 如果传入正则表达式作为参数，Beautifulsoup会通过正则表达式的match(来匹配内容下面例子中找出
# 所有以b开头的标签，这表示<body>和<b>标签都应该被找到:

import re

for tag in soup.find_all(re.compile("^b")):
    print("# 2 ", tag)

# 3.传入列表
# 如果传入参数是列表，BeautifulSoup会将与列表中任一元素匹配的内容返回。下面代码找
# 到文档中所有<a>标签和<b>标签!
print("# 3 ", soup.find_all(["a", "b"]))

# 4.传入True
# 传入True可以找到所有的标签。下面的例子在文档树中查找所有包含id属性的标签，
# 无论id的值是什么:
print("# 4 ", soup.find_all(id=True))


# 5方法
# 如果没有合适过滤器，那么还可以定义一个方法，方法只接受一个元素参数，
# 如果这个方法返回True表示当前元素匹配并且被找到，如果不是则返回False。
# 下面方法对当前元素进行校验，如果包含class属性却不包含id属性，那么将返回True:
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


# 将这个方法作为参数传入find_all()方法，将得到所有<p>标签:
print("# 5 ", soup.find_all(has_class_but_no_id))

# keyword参数

# 通过name参数是搜索Tag的标签类型名称，如ahead、title等
# 如果要通过标签内属性的值来搜索要通过键值对的形式来指定，实例如下:

print("# 6 ", soup.find_all(id='link2'))
# [<a class="software" href="http://example.com/spark" id="link2">Spark</a>]
print("# 6 ", soup.find_all(href=re.compile("spark")))

# 使用多个指定名字的参数可以同时过滤Tag的多个属性:
soup.find_all(href=re.compile("hadoop"), id='link1')

# 如果指定的key是Python的关键词，则后面需要加下划线:
print("# 6 ", soup.find_all(class_="software"))

# text
# (3) text参数
# text参数的作用和name参数类似，但是text参数的搜索范围是文档中的字符串内容(不包含注释
# 并且是完全匹配，当然也接受正则表达式、列表、True。实例如下:

print("# 7 ", soup.a)

print("# 7 ", soup.find_all(string="Hadoop"))

print("# 7 ", soup.find_all(text=["Hadoop", "Spark", "Flink"]))

print("# 7 ", soup.find_all(text="bigdata"))
print("# 7 ", soup.find_all(text="BigData Software"))

print("# 7 ", soup.find_all(text=re.compile("bigdata")))

#
# (4)limit参数
# 可以通过limit参数来限制使用name参数或者attrs参数过滤出来的条目的数量，实例如下:
print("# 8 ", soup.find_all("a"))

print("# 8 ", soup.find_all("a", limit=2))


# (5) recursive 参数
# 调用Tag的find_all()方法时，BeautifulSoup会检索当前Tag的所有子孙节点，
# 如果只想搜索Tag的直接子节点，可以使用参数recursive=False，实例如下:

print("# 9 ", soup.body.find_all("a", recursive=False))

# 在这个例子中，a标签都是在p标签内的，所以在body的直接子节点下搜索a标签是无法匹配到a标签的。
# 2.find()
# find(与find al()的区别是，find al()将所有匹配的条目组合成一个列表，
# 而find()仅返回第一个匹配的条目，除此以外，二者的用法都相同。

