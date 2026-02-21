
#part 1: RANDOM in NUMPY

"""
Check the difference between radom module and np.random

np.random module allows to generate random numbers from several probability distributions

you can initialize the pseudo-random number generator (PRNG or RNG) with:

rng = np.random.default_rng(42) :42 is just a nerd quote from the movie. any number works. If you dont put a numer then you will have always different result.
If you put a seed rng will give always the same answer.

This is the newer modern version, the older one would be just np.random.unfiform()

By default, with no seed provided, default_rng will seed the RNG from nondeterministic data from the operating system
and therefore generate different numbers each time.

rng.standard_normal(size=None)  : generates an array of N=size random numbers with Gaussian distribution, centered around 0 and with std 1.
size can be:
None --> 1 number
integer
(n,m) --> n*m matrix

if you want more flexibility use
rng.normal(loc=0.0, scale=1.0, size=None)
# loc   = mean (center of the bell curve)
# scale = standard deviation (how spread out it is)
# size  = same as above

rng.integers(low=0, high=10, size=5)  : returns random whole numbers between low (inclusive) and high (exclusive)

"""

import numpy as np 
import matplotlib.pyplot as plt

print(np.random.uniform(0,5,5))  # old version, returns random float numbers between low (inclusive) and high (exclusive) 

rng = np.random.default_rng() #since we want numbers to change all the time we dont use a seed number inside ()

print(rng.uniform(0,10,10))


print(rng.standard_normal(4))   #size 4 

print(rng.standard_normal()) #size 1

print(rng.normal(5,2,4)) #size 4 around 5 with std 1


x = np.arange(400)

plt.plot(x,rng.standard_normal(400))
#plt.show()




# part 2: SLICING ARRAYS AND MEAN,STD,MIN,MAX MANUALLY WITHOUT BUILT-IN FUNCTIONS

size = 1001
arr = np.arange(size)
print(arr[1:5])
arr_5=arr[0:5]
print(len(arr_5))

#with negative numers

arr_last_2 = arr[-2:]
print(arr_last_2)


#MEAN: manual vs numpy built-in

total = 0
for i in range(len(arr)):
    total +=  arr[i] 

total2 = np.sum(arr) # alternatively can use numpy built-in sum 
print(f"Total sum: {total:.1f}")     
man_mean = total / len(arr)
print(f"Manual mean: {man_mean:.1f}")
mean = np.mean(arr)     
print(f"Numpy mean: {mean:.1f}")

#STD: manual vs numpy

summa_2 = 0
for i in range(len(arr)):
    summa_2 += (arr[i] - mean)**2 


std_man = np.sqrt(1/(len(arr)) * summa_2 )

print(f"Manual std: {std_man:.2f}")

print(f"Numpy std: {np.std(arr):.2f}")


#TRY to turn my mean and std into functions

def my_mean(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    mean = total / len(x)
    return mean    

#EVEN CLEANER
def my_mean(x):
    total = 0
    for value in x:
        total += value
    mean = total / len(x)
    return mean    

#for std

def my_std(x):
    total_2 = 0
    mean = my_mean(x) # compute the mean outside the loop for efficiency
    for value in x:
        total_2 += (value - mean)**2
    std = np.sqrt(1/len(x)*total_2) # also std ouside the loop for efficiency
    return std

