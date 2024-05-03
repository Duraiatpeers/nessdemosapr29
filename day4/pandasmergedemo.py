import pandas as pd

df1 = pd.DataFrame({
    "city": ['pune','mumbai'],
    "temperature":[98,99]
})

df2 = pd.DataFrame({
    "city": ['bangalore','mumbai'],
    "state":["KA","MR"]
})

df = pd.merge(df1,df2,on='city',how="outer")
print(df)

df = pd.Series([10,20,30])
print(df)
