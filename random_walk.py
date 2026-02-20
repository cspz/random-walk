import numpy as np
import matplotlib.pyplot as plt
import random as rnd


test = rnd.random()
print(test)


i =0
arr = np.array([])
print(arr)
while i < 10:
    test = rnd.random()
    print(test)
    arr = np.append(arr,test)
    i += 1
print(arr)

len(arr)
x_values = np.array([])


for i in range(len(arr)):
    x_values = np.append(x_values,i)


print(x_values)

plt.plot(x_values, arr)
plt.show()


