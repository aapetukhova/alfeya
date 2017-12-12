k = 0
with open ("Extinct_languages.tsv", "r", encoding="utf-8") as f:
    for line in f:
        word = line.split("\t")
        if word[2] == "Critically endangered\n":
            k = k + 1
    print ("Critically endangered languages: ", k)
            
