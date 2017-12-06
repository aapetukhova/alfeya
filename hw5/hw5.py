while True:
    f=input("Please insert a latin word: ")
    m=len(f)
    if (f[-2:]=="re" or f[-2:]=="ri" or (f[-1:]=="i" and f[-2:]!="ai" and f[-2:]!="ei") or f[-4:]=="isse" ):
        with open("latin.txt", "a", encoding="utf-8") as n:
            n.write(f)
            n.write("\n")
    if f=="":
        break



    
