
a=int ( input ('son kiritng '))
b=a%1000%10
c=a%1000//10%10
d=a%1000//10//10

f=a//1000%10
e=a//1000//10%10
g=a//1000//10//10
print(b,c,d)
print(f,e,g)
q=b+c+d
w=f+e+g
if  q==w:
    print ('ajoyib son')
else :
    print('ajoyib son emas')
#%% 1-usul
a=int (input ('son kiriting'))
if a//100000+a//10000%10+a//1000%10==a%100+a//10%10+a%10:
    print("ajoyib")
else :
    print ('ajoyib emas')
#%% 2-usul
a=input ('6 xonali son kiriting')
if int (a[0])+int (a[1])+int(a[2])== int (a[3])+int (a[4])+int (a[5]):
    print('ajoyib')
else:
    print('ajoyib emas')
    