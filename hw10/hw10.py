import re
def page(filename):
    with open( filename, encoding='utf-8') as f:
        lines = f.readlines()        
    return lines

def name(datas):
    for data in datas:            
        r = re.search('<h1 id="firstHeading".+>(.+)</h1>', data)
        if r:
            scientist = r.group(1)
    return scientist

def field(datas):
    n = len(datas)
    for i in range (0, n):            
        r1 = re.search('Научная сфера', datas[i])
        if r1:
            r2 = re.search('title="(.+)"', datas[i+1])
            g = r2.group(1)
    return g

def result(filename, a, b):
    with open( filename, "w", encoding="utf-8") as f:
        f.write(a)
        f.write(' - ')
        f.write(b)
        f.write('\n')
        


def main():
    lines = page('landau.html')
    s = name(lines)
    g = field(lines)
    result('text.txt', s, g)
    
if __name__ == '__main__':
    main()


