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

