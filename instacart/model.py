import tensorflow as tf

def build_estimator(model_dir,model_type):
    reorder = tf.contrib.layers.sparse_column_with_keys(column_name="reordered",keys=[0,1])

    user_id = tf.contrib.layers.real_valued_column("user_id")
    order_number = tf.contrib.layers.real_valued_column("order_number")
    order_dow = tf.contrib.layers.real_valued_column("order_dow")
    order_hour_of_day = tf.contrib.layers.real_valued_column("order_hour_of_day")
    days_since_prior_order = tf.contrib.layers.real_valued_column("days_since_prior_order")

    f_columns = [ reorder, user_id, order_number, order_number, order_dow, order_hour_of_day, days_since_prior_order]

    if model_type=="linearClassifier":
        m = tf.contrib.learn.LinearClassifier(model_dir=model_dir, feature_columns=f_columns)
    return m
