from math import*
print(factorial(10))
import time
time.sleep(0.5)
print("1")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("3")
#%%
import random as r
son=r.random()
print(son)
#%%
import random as r
son=r.randint(1,11)
print(son)
#%%
import random as r
lis=[i for i in range (1,111)]
r.shuffle(lis)
r.choice(lis)
print(lis)
