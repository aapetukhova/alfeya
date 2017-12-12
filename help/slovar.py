with open ("C:/Users/annap/Desktop/sl.csv", "r", encoding="utf-8") as f:
    for line in f:
        word=line.split()
        if word[1]=="conj":
            print(word[0].strip('"'))
