import pandas

new_data_set = {

    "model":["i10","i20","i30","i40"],
    "year":[2010,2012,2014,2016]
}

df_data = pandas.DataFrame(new_data_set)

print(df_data)

# print(df_data.loc[0])
# print(df_data.loc[1])

# using index to get the data from the frame
# print(df_data.loc[[0,3]])
print(df_data.loc[[2,3]])
