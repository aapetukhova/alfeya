##В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём (в зависимости от варианта): 
##формы глагола «выпить»


import re
def words(filename):
    with open(filename, encoding='utf-8') as f: 
        text = f.read()
        words = text.split()
    return words

def main():
    w = words('gorky.txt')
    for word in w:
        r = re.search('вып(и(в(ш(ая|и(й|х|м(и)?)?))?[^а-я]|т(а(я)?|ы(й|х|м(и)?))?)|ь(ю(т)?|(е(шь|м|т(е)?)))(ся)?|ей(те)?(сь)?)', word)
        if r:
            print(r)



if __name__ == '__main__':
    main()
