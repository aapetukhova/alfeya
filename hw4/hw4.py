k=0;
n3=0;
n1=0;
with open("text.txt", "r", encoding="utf-8") as f:
    text=f.read()
    words=text.split()
    for i in range (0, len(words)):
        n=len(words[i])
        if n==3:
            n3+=1
        if n==1:
            n1+=1
    if n1>0:
        k=n3/n1
        print(k)
    else:
        print("слов длины 1 нет")
