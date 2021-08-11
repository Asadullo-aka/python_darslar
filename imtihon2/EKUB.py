#RECURSIVE FUNTION
def EKUB(a,b):
    print("a=",a,"b=",b)
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
    if a==b: # qachonki a va b o'zaro teng bo'lsa ikkalasidan birini qaytaradi 
        return a
    return EKUB(a, b)  # IF SHARTI BAJARILMASA  A VA B  NING YANGI QIYMATLARI YUQORIGA CHIQADI  VA SIKL JARAYONI  IF SHARTI BAJARILMAGUNGA QADAAR DAVOM ETADI AGAR SONLARNING EKUBI O'ZARO TO'G'RI KELMAGAN TAQDIRDA AYIRISH AMALI DAVOM ETIB KETAVERADI TOKI NATIJA 1 GA TENG BOLGUNCHHA
son1=int(input("son1:"))
son2=int(input("son2:"))
ekub=EKUB(son1,son2)
print(" EKUB ({},{})= {}".format(son1,son2,ekub))