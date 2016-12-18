# Outbrain-Click-Prediction
Kaggle competition to predict which recommended content each user will click.

[Competition link](https://www.kaggle.com/c/outbrain-click-prediction)

# Data
clicks_train.csv

* display_id: content recommendations served to a specific user

* ad_id: displayed advertisement id

* clicked: a flag that indicated if the ad (represented by ad_id) was clicked or not (1 for clicked, 0 for not clicked)

sample output

|display_id   |ad_id    |clicked|
| ----------  | ------- | ------|
|           1  |42337   |      0|
|           1  |139684  |      0|
|           1  |144739  |      1|
|           1  |156824  |      0|
|           1  |279295  |      0|
|           1  |296965  |      0|
|           2  |125211  |      0|
|           2  |156535  |      0|
|           2  |169564  |      0|
|           2  |308455  |      1|


clicks_test.csv

* display_id: content recommendations served to a specific user

* ad_id: displayed advertisement id

sample output

|display_id   |ad_id|
|-------------|-----|
|    16874594  |66758
|    16874594  |150083
|    16874594  |162754
|    16874594  |170392
|    16874594  |172888
|    16874594  |180797
|    16874595  |  8846
|    16874595  |30609
|    16874595  |143982
|    16874596  | 11430


documents_topics.csv

* document_id: html page that contains the all the content including Outbrains's promoted content
* topic_id: the topic type covered in the document
* confidence_level: confidence that the given topic was referred to in the document

sample output

|document_id  |topic_id  |confidence_level|
|-------------|----------|----------------|
|      1595802|       140|          0.073113
1      1595802|        16|          0.059416
2      1595802|       143|          0.045421
3      1595802|       170|          0.038867
4      1524246|       113|          0.196450
5      1524246|       260|          0.142878
6      1524246|        92|          0.033159
7      1524246|       168|          0.014090
8      1524246|        54|          0.008782
9      1524246|       207|          0.008282


document_entities.csv

sample output

|   document_id|                         entity_id|  confidence_level|
|--------------|----------------------------------|------------------|
|      1524246 | f9eec25663db4cd83183f5c805186f16 |         0.672865
|      1524246 | 55ebcfbdaff1d6f60b3907151f38527a |         0.399114
|      1524246 | 839907a972930b17b125eb0247898412 |         0.392096
|      1524246 | 04d8f9a1ad48f126d5806a9236872604 |         0.213996
|      1617787 | 612a1d17685a498aff4f036c1ee02c16 |         0.386193
|      1617787 | fb8c6cb0879e0de876298177eb1d3fcc |         0.364116
|      1617787 | 793c6a6cf386edb820600d49df045475 |         0.349168
|      1617787 | b525b84d5ed52a34565b8fb870555abe |         0.287005
|      1617787 | 758cb9cb3014607cb4a691cbd485cc94 |         0.237957
|      1617787 | d523aaba6d3916f8b7039fcce0f29639 |         0.235799