import pandas as pd

df = pd.read_excel('data.xlsx')
new_df = df.groupby('eloc')

print(new_df.get_group('Adelaide'))
# for eloc in new_df:
#     print(eloc)

# df = pd.read_json('data.json')
# print(df['salary'].sum())