__author__ = 'Tamby Kaghdo'

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict, KFold
from sklearn.metrics import roc_auc_score

# open train file
train_df = pd.read_csv("./cleaned_data/train.csv")
# remove row counts
train_df.drop(train_df.columns[0],axis=1,inplace=True)
# print(train_df.head())

features_columns = ["document_id", "topic_id", "topic_confidence_level", "entities_confidence_level", "source_id", "publisher_id", \
                    "category_id", "category_confidence_level", "platform"]

# create Random Forest model
lr = RandomForestClassifier(random_state=1, class_weight="balanced", n_estimators=50,  max_depth=5)
kf = KFold(train_df.shape[0], random_state=1)
predictions = cross_val_predict(lr,train_df[features_columns], train_df["clicked"], cv=kf)
predictions = pd.Series(predictions)


### calculate errors
# false positives
fp_filter = (predictions == 1) & (train_df["clicked"] == 0)
fp = len(predictions[fp_filter])

# true positives
tp_filter = (predictions == 1) & (train_df["clicked"] == 1)
tp = len(predictions[tp_filter])

# false negatives
fn_filter = (predictions == 0) & (train_df["clicked"] == 1)
fn = len(predictions[fn_filter])

# true negatives
tn_filter = (predictions == 0) & (train_df["clicked"] == 0)
tn = len(predictions[tn_filter])

# rates
tpr = float(tp) / float((tp + fn))
fpr = float(fp) / float((fp + tn))
tnr = float(tn) / float((tn + fp))
fnr = float(fn) / float((fn + tp))

auc = roc_auc_score(train_df["clicked"],predictions)

#print("False Positives: {0}".format(fp))
#print("True Positives: {0}".format(tp))
#print("False Negatives: {0}".format(fn))
#print("True Negatives: {0}".format(tn))
print("True Positives Rate: {0}".format(tpr))
print("False Positive Rate: {0}".format(fpr))
print("True Negatives Rate: {0}".format(tnr))
print("False negatives Rate: {0}".format(fnr))
print("AUC: {0}".format(auc))


