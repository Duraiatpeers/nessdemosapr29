import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from numpy import random

# sb.distplot([10,20,30,40,50], hist= False)

# sb.distplot(random.normal(size=1000),hist=False)

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

# plt.plot(x,y)
plt.subplot(2,1,1)

plt.plot(x,y,marker='d',linestyle='dashed')

plt.xlabel("Hours")
plt.ylabel("Miles")

# plt.grid(axis='y')

x = np.array([11,22,33,44,54])
y = np.array([20,40,60,80,100])

# plt.plot(x,y)
plt.subplot(2,1,2)

plt.plot(x,y,marker='o',linestyle='dotted')
plt.xlabel("Hours")
plt.ylabel("Miles")

plt.show()


