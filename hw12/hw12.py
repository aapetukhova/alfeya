##regex = '[a-zA-Z]'

import os
import re

def latin():
    l = []
    file_list = os.listdir()
    for file in file_list:
        r = re.search('[a-zA-Z]', file)
        if r and os.path.isdir(file):
            l.append(file)
    return l

def counter(spisok):
    k = len(spisok)
    return k
    
def main():
    a = latin()
    print('Найдено папок:', counter(a))
    for file in a:
        print(file)

if __name__ == '__main__':
    main()

    
            
