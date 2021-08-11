class Bank():
    nomi='Ipak yoli' # public(ochiq)
    __hisobraqami =123456 #private(yopiq)
    def privchiqarish(self):
        print(self.__hisobraqami)
    def privozgarish(self,son):
        self.__hisobraqami=987654
b1=Bank()
print(b1.nomi)
b1.nomi='Ipoteka'
print(b1.nomi)
b1.privchiqarish() 
b1.privozgarish(int(input('hisob raqamni kiritng\n>>')))
b1._Bank__hisobraqami=5555
b1.privchiqarish()  

