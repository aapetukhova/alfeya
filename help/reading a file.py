
#reading a file, list of words
def text(filename):
    symbols = '123456789.,/!?|\@#$%^&*():'"{}[];_-=+<>№'
    d = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                d.append(word.strip(symbols))
    return d


                
