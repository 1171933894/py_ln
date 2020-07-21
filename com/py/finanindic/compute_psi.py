# Python代码实现PSI群体稳定指数
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

def cal_psi(actual, predict, bins=10):
    """
    功能: 计算PSI值，并输出实际和预期占比分布曲线
    :param actual: Array或series，代表真实数据，如训练集模型得分
    :param predict: Array或series，代表预期数据，如测试集模型得分
    :param bins: 分段数
    :return:
        psi: float，PSI值
        psi_df:DataFrame

    Examples
    -----------------------------------------------------------------
    # >>> import random
    # >>> act = np.array([random.random() for _ in range(5000000)])
    # >>> pct = np.array([random.random() for _ in range(500000)])
    # >>> psi, psi_df = cal_psi(act,pct)
    # >>> psi
    1.65652278590053e-05
    # >>> psi_df
       actual  predict  actual_rate  predict_rate           psi
    0  498285    49612     0.099657      0.099226  1.869778e-06
    1  500639    50213     0.100128      0.100428  8.975056e-07
    2  504335    50679     0.100867      0.101360  2.401777e-06
    3  493872    49376     0.098775      0.098754  4.296694e-09
    4  500719    49710     0.100144      0.099422  5.224199e-06
    5  504588    50691     0.100918      0.101384  2.148699e-06
    6  499988    50044     0.099998      0.100090  8.497110e-08
    7  496196    49548     0.099239      0.099098  2.016157e-07
    8  498963    50107     0.099793      0.100216  1.790906e-06
    9  502415    50020     0.100483      0.100042  1.941479e-06

    """
    actual_min = actual.min()  # 实际中的最小概率
    actual_max = actual.max()  # 实际中的最大概率
    binlen = (actual_max - actual_min) / bins
    cuts = [actual_min + i * binlen for i in range(1, bins)]  # 设定分组
    cuts.insert(0, -float("inf"))
    cuts.append(float("inf"))
    actual_cuts = np.histogram(actual, bins=cuts)  # 将actual等宽分箱
    predict_cuts = np.histogram(predict, bins=cuts)  # 将predict按actual的分组等宽分箱
    actual_df = pd.DataFrame(actual_cuts[0], columns=['actual'])
    predict_df = pd.DataFrame(predict_cuts[0], columns=['predict'])
    psi_df = pd.merge(actual_df, predict_df, right_index=True, left_index=True)
    psi_df['actual_rate'] = (psi_df['actual'] + 1) / psi_df['actual'].sum()  # 计算占比，分子加1，防止计算PSI时分子分母为0
    psi_df['predict_rate'] = (psi_df['predict'] + 1) / psi_df['predict'].sum()
    psi_df['psi'] = (psi_df['actual_rate'] - psi_df['predict_rate']) * np.log(
        psi_df['actual_rate'] / psi_df['predict_rate'])
    psi = psi_df['psi'].sum()
    return psi, psi_df

# import random
# act = np.array([random.random() for _ in range(5000000)])
# pct = np.array([random.random() for _ in range(500000)])
# psi, psi_df = cal_psi(act,pct)
# print(psi)
# print(psi_df)

def psi_calc(actual,predict,bins=10):
    '''
    功能: 计算PSI值，并输出实际和预期占比分布曲线
    输入值:
    actual: 一维数组或series，代表训练集模型得分
    predict: 一维数组或series，代表测试集模型得分
    bins: 违约率段划分个数
    输出值:
    字典，键值关系为{'psi': PSI值，'psi_fig': 实际和预期占比分布曲线}
    '''
    psi_dict = {}
    actual = np.sort(actual)
    predict = np.sort(predict)
    actual_len = len(actual)
    predict_len = len(predict)
    psi_cut = []
    actual_bins = []
    predict_bins = []
    actual_min = actual.min()
    actual_max = actual.max()
    cuts = []
    binlen = (actual_max-actual_min) / bins
    for i in range(1, bins):
        cuts.append(actual_min+i*binlen)
    for i in range(1, (bins+1)):
        if i == 1:
            lowercut = float('-Inf')
            uppercut = cuts[i-1]
        elif i == bins:
            lowercut = cuts[i-2]
            uppercut = float('Inf')
        else:
            lowercut = cuts[i-2]
            uppercut = cuts[i-1]
        actual_cnt = ((actual >= lowercut) & (actual < uppercut)).sum()+1
        predict_cnt = ((predict >= lowercut) & (predict < uppercut)).sum()+1
        actual_pct = (actual_cnt+0.0) / actual_len
        predict_pct = (predict_cnt+0.0) / predict_len
        psi_cut.append((actual_pct-predict_pct) * math.log(actual_pct/predict_pct))
        actual_bins.append(actual_pct)
        predict_bins.append(predict_pct)
    psi = sum(psi_cut)
    nbins = len(actual_bins)
    xlab = np.arange(1, nbins+1)
    fig = plt.figure()
    plt.plot(xlab, np.array(actual_bins),'r',label='actual')
    plt.plot(xlab, np.array(predict_bins),'b',label='predict')
    plt.legend(loc='best')
    plt.title('Psi Curve')
    plt.show()
    # plt.close()
    psi_dict['psi'] = psi
    psi_dict['psi_fig'] = fig
    return psi_dict


import random
act = np.array([random.random() for _ in range(5000000)])
pct = np.array([random.random() for _ in range(500000)])
psi_dict = psi_calc(act,pct)
print(psi_dict)