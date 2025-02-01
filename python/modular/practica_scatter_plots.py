from numpy import random, linspace
import matplotlib
import matplotlib.pyplot as plt
x,y=random.rand(2,100)
x2,y2=random.rand(2,100)
plt.scatter(x,y,c="blue")
plt.scatter(x2,y2,c="red")
plt.show()
data=[1,1.1,1.8,2,2.1,3.2,3,3,3,3]
plt.subplot(2,1,1)
plt.hist(data, bins=5, rwidth=0.8)
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()