# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1

#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
import random as rnd
import numpy as np
import matplotlib.pyplot as plt



# %%
test = rnd.random()
print(test)

# %%
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

# %%
