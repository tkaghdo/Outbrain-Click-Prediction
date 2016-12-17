__author__ = 'Tamby Kaghdo'

import pandas as pd
import zipfile


zf = zipfile.ZipFile('./data/clicks_train.csv.zip')
df = pd.read_csv(zf.open('clicks_train.csv'))
print(df.head(10))
