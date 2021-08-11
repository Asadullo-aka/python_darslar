class Bank:
    nomi='Ipoteka'
    __hisobraqam=123456
    def privchiqar(self):
        print(f"hisob raqam \n>>{self.__hisobraqam}")
    def ozgar(self,son):
        self.__hisobraqam=987654
b=Bank()
print(b.nomi)
b.privchiqar()
b.ozgar(int (input('hisob raqami ozgartirng\n>>')))
b.privchiqar()
b._Bank__hisobraqam=55555
b.privchiqar()