import pandas as pd
import requests


user_data = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post('https://reqres.in/api/users',json=user_data)
res_data = response.json()

df = pd.DataFrame = res_data
print(df)