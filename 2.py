import re

def page(filename):
    with open( filename, encoding='utf-8') as f:
        text = f.readlines()        
    return text

def gal(lines, regex, name, exp):
    for line in lines:
        r = re.search(regex, lines)
        if r:
            t = len(r.group(1))
            if t >= 6:
                lines = re.sub( exp, name, lines)
    return lines

def changed(filename, file):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(file)
    return file

def main():
    s = page('short.html')
    gala = gal(s, '<a href.+?>([А-Я].+?) [А-Я].+? [А-Я].+?швили</a>|<a href.+?>([А-Я].+?) [А-Я].+? [А-Я].+?дзе</a>', 'Галактион', '[А-Я].+?')
    changed('galaktion.html', gala)
    
if __name__ == '__main__':
    main()

