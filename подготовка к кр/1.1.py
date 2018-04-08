import re

def page(filename):
    with open( filename, encoding='utf-8') as f:
        lines = f.readlines()        
    return lines

def count( regex, links):
    n = 0
    for link in links:
        r = re.search( regex, link)
        if r:
            n+=1
    return n

def main():
    file = page('short.html')
    print(count('<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?ия</a>', file))

if __name__ == '__main__':
    main()
