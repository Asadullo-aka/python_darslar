with open ("numbers","") as d:
    for i  in d.read().split():
        if len(i)%2==0:
            with open("juft","a") as w1:
                w1.write(i+"")
        else:
            with open ("toq","a") as w2:
                w2.write(i+" ")