with open("C:/Users/annap/Desktop/alal.txt", "r", encoding="utf-8") as f:
    text=f.read()
text=text.replace(".", ".\n")
print(text)
