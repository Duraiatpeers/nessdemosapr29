import numpy as np

arr = np.array([2,4,6,8,10])
# print(arr[0])

# for x in arr:
#     print(x)

arr = np.array(
    [
        [1,3,5],
        [2,4,6]
    ])

print(arr[0,2])


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

print('3 dim array data - ',arr[0,0,2])
print('3 dim array data - ',arr[0,1,2])
print('3 dim array data - ',arr[1,0,2])
print('3 dim array data - ',arr[1,1,2])
print('3 dim array data - ',arr[1,1,-1])