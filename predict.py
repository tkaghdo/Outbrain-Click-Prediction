"""
predict which recommended content each user will click
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict, KFold
from sklearn.metrics import roc_auc_score
import sys
import csv
import understand_outbrain_data as uod

__author__ = 'Tamby Kaghdo'


def predict(classifier):

    if classifier == "random_forest":
        # load files and transform the train and test files
        uod.load_files(load_full_page_views=False)

        try:
            # open train file
            train_df = pd.read_csv("./cleaned_data/train.csv")

        except IOError as e:
            print("ERROR: loading files unsuccessful")
            print(e)
            sys.exit(e.errno)

        # remove row counts
        train_df.drop(train_df.columns[0],axis=1,inplace=True)

        features_columns = ["document_id", "topic_id", "source_id", "publisher_id", \
                            "category_id", "platform"]

        # check model performance using cross validation
        lr = RandomForestClassifier(random_state=1, class_weight="balanced", n_estimators=25, max_depth=6)
        kf = KFold(train_df.shape[0], random_state=1)
        predictions = cross_val_predict(lr,train_df[features_columns], train_df["clicked"], cv=kf)
        predictions = pd.Series(predictions)

        # calculate errors
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

        print("True Positives Rate: {0}".format(tpr))
        print("False Positive Rate: {0}".format(fpr))
        print("True Negatives Rate: {0}".format(tnr))
        print("False negatives Rate: {0}".format(fnr))

        # fit the model
        lr.fit(train_df[features_columns], train_df["clicked"])
        predictions = lr.predict(train_df[features_columns])
        auc = roc_auc_score(train_df["clicked"],predictions)
        print("AUC: {0}".format(auc))

        try:
            # open test file
            test_df = pd.read_csv("./cleaned_data/test.csv")

        except IOError as e:
            print("ERROR: loading files unsuccessful")
            print(e)
            sys.exit(e.errno)

        test_df.drop(test_df.columns[0],axis=1,inplace=True)

        # Use the model to make predictions based on testing data.
        predictions = lr.predict(test_df[features_columns])
        predictions_proba = lr.predict_proba(test_df[features_columns])[:,1]

        test_df["predicted_label"] = predictions
        test_df["predicted_proba"] = predictions_proba

        print("TEST DATA\n")

        # prepare submission file
        drop_columns = ["document_id", "topic_id", "topic_confidence_level", "entities_confidence_level",
                        "source_id", "publisher_id", "category_id", "category_confidence_level", "platform",
                        "traffic_source", "clicked", "geo_location_codes"]

        test_df.drop(drop_columns,axis=1,inplace=True)
        test_df.sort_values(by=["display_id", "ad_id", "predicted_label", "predicted_proba"], ascending=[False, False, False, False], inplace=True)

        test_df.drop(["predicted_label", "predicted_proba"], axis=1, inplace=True)

        test_group_by = test_df.groupby("display_id")["ad_id"].apply(list)

        submission_dict = {}

        # create a dictionary to hold display ids and unique ad ids
        for index, row in test_group_by.iteritems():
            unique_lst = []
            for i in row:
                if i not in unique_lst:
                    unique_lst.append(i)
            submission_dict[index] = unique_lst

        # write to the submission file
        with open("./cleaned_data/submission.csv", "w") as submission_file_handle:
            file_writer = csv.writer(submission_file_handle, delimiter=',', quoting=csv.QUOTE_NONE, quotechar='', lineterminator='\n')
            file_writer.writerow(["display_id","ad_id"])
            for key, value in submission_dict.items():
                ad_id_str = ""
                for i, v in enumerate(value):
                    if i != 0:
                        ad_id_str += " " + str(v)
                    else:
                        ad_id_str += str(v)

                file_writer.writerow([key, ad_id_str])
    elif classifier == "SGD":
        # TODO
        # http://stackoverflow.com/questions/24617356/sklearn-sgdclassifier-partial-fit
        # http://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#sphx-glr-auto-examples-applications-plot-out-of-core-classification-py
        pass
        from sklearn.linear_model import SGDClassifier
        import random
        clf2 = SGDClassifier(loss='log')  # shuffle=True is useless here
        shuffledRange = range(len(X))
        n_iter = 5
        for n in range(n_iter):
            random.shuffle(shuffledRange)
            shuffledX = [X[i] for i in shuffledRange]
            shuffledY = [Y[i] for i in shuffledRange]
            for batch in batches(range(len(shuffledX)), 10000):
                clf2.partial_fit(shuffledX[batch[0]:batch[-1] + 1], shuffledY[batch[0]:batch[-1] + 1],
                                 classes=numpy.unique(Y))


def main():

    # use the transformed train and test to predict and create a submission file
    predict("random_forest")


if __name__ == "__main__":
    sys.exit(0 if main() else 1)