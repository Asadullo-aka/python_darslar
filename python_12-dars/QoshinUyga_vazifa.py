class Askar:
    def __init__(self,a,b,c,d):
        self.jinsi=a
        self.yoshi=b
        self.boyi=c
        self.vazn=d
    def info(self):
        if self.jinsi=='erkak' and self.yoshi>=18 and self.boyi<150 and self.vazn<75:
            print( f"\n>>Piyoda askarlariga qabul qilindingiz,\
            \n>>Jinsi {self.jinsi}\n>>Yoshi {self.yoshi} \n>>Boyi {self.boyi} \n>>Vazni {self.vazn}")
        elif self.jinsi=='erkak' and self.yoshi<18 and self.boyi>150 and self.vazn>75:
            print(f"\n>>Tank qoshinlariga qabul qilindiingiz,\
            \n>>Jinsi{self.jinsi}\n>> Yoshi {self.yoshi} \n>>Boyi {self.boyi} \n>>Vazni {self.vazn}")
        else:
            print("\n<<sizning kirishigiz taqiqlandi !!!!>>\n")
    def __str__(self):
        return "\n<<Men akar qabul kilaman>>\n"
class Qoshin(Askar):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
    def info(self):
        super().info()
Armiya=Qoshin(input("jinsingizni kiitng\n>>"),int(input("yoshingizni kiritng\n>>")),int(input("boyingizni kiritng\n>>")),int(input("vaszningizni kiitng\n>>")))
Armiya.info()
print(Armiya)
