#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 10:01
# @Author  : fchai
# @Desc    : 灯数据的聚类
# @File    : km_light.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd

# data, target = make_blobs(n_samples=100, n_features=2, centers=3)
# # 在2d图中绘制样本，每个样本颜色不通
# plt.scatter(data[:,0], data[:, 1], c=target)
# plt.show()

file = np.loadtxt("F:\Demo\PythonTest\pythonTest\Algorithms-data\part-00000-4aa0b4b6-a2ca-47ff-a697-d49fc925aba8-c000.csv",
           dtype=np.float, comments=',')


df_features = pd.read_csv(r'F:\Demo\PythonTest\pythonTest\Algorithms-data\part-00000-4aa0b4b6-a2ca-47ff-a697-d49fc925aba8-c000.csv') # 读入数据

print(df_features)

# km = KMeans(n_clusters=3)
# y_pre = km.fit(file)

# plt.scatter(file[:, 0],file[:,1], c=y_pre)
# print(km.labels_)
# plt.show()

# from sklearn.metrics import calinski_harabasz_score
# print(calinski_harabasz_score(file, y_pre))
SSE = []

for i in range(1, 9):
    estimator = KMeans(n_clusters=i)
    # estimator.fit(df_features)
    estimator.fit(file)
    SSE.append(estimator.inertia_) # estimator.inertia_获取聚类准则的总和

X = range(1, 9)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, 'o-')
plt.show()




