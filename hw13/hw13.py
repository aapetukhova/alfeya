import os
import re
import collections

def search():
    l = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        for dir_ in dirs:
            l.append(dir_[0].lower())
    return l

def list_sorting(spisok):
    counter = collections.Counter(spisok)
    max = 0
    for key, value in counter.items():
        if value > max:
            max = value
            letter = key
    if max != 0:
        print('Буква: ', letter)
    else:
        print('Папок, удовлетворяющих условию, нет')
        
def main():
    list_sorting(search())


if __name__ == '__main__':
    main()
