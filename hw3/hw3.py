word=input("Введите слово: " )
l=list(word)
n=len(l)
s=[]
m=[]
for i in range (0, n-1):
    m=l[:i]
    s=l[i+1:]
    s.extend(m)
    t="".join(s)
    print(t)

