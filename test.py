import os
import requests

url='https://data.toulouse-metropole.fr/api/records/1.0/download/?dataset=dechets-menagers-et-assimiles-collectes'
response = requests.get(url)
with open(os.path.join("C:\\folder", "file"), 'wb') as f:
    f.write(response.content)