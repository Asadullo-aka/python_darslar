#login
def login():
    a=5
    b=0
    while a!=0:
        if b==True:
            break
        else:
            c=input('login kiritn\n>>')
            if c=='Asadullo':
                print("""****** **** *********
                      ** ***** ***** *********
                      *** *** ****** **********
                      **** * *****************
                      ***** ********  ********""")
                while a!=0:
                     d=int(input("parolni kiritng\n>>"))
                     if d==12345:
                         print("""****** **** *********
                               ** ***** ***** *********
                               *** *** ****** **********
                               **** * *****************
                               ***** ********  ********""")
                         b+=1
                         break
                     else:
                         a-=1
                         print(f"xatoo{a}")
            else:
                a-=1
                print(f"xatoo !!{a}")
                
login()
        