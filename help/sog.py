vow="aouye"
v=list(vow)
n=len(v)
with open("C:/Users/annap/Desktop/alal.txt", "r", encoding="utf-8") as f:
    text=f.read()
t=(text)
m=len(t)
gl=0
sogl=0
for i in range(0,m):
    for j in range (0, n):
        if t[i]==v[j]:
            gl+=1
            print(t[i])
            break
##        elif t[i]!=v[j] and t[i]!="" and t[i]!=".":
##            sogl+=1
##            break
print(sogl)
print(gl)
print(m)
