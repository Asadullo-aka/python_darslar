with open ("numbers","r") as f:
    f.seek(12)
    print(f.read())
#%%
with open("numbers","r") as p:
    p.readline()
    print(p.tell())
    print(p.readlines())
    print(p.tell())
    