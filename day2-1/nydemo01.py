import numpy as np

arr = np.array([2,4,6,8,10])
print(arr)
# print(type(arr))

arr = np.array(
    [
        [1,3,5],
        [2,4,6]
    ])
print(arr)
print(arr.ndim)

arr = np.array(
       [
         [
           [1,3,5],
           [2,4,6]
         ],
         [
           [10,30,50],
           [20,40,60]
         ],
       ]
    )
print(arr)
print(arr.ndim)