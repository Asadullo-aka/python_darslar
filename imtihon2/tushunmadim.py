b=input()
a=input()
c=a
d=int(a)
print(a,end="")
for i in range (len(b)-1):
    a=a+c
    d=d+int(a)
    print("+{}".format(a),end="")
print("={}".format(d))