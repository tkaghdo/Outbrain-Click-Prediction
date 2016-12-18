__author__ = 'Tamby Kaghdo'

################################################################################
# This script is used to understand the basics of the data provided
# the results of this investigation will be recorded in README.MD
################################################################################


import pandas as pd
import zipfile

#clicks_train
zf = zipfile.ZipFile('./data/clicks_train.csv.zip')
df = pd.read_csv(zf.open('clicks_train.csv'))
print("*** CLICKS TRAIN ***")
print(df.head(10))

#clicks_test
zf = zipfile.ZipFile('./data/clicks_test.csv.zip')
df = pd.read_csv(zf.open('clicks_test.csv'))
print("*** CLICKS TEST")
print(df.head(10))

#documents_topics
zf = zipfile.ZipFile('./data/documents_topics.csv.zip')
df = pd.read_csv(zf.open('documents_topics.csv'))
print("*** DOCUMENT TOPICS")
print(df.head(10))

#documents_entities
zf = zipfile.ZipFile('./data/documents_entities.csv.zip')
df = pd.read_csv(zf.open('documents_entities.csv'))
print("*** DOCUMENT ENTITIES")
print(df.head(10))

#documents_meta
zf = zipfile.ZipFile('./data/documents_meta.csv.zip')
df = pd.read_csv(zf.open('documents_meta.csv'))
print("*** DOCUMENT META")
print(df.head(10))

#document_categories
zf = zipfile.ZipFile('./data/documents_categories.csv.zip')
df = pd.read_csv(zf.open('documents_categories.csv'))
print("*** DOCUMENT CATEGORIES")
print(df.head(10))

#events
zf = zipfile.ZipFile('./data/events.csv.zip')
df = pd.read_csv(zf.open('events.csv'))
print("*** EVENTS")
print(df.head(10))

#promoted content
zf = zipfile.ZipFile('./data/promoted_content.csv.zip')
df = pd.read_csv(zf.open('promoted_content.csv'))
print("*** PROMOTED CONTENT")
print(df.head(10))

#page_views_sample
zf = zipfile.ZipFile('./data/page_views_sample.csv.zip')
df = pd.read_csv(zf.open('page_views_sample.csv'))
print("*** PAGE VIEWS SAMPLE")
print(df.head(10))

#sample_submission
zf = zipfile.ZipFile('./data/sample_submission.csv.zip')
df = pd.read_csv(zf.open('sample_submission.csv'))
print("*** SAMPLE SUBMISSION")
print(df.head(10))


