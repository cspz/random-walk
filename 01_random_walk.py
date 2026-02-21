import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import pandas as pd


print("="*5+" Initial tests "+"="*6)
# random.random() generates a random float between 0.0 and 1.0 (inclusive)
test = rnd.random()
print("test random number:", f"{test:.2f}")


arr = np.array([])

s = rnd.sample(range(1, 100), 10)
print("Random sample of 10 numbers between 1 and 100:", s)

print("="*20)

print("="*5+" Random walk "+"="*5)

# random.uniform(a,b) generates a random float between a and b (inclusive)
i=0
while i < 1000:
    test = rnd.uniform(-5,5)
    arr = np.append(arr,test)
    i += 1

arr_mean = np.mean(arr)
print("Mean of array:", f"{arr_mean:.2f}")

arr_stf = np.std(arr)
print("Standard deviation of array:", f"{arr_stf:.2f}")

#add x values to plot
len(arr)
x_values = np.arange(len(arr))


# Using pandas to get descriptive statistics of the array
description = pd.DataFrame(arr).describe()
print("Descriptive statistics of the array:")
print(description)



plt.plot(x_values, arr)
plt.axhline(y=arr_mean, color='red', linestyle='--', label=f'Mean: {arr_mean:.2f}')
plt.axvline(x=len(arr)/2, color='black', linestyle='--')
plt.legend()
plt.show()



#test 2 - using a for loop instead of while loop
# and using a list first and then converting to a numpy array at the end
steps = []
for _ in range(1000):
    steps.append(rnd.uniform(-5, 5))

x_values = np.arange(len(steps)) # format of np.arange is np.arange(stop) - generates array from 0 to stop value, or can be more specific using np.arange(start, stop, step)






