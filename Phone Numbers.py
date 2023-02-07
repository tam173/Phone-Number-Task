def PhoneN():
    f=open("PhoneNumber",'r')
    for x in f:
        x=x.strip()
        print("{}-{}-{}".format(x[:3],x[3:6],x[6:]))
        