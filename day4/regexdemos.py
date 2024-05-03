import pandas as pd

data = {
    'product id': ['AB  1234','CD 5678','DE 9001','FG   8765']
}

df = pd.DataFrame(data)
# print(df)

# df['Product Code'] = df['product id'].str.split("\\s+").str[1]
# print(df)

pattern = "(\d{4})"
df['Code'] = df['product id'].str.extract(pattern)

# print(df)

mobile_dt = {
    'phone': ['123 456 7890']
}

df = pd.DataFrame(mobile_dt)
print(df)
pattern = r"(\s)"
replacement = r"-"

df['phone'] = df['phone'].str.replace(pattern,replacement,regex=True)

print(df)