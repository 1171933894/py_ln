import pandas as pd
import numpy as np

## 癌症病名模型建立并评估
## https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

# 1、读取数据
path="https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
column_name=["Sample code number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape","Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class"]
data=pd.read_csv(path,names=column_name)
# print(data)
# print(data.head())
# print(type(data))
# 2、缺失值处理
# 1）替换：?->np.nan
data.replace(to_replace='?',value=np.nan,inplace=True)
# 2) 删除缺少样本
data.dropna(inplace=True)
#print(data.isnull().any()) # 查看是否有缺失值
# 3、划分数据集
from sklearn.model_selection import train_test_split
# 筛选特征值和目标值
x = data.iloc[:,1:-1]
y = data["Class"]
# print(x)
# print(y)
# x ：所要划分的样本特征集; y ：所要划分的样本结果
x_train,x_test,y_train,y_test=train_test_split(x,y)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)
# 4、标准化（特征工程）
from sklearn.preprocessing import StandardScaler
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# print(x_test)
# print(x_train)
 # 5、逻辑回归预估器
from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression()
estimator.fit(x_train,y_train)
# 逻辑回归的模型参数：回归系数和偏置
print(estimator.coef_)# 回归系数
print(estimator.intercept_)# 偏置
y_predict = estimator.predict(x_test)
# 6、模型评估
# 1）方法一：直接比对真实值和预估值
# print("y_predict:\n", y_predict)
# print("直接比对真实值和预测值：\n", y_test==y_predict)
# 2）方法二：
# score = estimator.score(x_test,y_test)
# print("准确率为：\n", score)
# print(y_test)
# print(y_test)
# 3）查看精确率、召回率、F1-score
# from sklearn.metrics import classification_report
# report = classification_report(y_test,y_predict,labels=[2,4],target_names=["良性","恶性"])
# print(report)
# 4）ROC/AUC指标
y_true=np.where(y_test>3,1,0)
# print(y_true)
print(y_predict)
from sklearn.metrics import roc_auc_score
# 计算ROC曲线面积，即AUC值：
# 1）y_true：每个样本的真实类别
# 2）y_score：预测得分，可以是正类的估计概率、置信值或者分类器方法的返回值
# 注意：AUC只能用来评价二分类，且非常适合评价样本不平衡中的分类器性能
auc=roc_auc_score(y_true,y_predict)
print("AUC指标",auc)