import matplotlib.pyplot as plt
import  numpy as np

# x = np.array([12,5,6,7,9,11,34,12,11,19,21,41])
# y = np.array([2,15,46,77,89,10,4,24,67,99,18,4])
#
# plt.scatter(x,y)
#
# x = np.array([2,4,9,71,91,1,46,18,13,9,15,47])
# y = np.array([32,65,60,77,29,50,4,44,77,79,78,64])
#
# plt.scatter(x,y)

# fifa_winners = np.array(["Brazil","Germany","Argentina","France"])
# no_of_times =  np.array([5,3,3,2])
# plt.bar(fifa_winners,no_of_times)
# plt.xlabel("Countries")
# plt.ylabel("No of Times")
#
# plt.show()


x = np.random.normal(50,10,10)

print(x)
plt.hist(x)

plt.show()

chart_data = np.array([15,5,35,45])
plt.pie(chart_data)
plt.show()