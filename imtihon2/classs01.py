class animal():
    name='tiger'
    tipi='yirtqich'
    vazni=1000
    def printf(self):
        print(f" nomi {self.name}\n tipi {self.tipi} \n vazni {self.vazni}\n\n")
    def ozgar(self,a,b,c,):
        self.name=a
        self.tipi=b
        self.vazni=c
t=animal()
t.printf()
t.name='sigir\n'
t.tipi='uyhayvoni\n'
t.vazni=250
t.printf()
t.ozgar('ayiq\n', 'yirtqich\n', 500)
t.printf()
#%%
'''classlarda  2 xil medodlaar boor 
1) foydalanuvchi tomanidan yaratiladiagan metodlar
2) classninig uzini metotdalr'''
class Mashina:
    def __del__ (self):
        print("Malumoatlar  o'chirildi ")
    def __init__(self,model,narx,otkuchi):
        self.a=model
        self.b=narx
        self.c=otkuchi
    def printmashina(self):
        print(f"Mashina turi {self.a}\n Mashina  narxi {self.b}\n Mashina kuchhi {self.c}\n")
A=Mashina("ferrari",'500000',555555555)
A.printmashina()
A.__del__()
        
