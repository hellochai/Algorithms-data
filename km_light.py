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
from db.about_mysql import Mysql

file_path = "F:\Demo\PythonTest\pythonTest\DataAnalysis\part-00000-f6600f83-48d3-4d8e-954f-514cebfb7709-c000.csv"

file = np.loadtxt(
    open(r"F:\Demo\PythonTest\pythonTest\Algorithms-data\part-00000-03bef20f-d377-4232-a43a-90e9c6726b5a-c000.csv",
         "rb", ), dtype=str,
    delimiter=",")
# df_features = pd.DataFrame(pd.read_csv(r'F:\Demo\PythonTest\pythonTest\DataAnalysis\part-00000-f6600f83-48d3-4d8e-954f-514cebfb7709-c000.csv')) # 读入数据


file_d = file[..., 0:2]
file_d = file_d.astype(float)

print('-----', file_d)

km = KMeans(n_clusters=3)
clf = km.fit(file_d)

# km.fit_predict(file)


centroids = km.cluster_centers_

y_kmean = km.predict(file_d)

plt.show()

plt.scatter(file_d[:, 0], file_d[:, 1], s=50, cmap='viridis')
# plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=100, alpha=0.5)
plt.show()

clust_labels = km.labels_
df = pd.DataFrame(file)

cluster = {'cluster_one': '', 'cluster_two': '', 'cluster_three': ''}

df['label'] = clust_labels
for i in range(3):
    print(">>>>", df[df['label'] == i])

list1 = [list(d) for d in df[df['label'] == 0].values]
list2 = [list(d) for d in df[df['label'] == 1].values]
list3 = [list(d) for d in df[df['label'] == 2].values]


def sum_list(list_data, index):
    sum = 0
    for d in list_data:
        sum += float(d[index])
    return sum


list1_sum = sum_list(list1, 0) * 0.2 + sum_list(list1, 1) * 0.8
list2_sum = sum_list(list2, 0) * 0.2 + sum_list(list2, 1) * 0.8
list3_sum = sum_list(list3, 0) * 0.2 + sum_list(list3, 1) * 0.8

list_all = [list1_sum, list2_sum, list3_sum]
list_all.sort()

print(list_all, {'0': list1_sum, '1': list2_sum, '2': list3_sum})

cluster['cluster_one'] = str([list(d) for d in df[df['label'] == 0].values])
cluster['cluster_two'] = str([list(d) for d in df[df['label'] == 1].values])
cluster['cluster_three'] = str([list(d) for d in df[df['label'] == 2].values])

conn = Mysql().connect()
cur = conn.cursor()

# print("----->>>>>>>", cluster)




sql = '''insert into light_cluster (cluster_one, cluster_two, cluster_three) values ("%s","%s","%s")''' % (
    cluster['cluster_one'], cluster['cluster_two'], cluster['cluster_three'])

# print(sql)
# cur.execute(sql)
# cur.fetchall()


# print(sql)
# cur.execute(sql)
# cur.fetchall()


# # from sklearn.metrics import calinski_harabasz_score
# # print(calinski_harabasz_score(file, y_pre))
# SSE = []
#
#     estimator = KMeans(n_clusters=i)
#     # estimator.fit(df_features)
#     estimator.fit(file)
#     SSE.append(estimator.inertia_)  # estimator.inertia_获取聚类准则的总和
#
# X = range(1, 9)
# plt.xlabel('k')
# plt.ylabel('SSE')
# plt.plot(X, SSE, 'o-')
# plt.show()

# for i in range(1, 9):
