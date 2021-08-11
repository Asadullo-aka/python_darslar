class Usta:
    def __init__(self,ism,fam,yosh):
        self.name=ism
        self.surname=fam
        self.age=yosh
    def chiqar(self):
        print(f">>Ismim {self.name} \n>>familyasi {self.surname} \n>>Yoshi {self.age}")
class Ustoz(Usta):
    def __init__(self, ism, fam, yosh,maosh):
        super().__init__(ism, fam, yosh)
        self.oy=maosh
    def chiqar(self):
        super().chiqar()
        print(f">>Maoshi {self.oy}\n\n")
Us=Ustoz("Asdullo","Qodirov",23,"10 mln")
Us.chiqar()
Us=Usta("Asadullo", "Tosshpolatov", 23)
Us.chiqar()
       