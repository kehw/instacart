import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import csv


pd.options.mode.chained_assignment = None  # default='warn'

def loadData(prior_data, train_data, aisles, departments, orders, products):
    order_products_prior_df = pd.read_csv(prior_data)
    order_products_train_df = pd.read_csv(train_data)
    aisles_df = pd.read_csv(aisles)
    departments_df = pd.read_csv(departments)
    orders_df = pd.read_csv(orders)
    products_df = pd.read_csv(products)

    order_products_prior_df = pd.merge(order_products_prior_df, products_df, on='product_id', how='left')
    order_products_prior_df = pd.merge(order_products_prior_df, orders_df, on='order_id', how='left')
    order_products_prior_df = pd.merge(order_products_prior_df, aisles_df, on='aisle_id', how='left')
    order_products_prior_df = pd.merge(order_products_prior_df, departments_df, on='department_id',how='left')

    order_products_train_df = pd.merge(order_products_train_df, products_df, on='product_id',how='left')
    order_products_train_df = pd.merge(order_products_train_df, orders_df, on='order_id', how='left')
    order_products_train_df = pd.merge(order_products_train_df, aisles_df, on='aisle_id',how='left')
    order_products_train_df = pd.merge(order_products_train_df, departments_df, on='department_id',how='left')

    order_train_df = orders_df[orders_df['eval_set'].str.contains('train')]

    order_eval_df = orders_df[orders_df['eval_set'].str.contains('test')]

    return order_products_prior_df, order_products_train_df, order_train_df, order_eval_df
