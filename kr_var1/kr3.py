k=0
listofl = []
while True:
    lang = input("Enter Language: ")
    listofl.append(lang)
    if lang == "" :
        break
n = len(listofl)
for i in range (0, n-1):
    with open ("Extinct_languages.tsv", "r", encoding="utf-8") as f:
        for line in f:
            word = line.split("\t")
            if listofl[i] == word[0]:
                k += 1
                print (line.replace("\t", "-"))
        if k < n:
            print("No Language Found")

