from math import *
print (factorial(5))
print (sin (10))

#%%
import math as mt
print(mt.factorial(5))
#%% time modiule 
import time
time.sleep(3)
print("salom")
#%%BOMBA
import time
time.sleep(1)
print(3)
time.sleep(2)
print(2)
time.sleep(3)
print(1)
print('buuum!!!!!!')
#%% RANDOM MODULE
import random as r
son1=r.random ()
print(son1)

son2=r.randint (10,20)
print(son2)

son3=r.randrange(2,10,3)
print (son3)

list1=[1,2,3,4,5,6,7,8,9,10]
r.shuffle(list1)
print(list1)

son4=r.choice(list1)
print(son4)