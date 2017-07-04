import sys
sys.path.append('../')
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import instacart as ins
from instacart.test import *
from instacart.datareader import *
from instacart.constants import *
from instacart.model import *

import tensorflow as tf

filename = ['../data/order_products__prior_test.csv',
        '../data/order_products__train_test.csv',
        '../data/aisles.csv',  '../data/departments.csv', '../data/orders.csv',
        '../data/products.csv']
#filename = ['../data/order_products__prior.csv', '../data/order_products__train.csv',
#        '../data/aisles.csv',  '../data/departments.csv', '../data/orders.csv',
#        '../data/products.csv']

CONTINUOUS_COLUMNS  = ins.constants.CONTINUOUS_COLUMNS
CATEGORICAL_COLUMNS = ins.constants.CATEGORICAL_COLUMNS
LABEL_COLUMN = "label"

def input_fn(df):
    # Create a dictionary mappint from each continuous feature column name (k)
    # to the values of that column stored in a constant Tensor.
    CONTINUOUS_COLUMNS  = ins.constants.CONTINUOUS_COLUMNS
    CATEGORICAL_COLUMNS = ins.constants.CATEGORICAL_COLUMNS
    continuous_cols = {k: tf.constant(df[k].values) for k in CONTINUOUS_COLUMNS}

    # Create a dictionary mapping from each categorical feature column name (k)
    # to the values of that column stored in a tf.SparseTensor.
    categorical_cols = {k: tf.SparseTensor(indices=[[i,0] for i in
        range(df[k].size)],
        values=df[k].values, dense_shape =
        [df[k].size, 1])
        for k in CATEGORICAL_COLUMNS}

    # Merges the two dictionaries into one.
    #feature_cols = dict(continuous_cols.items() + categorical_cols.items()) #python 2.7
    feature_cols = list(continuous_cols.items()) + list(categorical_cols.items())

    # Converts the label column into a constant Tensor.
    LABEL_COLUMN = "label"
    df[LABEL_COLUMN] = (df["product_id"].apply(lambda x: x>0)).astype(int)
    label = tf.constant(df[LABEL_COLUMN].values)
 
    return feature_cols, label

if __name__=='__main__':
    ins.test.printTest()
    #Read data
    order_products_prior_df, order_products_train_df, order_train_df, order_eval_df = ins.datareader.loadData(filename[0],filename[1],filename[2],filename[3],filename[4],filename[5])

    print (order_products_prior_df.head(5)) 
    print (order_products_train_df.head(5))
    #print (order_train_df.head(5))
    #print (order_eval_df.head(5))
    
    #sess = tf.InteractiveSession()
    #print(sess.run(feature_cols))

    m = instacart.model.build_estimator(model_dir='./', "linearClassifier")
    m.fit(input_fn=lambda: input_fn(order_products_prior_df),steps=200)
    results = m.evaluate(input_fn=lambda: input_fn(order_products_train_df),steps=1)

    for key in sorted(results):
        print("%s: %s" % (key, results[key]))

