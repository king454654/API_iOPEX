import pandas as pd
import numpy as np
import requests


# li=['users','posts','posts','comments','albums','photos','todos']
# for i in li:
#     response=requests.get(f'https://jsonplaceholder.typicode.com/{i}')
#     file = response.json()
#     df = pd.DataFrame(file)

response=requests.get(f'https://jsonplaceholder.typicode.com/users')
file = response.json()

# df = pd.DataFrame(file)