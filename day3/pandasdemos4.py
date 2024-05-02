import pandas as pd
import requests

response = requests.get('https://reqres.in/api/users?page=2')
res_data = response.json()
df = pd.DataFrame(res_data["data"])

print(df['email'].head(3))


