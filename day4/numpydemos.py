import pandas as pd

ts = pd.Timestamp(year=2024,month=5,day=3,hour=11, minute=10, second=10)

print(type(ts))

print(ts.day_name())
print(ts.dayofweek)
print(ts.year)

this_week = pd.date_range(ts, periods=7)
print(this_week)


df = pd.read_csv('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/server_util.csv')
# print(df.head(5))
# print(df.info())

df['datetime'] = pd.to_datetime(df['datetime'])
# print(df.head(5))
# print(df.info())
#
# print(df['datetime'].min())
# print(df['datetime'].max())

# filter = (df['datetime'] < pd.Timestamp('2019-04-06'))
# print(df.loc[filter])

# print(df.between_time())