# 3.5.3遍历文档树
# 遍历文档树就是从根节点html标签开始遍历，直到找到目标元素为止。

# (1) .contents属性
# Tag对象的contents属性可以将某个Tag的子节点以列表的方式输出，
# 当然列表会允许用索引的方式来获取列表中的元素。
# 下面是示例代码:


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
print(soup.body.contents)

# (2) .children属性
# Tag对象的.children属性是一个迭代器，可以使用for循环进行遍历，代码如下
# >>> for child in soup.body.children:
# print(child)

print(soup.body.contents[0])

for child in soup.body.children:
    print(child)

# # s所有子孙节点 结果太长 注释掉
# for child in soup.descendants:
#     print(child)

# 节点内容
# tag无标签
print("soup.title:", soup.title)

print("soup.title.string:", soup.title.string)

# tag对象有一个标签
#
print("soup.head:", soup.head)

print("soup.head.string:", soup.head.string)

# 多个标签 strings
for string in soup.strings:
    print(repr(string))

# 使用Tag对象的.stripped_strings属性，可以获得去掉空白行的标签内的众多内容，示例代码如下
print("\n.stripped_strings")
for string in soup.stripped_strings:
    print(string)

# 4.直接父节点
# 使用Tag对象的.parent属性可以获得父节点，使用Tag对象的.parents属性可以获得从父到
# 根的所有节点
# 下面是标签的父节点:
p = soup.p
print("\np.parent.name:", p.parent.name)

# 下面是内容的父节点:
content = soup.head.title.string
print("content:", content)

print("content.parent.name:", content.parent.name)

# Tag对象的.parents属性，得到的也是一个生成器
content = soup.head.title.string
print("content", content)

for parent in content.parents:
    print("# 7生成器content.parents:", parent.name)

# 5.兄弟节点
# 可以使用Tag对象的next_sibling和previous_sibling属性分别获取下一个兄弟结点和
# 获取上一个兄弟结点。
# 需要注意的是，实际文档中Tag的next_sibling和previous_sibling属性通常是字符串或空白，
# 因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行。
# 示例代码如下:
print("# 8", soup.pnext_sibling)
# # 此处返回为空白
print("# 8", soup.prev_sibling)
# None #没有前一个兄弟节点，返回None
print("# 8", soup.p.next_sibling.next_sibling)

# 6.全部兄弟节点
# 可以使用Tag对象的.next_siblings和.previous_siblings属性对当前的兄弟结点迭代输出。示例代码如下
for next in soup.a.next_siblings:
    print("# 9 ", repr(next))

# 7.前后节点
# Tag对象的.next_element和,previous_element属性，用于获得不分层次的前后元素，
# 示例代码如下
print("# 10",soup.head.next_element)
# <title>BigData Software</title>

# 8.所有前后节点
# 使用Tag对象的.next_elements和.previous_elements属性可以向前或向后解析文档内容，示例代码如下:
for element in soup.a.next_elements:
    print("# 11 ",repr(element))

