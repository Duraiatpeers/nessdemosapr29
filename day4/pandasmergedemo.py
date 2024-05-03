import pandas as pd

df = pd.read_csv('data.csv')
# print(df.dropna())
# print(df.dropna(thresh=1))

new_df = df.fillna({
    'subject1': 9999,
    'subject2': 8888,
    'subject3': 7777
})

print(new_df)