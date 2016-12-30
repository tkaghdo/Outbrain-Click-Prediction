__author__ = 'Tamby Kaghdo'

################################################################################
# This script is used to understand the basics of the data provided
# the results of this investigation will be recorded in README.MD
################################################################################


import pandas as pd
import zipfile


#clicks_train
zf = zipfile.ZipFile('./data/clicks_train.csv.zip')
clicks_train_df = pd.read_csv(zf.open('clicks_train.csv'))

#clicks_test
zf = zipfile.ZipFile('./data/clicks_test.csv.zip')
clicks_test_df = pd.read_csv(zf.open('clicks_test.csv'))

#documents_topics
zf = zipfile.ZipFile('./data/documents_topics.csv.zip')
documents_topics_df = pd.read_csv(zf.open('documents_topics.csv'))

#documents_entities
zf = zipfile.ZipFile('./data/documents_entities.csv.zip')
documents_entities_df = pd.read_csv(zf.open('documents_entities.csv'))

#documents_meta
zf = zipfile.ZipFile('./data/documents_meta.csv.zip')
documents_meta_df = pd.read_csv(zf.open('documents_meta.csv'))

#document_categories
zf = zipfile.ZipFile('./data/documents_categories.csv.zip')
documents_categories_df = pd.read_csv(zf.open('documents_categories.csv'))

#page_views_sample
zf = zipfile.ZipFile('./data/page_views_sample.csv.zip')
page_views_sample_df = pd.read_csv(zf.open('page_views_sample.csv'))

#events
zf = zipfile.ZipFile('./data/events.csv.zip')
events_df = pd.read_csv(zf.open('events.csv'))
# cleanup by removing all rows that that have "\N" as platform. There were only 5
events_df = events_df[events_df["platform"] != "\\N"]

#promoted content
zf = zipfile.ZipFile('./data/promoted_content.csv.zip')
promoted_content_df = pd.read_csv(zf.open('promoted_content.csv'))
'''
#sample_submission
zf = zipfile.ZipFile('./data/sample_submission.csv.zip')
sample_submission_df = pd.read_csv(zf.open('sample_submission.csv'))
'''
# join documents_topics and documents_entities by document_id
by_document_id_df = documents_topics_df.merge(documents_entities_df, left_on='document_id', right_on='document_id', how='inner')
by_document_id_df.rename(columns={'confidence_level_x': 'topic_confidence_level', 'confidence_level_y': 'entities_confidence_level'}, inplace=True)

#join by_document_id_df with documents_meta_df by document_id
by_document_id_df = by_document_id_df.merge(documents_meta_df, left_on="document_id", right_on="document_id", how="inner")

# join by_document_id_df with documents_catgories_df by document_id
by_document_id_df = by_document_id_df.merge(documents_categories_df, left_on="document_id", right_on="document_id", how="inner")
by_document_id_df.rename(columns={'confidence_level': 'category_confidence_level'}, inplace=True)

# join page_views_sample with events by uuid, document_id, timestamp, platform, geo_location
join_columns = ["uuid", "document_id", "timestamp", "platform", "geo_location"]
page_views_sample_events_df = page_views_sample_df.merge(events_df, left_on=join_columns, right_on=join_columns, how="inner")


# join by_document_id_df with page_views_sample_events_df by document_id
by_document_id_with_page_views_sample_events_df = by_document_id_df.merge(page_views_sample_events_df, left_on="document_id", right_on="document_id", how="inner")

# join by_document_id_with_page_views_sample_events_df with promoted_content_df by display_id
pre_final_sample_df = by_document_id_with_page_views_sample_events_df.merge(promoted_content_df \
                                                                        , left_on="document_id", right_on="document_id", how="inner")
print(clicks_train_df.head())
print("********")
print(pre_final_sample_df.head())
#join above with clicks_train_df by
#train_df = pre_final_sample_df.merge(clicks_train_df, left_on=["display_id", "ad_id"], right_on=["display_id", "ad_id"], how="inner")
#print(len(train_df))
#print(train_df.head())
#print(train_df.columns.values)




