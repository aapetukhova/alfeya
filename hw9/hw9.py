import re

def text(filename):
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
    d = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                d.append(word.strip(symbols))
    return d


def forms(words):
    s = []
    for word in s:
        if re.search('вып.?', word) and word not in s:
            s.append(word)
    print(' '.join(s))
    return s

def main():
    print(forms(text('gorky.txt')))


if __name__ == '__main__':
    main()

