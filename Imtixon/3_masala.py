class kitoob():
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.muallifi=b
        self.narxi=c
        self.nashiryoti=d
    def chiqar(self):
        print("kitob nomi {}".format(self.nomi))
        print("kitob muallifi {}".format(self.muallifi))
        print("kitob narxi {}".format(self.narxi))
        print("kitob nihol {}".format(self.nashiryoti))
k=kitoob('asaxiy', 'hooks', 63000, 'nihol')
k=kitoob('axiy','book',62000,'holi')
k=kitoob('saxiy','book',45000,'ali')
ka=list()
ka.append(k.nomi)
ka.append(k.muallifi)
ka.append(k.narxi)
ka.append(k.nashiryoti)
ka.sort()
for i in ka:
    if i[0]=='a':
        k.chiqar()