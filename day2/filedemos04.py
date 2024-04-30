import xlrd

data_list = []

# open the workbook
data_file = xlrd.open_workbook("data.xls")

# access the sheet using index
sheet = data_file.sheet_by_index(0)

# iterate through each row and store the data in the data list
for row in range(0, sheet.nrows):
    row_values = sheet.row_values(row, 0, sheet.ncols)
    print(row_values)
    data_list.append(row_values)

print(data_list)
