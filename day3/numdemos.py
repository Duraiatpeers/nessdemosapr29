import numpy as np
from numpy import random

# arr = np.array([10,20,30,40])
# #
# # for data in arr:
# #     print(data)
#
# arr = np.array([[10,20,30],[40,50,60]])
#
# for x in arr:
#     for y in x:
#         print(y)
#
#

# arr1 = np.array([[100,200,300],[101,201,301]],dtype='i')
# arr2 = np.array([[400,500,600],[401,501,601]],dtype='i')
#
# new_arr = np.concatenate((arr1,arr2),axis=1)
#
# print(new_arr)


# arr = np.array([6,2,3,4,1,5])
#
# indx = np.where(arr % 2 == 0)
# print(indx)
#
# print(np.sort(arr))
#
# print(arr[arr % 2 == 0])


choice = random.choice([10,10,100,1000],size=(3,5))
# print(choice)

new_data = random.randint(100,size=(2,4))
# print(new_data)

choice = random.choice([10,100,1000,10000],p=[0.1,0.5,0.4,0.0],size=(3,5))
# print(choice)

cities = np.array(["Pune","Mumbai","Hyderabad","Bangalore"])
# random.shuffle(cities)
# print(cities)

new_cities = random.permutation(cities)
print("Old order ",cities)
print("New order ",new_cities)
