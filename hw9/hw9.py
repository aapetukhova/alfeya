def text(filename):
    with open(filename, encoding='utf-8') as f: 
        text = f.read()   
    return text

def main():
    lala = text('gorky.txt')
    import re
    s = re.compile('вып(и(в(ш(ая|и(й|х|м(и)?)?))?[^а-я]|т(а(я)?|ы(й|х|м(и)?))?)|ь(ю(т)?|(е(шь|м|т(е)?)))(ся)?|ей(те)?(сь)?)', re.IGNORECASE)
    iterator = s.finditer(lala)
    for match in iterator:
        print(match.group())

if __name__ == '__main__':
    main()

