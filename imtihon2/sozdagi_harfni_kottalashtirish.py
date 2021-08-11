def numb(soz,harf):
    for i in range (len(soz)):
        if soz[i]==harf:
            print(soz[i].upper(),end="")
        else:
            print(soz[i],end="")
numb(input("soz kiriting\n>>"),input("harf kiriting\n>>"))
"""foydalanuvchi soz va harf kiritadi agar kritilgan harf sozda bolsa osha harf kottalalshtirib breadai Masaalan salomlar  ni sAlomlAr ga aylantirish mumkin"""
