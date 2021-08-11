def nom(soz,n):
    if len(soz)==n:
        pass
    else:
        print(soz[-n:]+soz[0:len(soz)-n])
nom(input("soz kiritng__"),int(input('sonni kiritng: ')))