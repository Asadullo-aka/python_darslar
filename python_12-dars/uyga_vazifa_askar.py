class Askar:
    def __init__(self,a,b,c,d):
        self.jinsi=a
        self.yoshi=b
        self.vazni=c
        self.boyi=d
    def info(self):
        if self.jinsi=='erkak' and self.yoshi>=18 and self.vazni<75 and self.boyi>165:
            print(f"\n<<Piyoda qoshinlariga qabull qilindingiz>>\n\
                  \n>>Jinsi {self.jinsi} \n>>Yoshi {self.yoshi}\n>>Vazni {self.vazni} \n>>Boyi {self.boyi}")
        
        elif self.jinsi=='erkak' and self.yoshi<18 and self.vazni>75 and self.boyi<165:    
            print(f"\n>>Tank qoshinlariga qabull qilindingiz,\
                  \n>>Jinsi {self.jinsi} \n>>Yoshi {self.yoshi}\n>>Vazni {self.vazni} \n>>Boyi {self.boyi}")
        else:
            print("\n<< siz bizning standartga tori kelmadingiz >>\n")
        
    def __str__(self):
        return "\n<< Vayenkamat >>\n"
class Qoshin(Askar):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
    def info(self):
        super().info()
print("<< Qoshin >>")
Armiya=Qoshin(input("Jinsingizni kiritng\n>>"),int(input("Yoshingizni kiritng\n>>")),int(input("vazningizni kiritng\n>>")),int(input("Boyingizni kirting\n>>")))
Armiya.info()
print("<< Askar >>")
Armiya=Askar(input("Jinsingizni kiritng\n>>"),int(input("Yoshingizni kiritng\n>>")),int(input("vazningizni kiritng\n>>")),int(input("Boyingizni kirting\n>>")))
Armiya.info()
print(Armiya)
