import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

even_data_array = arr[arr % 2 == 0]
print(even_data_array)

less_than_five_data_array = arr[arr < 5]
print(less_than_five_data_array)

data_arr = np.array([11,2,33,14,51,62,37,48,99,10])

print(np.sort(data_arr))







