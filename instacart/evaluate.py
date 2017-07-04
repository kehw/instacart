import sklearn as sk

def predict(estimator, tests):
    results = estimator.evaluate(input_fn = tests) 
    return results

def evaluate(pred,correct_pred,accuracy):
    f1_score = sk.metrics.f1_score(y_true, y_pred)
    precision = sk.metrics.precision_score(y_true, y_pred)
    recall = sk.metrics.recall_score(y_true, y_pred)
    return f1_score, precision, recall
