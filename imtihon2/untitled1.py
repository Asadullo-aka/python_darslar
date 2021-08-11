with open("salom","w") as fyle:
      fyle.write(input("son aralash maaatn  kritng\>>"))
with open("salom","r") as fyle:
     a=fyle.readlines()
     for i in a:
         for j in i:
             if j.isnumeric():
                  print(j)
                  with open("raqam","a")as fyle1:
                      fyle1.write(j)
