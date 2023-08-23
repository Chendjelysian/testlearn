import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

# load_iris 返回的 iris 对象是一个 Bunch 对象，与字典非常相似，里面包含键和值
print("Keys of iriss_dataset: \n{}".format(iris_dataset.keys()))

# DESCR 键对应的值是数据集的简要说明。我们这里给出说明的开头部分
print(iris_dataset['DESCR'][:100] + "\n...")

# target_names 键对应的值是一个字符串数组，里面包含我们要预测的花的品种：
print("Target names: {}".format(iris_dataset['target_names']))

# feature_names 键对应的值是一个字符串列表，对每一个特征进行了说明
print("Feature names: \n{}".format(iris_dataset['feature_names']))
# 数据包含在 target 和 data 字段中。
# data 里面是花萼长度、花萼宽度、花瓣长度、花瓣宽度的测量数据，


# data 数组的每一行对应一朵花，列代表每朵花的四个测量数据
print("Type of data: {}".format(type(iris_dataset['data'])))

print("Shape of data: {}".format(iris_dataset['data'].shape))

# 数组中包含 150 朵不同的花的测量数据。前面说过，机器学习中的个体叫作样本（sample），
# 其属性叫作特征（feature）。data 数组的形状（shape）是样本数乘以特征数。
# 这是 scikit-learn 中的约定，你的数据形状应始终遵循这个约定。


# 前 5 个样本的特征数值
print("First five rows of data:\n{}".format(iris_dataset['data'][:5]))

# target 数组包含的是测量过的每朵花的品种，也是一个 NumPy 数组：
# target 是一维数组，每朵花对应其中一个数据：
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))

# 品种被转换成从 0 到 2 的整数：
print("Target:\n{}".format(iris_dataset['target']))

# scikit-learn 中的 train_test_split 函数可以打乱数据集并进行拆分。

# scikit-learn 中的数据通常用大写的 X 表示，而标签用小写的 y 表示。
# 这是受到了数学标准公式 f(x)=y 的启发，其中 x 是函数的输入，y 是输出。
# 我们用大写的 X 是因为数据是一个二维数组（矩阵），
# 用小写的 y 是因为目标是一个一维数组（向量），这也是数学中的约定。


# 在对数据进行拆分之前，train_test_split 函数利用伪随机数生成器将数据集打乱
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
# 为了确保多次运行同一函数能够得到相同的输出，我们利用 random_state 参数指定了随机
# 数生成器的种子。


# train_test_split 函数的输出为 X_train、X_test、y_train 和 y_test，
# 它们都是 NumPy数组。X_train 包含 75% 的行数据，X_test 包含剩下的 25%：


print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

# 绘制散点图矩阵（pair plot） 以检查数据的好坏

# 训练集中特征的散点图矩阵。数据点的颜色与鸢尾花的品种相对应。
# 为了绘制这张图，我们首先将 NumPy 数组转换成 pandas DataFrame。
# pandas 有一个绘制散点图矩阵的函数，叫作 scatter_matrix。
# 矩阵的对角线是每个特征的直方图：

# 利用X_train中的数据创建DataFrame
# 利用iris_dataset.feature_names中的字符串对数据列进行标记
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# 利用DataFrame创建散点图矩阵，按y_train着色
grr = pd.plotting.scatter_matrix(iris_dataframe,
                                 c=y_train,
                                 figsize=(15, 15),
                                 marker='0',
                                 hist_kwds={'bins': 20},
                                 s=60,
                                 alpha=.8,
                                 cmap=mglearn.cm3)
# pandas.plotting.scatter_matrix
#
# 完整用法：pd.plotting.scatter_matrix(iris_dataframe, c=y_train,
# figsize=(15,15), marker=‘0’, hist_kwds={‘bins’:50},s=60,alpha=.8,
# cmap=mglearn.cm3)
#
# 参数如下：
#
# frame，pandas dataframe对象
# alpha， 图像透明度，一般取(0,1]
# figsize，以英寸为单位的图像大小，一般以元组 (width, height) 形式设置
# ax，可选一般为none
# diagonal，必须且只能在{‘hist’, ‘kde’}中选择1个，’hist’表示直方图
# (Histogram plot),’kde’表示核密度估计(Kernel Density Estimation)；
# 该参数是scatter_matrix函数的关键参数
# marker，Matplotlib可用的标记类型，如’.’，’,’，’o’等
# density_kwds，(other plotting keyword arguments，可选)，与kde相关的字典参数
# hist_kwds，与hist相关的字典参数
# range_padding，(float, 可选)，图像在x轴、y轴原点附近的留白(padding)，该值越大，留白距离越大，图像远离坐标原点
# kwds，与scatter_matrix函数本身相关的字典参数
# c，颜色

# df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
# pd.plotting.scatter_matrix(df, alpha=0.2)

plt.show()

# 构建第一个模型：k近邻算法
# k 近邻算法中 k 的含义是，我们可以考虑训练集中与新数据点最近的任意 k 个邻居（比如
# 说，距离最近的 3 个或 5 个邻居），而不是只考虑最近的那一个。
# 然后，我们可以用这些邻居中数量最多的类别做出预测。

# scikit-learn 中所有的机器学习模型都在各自的类中实现，这些类被称为 Estimator类。
# k 近邻分类算法是在 neighbors 模块的 KNeighborsClassifier 类中实现的。
# 我们需要将这个类实例化为一个对象，然后才能使用这个模型。这时我们需要设置模型的参数。
# NeighborsClassifier 最重要的参数就是邻居的数目，这里我们设为 1：

knn = KNeighborsClassifier(n_neighbors=1)

# knn 对象对算法进行了封装，既包括用训练数据构建模型的算法，也包括对新数据点进行
# 预测的算法。它还包括算法从训练数据中提取的信息。对于 KNeighborsClassifier 来说，
# 里面只保存了训练集。
# 想要基于训练集来构建模型，需要调用 knn 对象的 fit 方法，输入参数为 X_train 和 y_
# train，二者都是 NumPy 数组，前者包含训练数据，后者包含相应的训练标签

knn.fit(X_train, y_train)

# 做出预测

# # 些数据放在一个 NumPy 数组中，再次计算形状，数组形状为样本数（1）乘以特征数（4）
# 注意，我们将这朵花的测量数据转换为二维 NumPy 数组的一行，这是因为 scikit-learn
# 的输入数据必须是二维数组。
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape: {}".format(X_new.shape))

prediction = knn.predict(X_new)
print("Prediction:{}".format(prediction))
print("preicted target name:{}".format(
    iris_dataset['target_names'][prediction]
))

# 评估模型

# 过计算精度（accuracy）来衡量模型的优劣，精度就是品种预
# 测正确的花所占的比例：

y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

# 训练和评估过程所必需的代码
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=2)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))