def raw_word():
    with open ("C:/Users/student/Desktop/rj.txt", "r", encoding="utf-8") as f:
        for line in f:
            word=line.split()
            for raw in word:
                raw=raw.strip(".,!?;:'()")
##        print(raw)
##массив-word
 
def lowercase(a):
    for raw in word:
        raw=raw.lower()
##        print(raw)

