from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html_doc, "lxml")
content = soup.prettify()
print(content)
# BeautifulSoup将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有
# 对象可以归纳为4种: Tag、NavigableString、 BeautifulSoup、Comment.
# Tag就是HTML中的一个个标签，例如:
# <title>BigData Software</title>
# <a href="http://example.com/hadoop" class="software"id="link1">Hadoop</a>
# 上面的<title>、<a>等标签加上里面包括的内容就是Tag，利用soup加标签名可以轻松地获取
# 这些标签的内容。作为演示，我们可以继续执行以下代码:

print(soup.a)

print(soup.title)


print(soup.name)
print(soup.p.attrs)


print(soup.p['class'])
print(soup.p.get('class'))





