vowels = ["уеыаоэяиюё"]
vow_list = list(vowels)
s = input("Your word/phrase: ")
for i in range (0, len(s)):
    print(s[i])
    for j in range (0, len(vowels)):
        if s[i] == vowels[j]:
            s[i+1] == "c"
            s[i+2] == s[i]
        i=i+3
print(s)
    
    
