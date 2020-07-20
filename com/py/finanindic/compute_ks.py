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