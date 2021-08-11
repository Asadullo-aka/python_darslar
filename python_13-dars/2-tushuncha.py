class Korzinka:
    def ozgarish(self,meva,sabzavot):
        self.fruit=meva
        self.vegetable=sabzavot
    def chiqarish(self):
        print("meva",self.fruit)
        print("sabzavot",self.vegetable)
class Macro:
    def ozgarish1(self,kiyim):
        self.kiyim1=kiyim
    def chiqarish1(self):
        print("Kiyim",self.kiyim1)
class Magazin(Korzinka,Macro):
    def __init__(self,meva,sabzavot,kiyim):
        super().ozgarish(meva,sabzavot)
        super().ozgarish1(kiyim)
    def printf(self):
        super().chiqarish()
        super().chiqarish1()
dokon=Magazin("olma","Sabzi","Mayka")
dokon.printf()


