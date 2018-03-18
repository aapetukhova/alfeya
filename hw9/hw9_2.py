import re

def words(filename):
    with open(filename, encoding='utf-8') as f: 
        text = f.read()
        words = text.split()
    return words

def main():
    inf = words('bulgakov.txt')
    for word in inf:
        r = re.search('((вып(и(в(ш(ая|и(й|х|м(и)?)?))?|т(а(я)?|ы(й|х|м(и)?))?)|ь(ю(т)?|(е(шь|м|т(е)?)))(ся)?|ей(те)?(сь)?)))', word)
        if r:
            g = r.group(1)
            print(g)

if __name__ == '__main__':
    main()


