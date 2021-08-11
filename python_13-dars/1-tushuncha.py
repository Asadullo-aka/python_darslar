class first:
    a=10
    b='salom'
class second(first):
    c=True
class third(first):
    d=3.14
ob1=third()
print(ob1.a,ob1.b,ob1.d)
ob2=second()
print(ob2.a,ob2.b,ob2.c)
#%%
class first:
    a=10
class second:
    b='Hello'
class third(first,second):
    d=3.24
ob1=third()
print(ob1.a,ob1.b,ob1.d)
    
