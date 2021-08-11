
with open("fayl", "r") as fp:
    with open("new1", "w") as new1:
        with open("new2", "w") as new2:
            for i in fp.readlines():
                for j in i.split():
                    if len(j) % 2 == 0:
                        new1.write(j+' ')
                    else:
                        new2.write(j+' ')