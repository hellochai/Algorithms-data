#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 12:04
# @Author  : fchai
# @Desc    :
# @File    : light_kmeans.py
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


def sum_list(list_data, index):
    sum = 0
    for d in list_data:
        sum += float(d[index])
    return sum


def kmeans_AI(narr: np.ndarray, tenant):
    # print(type(narr))
    narr_new = narr[..., 0:2].astype(float)
    km = KMeans(n_clusters=3)
    clf = km.fit(narr_new)

    centroids = km.cluster_centers_
    y_kmean = km.predict(narr_new)

    # plt.scatter(clf[:, 0], clf[:, 1], s=50, cmap='viridis')
    # plt.show()
    clust_labels = km.labels_
    df = pd.DataFrame(narr)

    df['label'] = clust_labels

    # for i in range(3):
    #     print(">>>>", df[df['label'] == i])

    cluster = {'cluster_one': '', 'cluster_two': '', 'cluster_three': ''}

    list1 = [list(d) for d in df[df['label'] == 0].values]
    list2 = [list(d) for d in df[df['label'] == 1].values]
    list3 = [list(d) for d in df[df['label'] == 2].values]

    list1_sum = sum_list(list1, 0) * 0.2 + sum_list(list1, 1) * 0.8
    list2_sum = sum_list(list2, 0) * 0.2 + sum_list(list2, 1) * 0.8
    list3_sum = sum_list(list3, 0) * 0.2 + sum_list(list3, 1) * 0.8

    list_all = [list1_sum, list2_sum, list3_sum]

    list_all.sort()
    list_class = [0, 1, 2]

    cluster['cluster_one'] = str([list(d) for d in df[df['label'] == 0].values])
    cluster['cluster_two'] = str([list(d) for d in df[df['label'] == 1].values])
    cluster['cluster_three'] = str([list(d) for d in df[df['label'] == 2].values])

    class_value = tuple(zip(list_all, list_class))

    return cluster, class_value
