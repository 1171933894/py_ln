import pandas as pd
import numpy as np

# 实现KS指标统计函数
# 方法一：二分类问题，正样本标记为1，负样本标记为0。里面有用到pandas和numpy库，import语句就不贴了，代码如下
def compute_ks(data):
    sorted_list = data.sort_values(['predict_proba'], ascending=[True])#按照样本为正样本的概率值升序排序 ，也即坏样本的概率从高到低排序
    total_good=sorted_list['label'].sum()
    total_bad = sorted_list.shape[0] - total_good
    max_ks = 0.0
    good_count = 0.0
    bad_count = 0.0
    for index, row in sorted_list.iterrows(): #按照标签和每行拆开
        if row['label'] == 0:
            bad_count +=1
        else:
            good_count +=1
        val = abs(bad_count/total_bad - good_count/total_good)
        max_ks = max(max_ks, val)
    return max_ks

# test_pd=pd.DataFrame()
# y_predict_proba=[.2,.3,.4,.5,.6,.7,.9]#取被分为正样本的概率那一列
# Y_test_1=np.array([0,1,0,1,0,1,0])
# test_pd['label']=Y_test_1
# test_pd['predict_proba']=y_predict_proba
# print(test_pd)
# print ("测试集 KS:",compute_ks(test_pd))

# 方法二：这个方法比较简洁，使用了sklearn的metrics里的函数roc_curve()求出FPR，TPR，然后直接计算max(TPR-FPR)
# y_predict_proba = est.predict_proba(X_test)[:,1]
# fpr,tpr,thresholds= sklearn.metrics.roc_curve(np.array(Y_test),y_predict_proba)
# print ('KS:',max(tpr-fpr))

# 方法三：我们知道计算ks的核心就是好坏人的累积概率分布，我们采用pandas.crosstab函数来计算累积概率分布。
def ks_calc_cross(data,score_col,class_col):
    '''
    功能: 计算KS值，输出对应分割点和累计分布函数曲线图
    输入值:
    data: 二维数组或dataframe，包括模型得分和真实的标签
    score_col: 一维数组或series，代表模型得分（一般为预测正类的概率）
    class_col: 一维数组或series，代表真实的标签（{0,1}或{-1,1}）
    输出值:
    'ks': KS值，'crossdens': 好坏人累积概率分布以及其差值gap
    '''
    ks_dict = {}
    # print("--------")
    # print(data[score_col[0]])
    # print(data[class_col[0]])
    # print("--------")
    crossfreq = pd.crosstab(data[score_col[0]],data[class_col[0]])
    crossdens = crossfreq.cumsum(axis=0) / crossfreq.sum()
    # print("--------")
    # print(crossdens)
    # print("--------")
    crossdens['gap'] = abs(crossdens[0] - crossdens[1])
    ks = crossdens[crossdens['gap'] == crossdens['gap'].max()]
    return ks,crossdens

data_test_1 = {'y30':[1,1,1,1,1,1,0,0,0,0,0,0],'a':[1,2,4,2,2,6,5,3,0,5,4,18]}
data_test_1 = pd.DataFrame(data_test_1)
# print(data_test_1)
ks_cross,cdf_cross=ks_calc_cross(data_test_1,['a'],['y30'])
print(ks_cross)
print("--------")
print(cdf_cross)