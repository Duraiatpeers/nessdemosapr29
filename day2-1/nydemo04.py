import numpy as np

arr = np.array([2,4,6,8,10,12,14,16,18,20])
# new_arr = arr.copy()
new_arr = arr.view()
print(new_arr[9])

# arr[9] = 200
new_arr[9] = 200
print(arr[9])
print(new_arr[9])




