#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 11:56
# @Author  : fchai
# @Desc    :
# @File    : get_data.py

'''
从
'''
from about_mysql import Mysql
from light_kmeans import kmeans_AI
import numpy as np

conn = Mysql().connect()


def select_light_data():
    cur = conn.cursor()
    try:
        sql_select = '''select * from dhlk_light_vi'''
        cur.execute(sql_select)
        result = cur.fetchall()

        tenant_data = {}
        for d in result:
            if d[3] not in tenant_data:
                tenant_data[d[3]] = [list(d)]
            else:
                tenant_data[d[3]].append(list(d))
        for tenant in list(tenant_data.keys()):
            print("===========", tenant)
            cluster, class_value = kmeans_AI(np.asarray(tenant_data[tenant]), tenant)
            save_res_to_mysql(cluster, tenant, class_value)

    except Exception as e:
        cur.close()


def save_res_to_mysql(cluster, tenant, class_value):
    cur = conn.cursor()
    try:
        sql_select = '''select factoryCode from dhlk_light_cluster where factoryCode="%s"''' % tenant
        cur.execute(sql_select)
        result = cur.fetchall()
        if result:
            sql_update = '''update dhlk_light_cluster set cluster_one="%s",cluster_two="%s",cluster_three="%s", cluster_value="%s" where factoryCode="%s"''' % (
                cluster['cluster_one'], cluster['cluster_two'], cluster['cluster_three'], class_value, tenant)
            # print(sql_update)
            sql_update = sql_update.replace("'", "")
            cur.execute(sql_update)
            conn.commit()
        else:
            sql = '''insert into dhlk_light_cluster (cluster_one, cluster_two, cluster_three, factoryCode, cluster_value) values ("%s","%s","%s", "%s", "%s")''' % (
                cluster['cluster_one'], cluster['cluster_two'], cluster['cluster_three'], tenant, class_value)
            sql = sql.replace("'", "")
            cur.execute(sql)
            conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        cur.close()


