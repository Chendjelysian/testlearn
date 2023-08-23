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

#
#
# BeautifulSoup支持大部分的css选择器
# 在Tag或BeautifulSoup对象的select()方法中传入字符串参数
# 即可使用css选择器的语法找到标签

# 通过标签名查找
soup = BeautifulSoup(html_doc, "lxml")

print("# 1", soup.select('title'))

print("# 1", soup.select('a'))

# 2.通过类名查找
print("# 2", soup.select('.software'))

# 3.通过id名找
print("# 3", soup.select('#link1'))

# 4.组合查找

print("# 4", soup.select('p #link1'))

print("# 4", soup.select("head > title"))

print("# 4", soup.select("p > a:nth-of-type(1)"))

print("# 4", soup.select("p > a:nth-of-type(2)"))

print("# 4", soup.select("p > a:nth-of-type(3)"))

# 在上面的语句中，"p>a:nth-of-type(2)的含义是:a元素是某个父元素p的子元素，选择子元素a
# 且子元素a必须是其父元素p下的第二个a元素


# 属性查找
# 查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，
# 所以中间不能加空格，否则会无法匹配到。
print("# 5", soup.select('a[class="software"]'))

print("# 5", soup.select('a[href="http://example.com/hadoop"]'))

print("# 5", soup.select('p a[href="http://example.com/hadoop"]'))


# 以上的select方法返回的结果都是列表形式，可以以遍历的形式进行输出，然后用get_text()方法
# 来获取它的内容，实例如下:
print("# 6", type(soup.select('title')))

print("# 6", soup.select('title')[0].get_text())

for title in soup.select('title'):
    print("# 6", title.get_text())
# 上面语句的执行结果如下:
# BigData Software