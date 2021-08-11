class oquvchi():
    def __init__(self,ism,fam,yosh):
        self.name=ism
        self.surname=fam
        self.age=yosh
    def info(self):
        print("""
    Name: {}
    Surname: {}
    Age: {}""".format(self.name,self.surname,self.age))
class oqituvchi(oquvchi):
    def __init__(self, ism, fam, yosh,maosh):
        super().__init__(ism, fam, yosh)
        self.price=maosh
    def info(self):
        super().info()
        print('  price: ',self.price)
ustoz=oqituvchi('ism','fam','yosh','maosh')
ustoz.info()
ob=oquvchi('asadullo', 'anvar', 45)
ob.info()