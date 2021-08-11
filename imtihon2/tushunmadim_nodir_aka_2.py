
from random import shuffle
from math import factorial
m=0
a=[int(x) for x in input().split()]
b=a
s=[]
while factorial(len(a))!=m:
   shuffle(b)
   if b not in a:
       s.append(b)
       m+=1
       b=a
print(s)