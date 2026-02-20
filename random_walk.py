import numpy as np
import matplotlib.pyplot as plt
import random as rnd

test = rnd.random()
print("test random number:", f"{test:.2f}")

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

arr_mean = np.mean(arr)
print("Mean of array:", f"{arr_mean:.2f}")

arr_stf = np.std(arr)
print("Standard deviation of array:", f"{arr_stf:.2f}")

for i in range(len(arr)):
    x_values = np.append(x_values,i)
print(x_values)

plt.plot(x_values, arr)
plt.axhline(y=arr_mean, color='red', linestyle='--', label=f'Mean: {arr_mean:.2f}')
plt.legend()
plt.show()





