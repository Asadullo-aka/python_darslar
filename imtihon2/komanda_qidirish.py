class komanda():
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.soni=b
        self.treneri=c
        self.kapitani=d
    def chiqarish(self):
        print("---------------------------------");
        print("Komanda nomi:",self.nomi)
        print("Komanda ish.soni:",self.soni)
        print("Komanda murabbiyi:",self.treneri)
        print("Komanda kapitani:",self.kapitani)
        print("---------------------------------");
def sorting():
    team1=komanda("Liverpool", 11, "Klopp", "Henderson")
    team2=komanda("Arsenal", 11, "Venger", "Aubomeyang")
    team3=komanda("ManCity", 11, "Gvardiola", "DeBruyne")
    team4=komanda("Real", 11, "Anchelotti", "Ramos")
    team5=komanda("Barcelona", 11, "Human", "Messi")
    team=list()
    team.append(team1.nomi)
    team.append(team2.nomi)
    team.append(team3.nomi)
    team.append(team4.nomi)
    team.append(team5.nomi)
    team.sort()
    for i in team:
        if i==team1.nomi:
            team1.chiqarish()
        elif i==team2.nomi:
            team2.chiqarish()
        elif i==team3.nomi:
            team3.chiqarish()
        elif i==team4.nomi:
            team4.chiqarish()
        else:
            team5.chiqarish()
def searching():
    team1=komanda("Liverpool", 11, "Klopp", "Henderson")
    team2=komanda("Arsenal", 11, "Venger", "Aubomeyang")
    team3=komanda("ManCity", 11, "Gvardiola", "DeBruyne")
    team4=komanda("Real", 11, "Anchelotti", "Ramos")
    team5=komanda("Barcelona", 11, "Human", "Messi")
    new_team=input("Qidirilayotgan komanda: ")
    if new_team.title()==team1.nomi:
        team1.chiqarish()
    elif new_team.title()==team2.nomi:
        team2.chiqarish()
    elif new_team.title()==team3.nomi:
        team3.chiqarish()
    elif new_team.title()==team4.nomi:
        team4.chiqarish()
    elif new_team.title()==team5.nomi:
        team5.chiqarish()
    else:
        print("Bunday komanda yo'q UZUR")

sorting()
searching()