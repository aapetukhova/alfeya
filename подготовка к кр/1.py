##на швили
##на дзе
##во сколько раз -дзе > -швили

import re

#чтение файла

def page(filename):
    with open( filename, encoding='utf-8') as f:
        lines = f.readlines()        
    return lines

#счет необходимого
def count( regex, links):
    n = 0
    for link in links:
        r = re.search( regex, link)
        if r:
            n+=1
    return n

def comparing(a, b):
    t = a/b
    print(t)
    return t

def main():
    file = page('short.html')
    sh = count('<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?швили</a>', file)
    dze = count('<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?дзе</a>', file)
    comparing(dze, sh)

if __name__ == '__main__':
    main()

##имя/фамилия/отчество
##^[А-Я].? [А-Я].? [А-Я].?
##
##ссылка
##<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?</a>
    
