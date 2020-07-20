import pandas as pd

# read_csv，读取CSV数据文件
num = pd.read_csv("test.csv")
# print(num)
# print(type(num))
# print(num.dtypes)
# 只需要在这个函数中添加参数即可让数据显示多条
# head = num.head(2)
# print(head)
# 获取到数据表中每一列的列名指标
# print(num.columns)
# 查看矩阵的维度
# print(num.shape)
# 取第一行值
# print(num.loc[0])

## pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
# Series:类似一维数组的对象
# DateFrame:类似多维数组/表格数组；每列数据可以是不同的类型；索引包括列索引和行索引。

# 构建Series,由索引和数据组成（索引在左<自动创建的>，数据在右）。
# ser_obj=pd.Series(range(10))
# print(ser_obj)
# print(type(ser_obj))
# 获取数据和索引
# print(ser_obj.index)
# print(ser_obj.values)
# # 预览数据： ser_obj.head(n);ser_obj.tail(n)
# print(ser_obj.head(3))
# print(ser_obj.tail(3))

# DateFrame 获取列数据：df_obj[col_idx]或df_obj.col_idx
# print(num['1'])
# print(num['3'])
# 其他操作
# print(num)
# num["15"]="5"
# print(num)
# del num["2"]
# print(num)

# print(num.shape)
# print(num.shape[0])
print(num)
print("-----")
print(num[3:-1])