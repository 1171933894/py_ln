# -*- coding: utf-8 -*-
# Matplotlib 是 Python 的绘图库
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc  ###计算roc和auc

train_x = [[0.], [1.], [1.], [0.], [1.]]
train_y = [0., 1., 1., 0., 1.]
test_x = [[1.], [1.], [0.], [1.], [0.]]
test_y = [1., 1., 0., 1., 0.]
print(train_y)
print(test_x)

# Learn to predict each class against the other
svm = svm.SVC(kernel='linear', probability=True)

###通过decision_function()计算得到的y_score的值，用在roc_curve()函数中
model = svm.fit(train_x, train_y)
test_y_score = model.decision_function(test_x)
prediction = model.predict(test_x)
print(test_y_score)
print(prediction)
# Compute ROC curve and ROC area for each class
fpr, tpr, threshold = roc_curve(test_y, test_y_score)  ###计算真正率和假正率
roc_auc = auc(fpr, tpr)  ###计算auc的值
print(fpr)
print(tpr)
# 计算KS值（使用了sklearn的metrics里的函数roc_curve()求出FPR，TPR，然后直接计算max(TPR-FPR)）
print("最佳ks:",max(tpr-fpr))

print(threshold)
lw = 2
plt.figure(figsize=(8, 5))
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()