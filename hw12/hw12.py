##regex = '[a-zA-Z]'

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

    
            
#Функция ищет папки (кстати, надо было искать файлы), в которых ХОТЯ БЫ один латинский символ, а не все; нет вывода на экран списка всех папок и файлов
