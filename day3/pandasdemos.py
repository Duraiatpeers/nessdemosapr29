import pandas as pd

df = pd.read_csv('data.csv',index_col=0)

# print(type(df))
# print(df)
# new_df = df.fillna("missed data")
new_df = df.fillna({
    "edesign":"admin1",
    "ename":"Steve"
    })

# print(new_df)
# print(new_df[new_df['eloc']=='hyderabad'])

# print(new_df.head(3))
# print(new_df.tail(3))

# print(new_df[2:5])

# print(new_df.columns)

# print(type(new_df['eid']))

print(new_df[['eid','ename']])