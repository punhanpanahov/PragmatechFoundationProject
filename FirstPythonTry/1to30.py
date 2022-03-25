def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
upper=int(input("Upper,ust heddi yaz: "))
# en ust heddi 30 edecik

printno(upper)