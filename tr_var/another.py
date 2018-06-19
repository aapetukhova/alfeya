def text(filename):
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
    d = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                d.append(word.strip(symbols))
    return d

def maxi(d):
    maxim = 0
    for word in d:
        if len(word) > maxim:
            maxim = len(word)
    print(maxim)
    return maxim      
   
def align(d):
    m=int(6)
    t = '{:>m}'
    for item in d:
        print(t.format(item))
        
def main():
    align(text('text.txt'))

if __name__ == '__main__':
    main()
