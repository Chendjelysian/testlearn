html_text = """
<html>
  <body>
    <head><title>BigData Software</title></head>
    <p class="title"><b>BigData Software</b></p>
    <p class="bigdata">There are three famous bigdata software;and their names are
      <a href="http://example.com/hadoop" class="bigdata Hadoop" id="link1">Hadoop</a>,
      <a href="http://example.com/spark" class="bigdata Spark" id="link2">Spark</a>and
      <a href="http://example.com/flink" class="bigdata Flink" id="link3"><!--Flink--></a>;
        and they are widely used in real application.</p>
    <p class="bigdata">others</p>
    <p>……</p>
  </body>
</html>
"""
from lxml import etree

html = etree.HTML(html_text)
html_data = html.xpath('body')
print(html_data)
# [<Element body at 0x1608dda2d80>]


# XPath选取节点时，是沿着路径到达目标，表3-3列出了常用的表达式
# 表3-3常用表达式
# 表达式
# nodename 描述选取nodename节点的所有子节点
# /        从根节点开始选取
# //       从当前文档选取所有匹配的节点，而不考虑它们的位置
# @        选取属性
# .         选取当前节点
# ..        选取当前节点的父节点


# 可以看出，html.xpath(body”的输出结果不是像HTML里面那样显示的标签，其实这就是我们所要
# 的元素，只不过我们还需要再进行一步操作，也就是使用etree中的.tostring()方法将其进行转换。此
# 外，html.xpath(“body”的输出结果是一个列表，因此，我们可以使用for循环来遍历列表，具体代码如
# 下:
# for element in html_data:
#     print(etree.tostring(element))

# “//”表示全局搜索，比如，“//p”可以将所有的<p>标签搜索出来。“/”表示在某标签下进行搜
# 索，只能搜索子节点，不能搜索子节点的子节点。
# 简单来说，“//”可以进行跳级搜索，“”只能在本级上进行搜索，不能跳跃。下面是具体实例:


# 逐级搜索
html_data = html.xpath('/html/body/p/a')
for element in html_data:
    print("#2 ", etree.tostring(element))

# 跳级搜索
html_data = html.xpath('//a')
for element in html_data:
    print("#3 ", etree.tostring(element))

# 可以在方括号内添加“@”，将标签属性填进去，这样就可以准确地将含有该标签属性的部分提!
# 出来，示例代码如下:

html_data = html.xpath('//pa[@class = "bigdata spark"]')
for element in html_data:
    print(etree.tostring(element))


# (2) 谓语
# 直接使用前面介绍的方法可以定位到多数我们需要的节点，但是有时候我们需要查找某个特定的节点
# 或者包含某个指定值的节点，就要用到谓语。谓语是被嵌在方括号中的。表3-4列出了一些带有谓语的
# 路径表达式及其描述的内容。
# 表3-4带有谓语的路径表达式实例
# 路径表达式                 描述
# //body/p[k]                   选取所有body下第k个p标签 (k取值从1开始)
# //body/p[last()]              选取所有body下最后一个p标签
# //body/p[last()-1]            选取所有body下倒数第二个p标签
# //body/p[position()<3]        选取所有body下的前两个p标签
# //body/p[@class]              选取所有body下的带有class属性的p标签
# //body/p[@class="bigdata"]    选取所有body下的,class为bigdata的p标签


# xPath中提供超过100个内建函数用于字符串值、数值、日期和时间比较序列处理等操作，极大地方
# 便了我们定位获取所需要的信息。表3-5列出了几个常用的函数。
# 表3-5常用函数
# 函数名              # 描述
# contains()        选取属性或文本包含某些字符
# //p[contains(@class, "bigdata")]  # 选取所有class属性包含bigdata的p标签

# starts-with()   # 选择属性或文本以某些字符开头
# //a[starts-with (@class,"bigdata")]
# 选取所有class属性以bigdata开头的a标签


# ends-with()       # 选取属性或文本以某些字符结尾
# //a[ends-with(@class,"Flink")]
# 选取所有class属性以Flink结尾的a标签

# text()            # 获取元素节点包含的文本内容
# //a[contains("Hadoop")]//text()
# 获取所有class属性包含Hadoop的a标签中的文本内容