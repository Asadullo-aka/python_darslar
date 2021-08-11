class Shogirt:
    def __init__(self,ism,fam,yoshi):
        self.ism=ism
        self.fam=fam
        self.yoshi=yoshi
    def info (self):
        print(f">>Ismi {self.ism} \n>>Familyasi {self.fam} \n>>Yoshi {self.yoshi}")
class Ustoz(Shogirt):
    def __init__(self, ism, fam, yoshi,yili):
        super().__init__(ism, fam, yoshi)
        self.yili=yili
    def info(self):
        super().info()
        print(f">>Tug'ilgan yili {self.yili}")
U=Ustoz (input('ismingiz\n>>'),input('familyangiz\n>>'),int(input("yoshingiz\n>>")),int(input("Tugilgan yilingiz\n>>")))
U.info()
print("Shogirt anketasi")
S=Shogirt(input('ismingiz\n>>'),input('familyangiz\n>>'),int(input("yoshingiz\n>>\n ")))
S.info()