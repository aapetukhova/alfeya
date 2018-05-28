import collections


def text():
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№—'
    d = []
    with open('text.txt', encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                d.append(word.strip(symbols))
    return d

def gram(d):
    dn = []
    n = int(input('N: '))
    m = len(d)
    for i in range (0, m-n+1):
        p = ''
        for j in range (i, i+n):
            p = p + d[j] + ' ' 
        dn.append(p)
#цикл формирования n-грам        
    return dn

def freq(dn):
    s = collections.Counter(dn)
    with open('output.csv', 'w', encoding='utf-8') as f:
        for value in sorted(s, key = s.get, reverse=True):
            f.write(value)
            f.write(' ')
            f.write(str(s[value]))
            f.write('\n')

def main():
    a = freq(gram(text()))
    

if __name__ == '__main__':
    main()

#ключ - строчка, проверять, число ли это
#проверка, дошли ли мы до конца
    
        
        
        
