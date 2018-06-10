##regex = '[a-zA-Z]'

##Программа должна просмотреть все папки и файлы, находящиеся в одной папке с ней, и сообщить следующую информацию (а также смотрите дополнительное задание внизу!):
##Сколько найдено файлов, название которых состоит только из латинских символов
##Кроме этого, программа должна выводить на экран названия всех файлов или папок, которые она нашла, без повторов (это задание на 9 и 10).

import os
import re

def latin():
    print('Все файлы и папки:')
    l = []
    file_list = os.listdir()
    for file in file_list:
        print(file)
        r = re.search('^[a-zA-Z]+?', file)
        if r and os.path.isfile(file):
            l.append(file)
    return l

def counter(spisok):
    k = len(spisok)
    return k
    
def main():
    a = latin()
    print('')
    print('Найдено файлов:', counter(a))
    for file in a:
        print(file)

if __name__ == '__main__':
    main()

    
            

