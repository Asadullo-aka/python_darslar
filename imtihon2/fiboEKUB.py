'''def salomber():
    return "salom"
#salomber()
def main():
    print(salomber())
    hayirlashish()
def hayirlashish():
    print("Hayr")
a=salomber()
print(a,type(a))'''
'''def f (ism,fam,yosh=30):
    print(f">>Ismi {ism}\n>>Familyasi {fam}\n>>Yosh {yosh}")
f("Abror ","Abrorov")
f(None,None,15)
def f1 (ism="Kimdir",fam="Kimdirov",yosh="ancha"):
    print(f">> Ismi {ism} \n>> Familyasi {fam} \n>> Yoshi {yosh}")
f1()
f1(input("Ismi \n>>"),input("familayasi\n>>"), int(input("yoshi \n>>")))'''
'''def ekub(a,b):
    print("a=",a,"b=",b)
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
    if a==b:
        return a
    return  ekub(a, b)
son=int(input("son1: "))
son1=int(input("son2: "))
EKUB=ekub(son,son1)
print("EKUB({},{}={})".format(son,son1,EKUB))'''
def fib(n):
    if n== 1 or n==2:
        return 1
    elif n>2:
        return fib (n-1)+fib (n-2)
def fib1(n):
    f1=1
    f2=1
    for i in range(3,n+1):
        print("f1=",f1,"f2=",f2)
        f1,f2=f2,f1+f2
    print(n,"chi fibonachi soni >> ",f2)
son=int(input("son: "))
print(son,"chi fibonachi son >> ",fib(son))
fib1(int (input("n\n>>")))













    
    






