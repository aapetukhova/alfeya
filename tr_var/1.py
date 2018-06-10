import re
import collections

def file(filename):
    with open(filename, encoding='utf-8') as f: 
        lines = f.readlines()
    return lines

def avg(lines):
    w = 0
    ana = 0
    for line in lines:
        ws = re.findall('^<w>.+?', line)
        w = w + len(ws)
        anas = re.findall('<ana.+?>', line)
        ana = ana + len(anas)
    n = ana/w
    print('Среднее количество разборов: ', n)
    
def freq(lines):
    s = []
    for line in lines:
        pos = re.findall('gr="([A-Z]+)', line)
        for i in range (0, len(pos)):
            if pos:
                s.append(pos[i])
    return s

def out(filename, s):
    counter = collections.Counter(s)
    with open(filename, 'w', encoding='utf-8') as f:
        t = '{}\t{}'
        for key, value in counter.items():
            f.write(key)
            f.write('\t')
            f.write(str(value))
            f.write('\n')

def abl(lines, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range (0, len(lines)):
            pos = re.search('<ana.+gr="S,.+/>(.+)</w>', lines[i])
            ab = re.search('<ana.+gr="S,.+твор.+?/>', lines[i])
            if pos and ab:
                for j in range (i-3, i+4):
                    lal = re.search('<ana.+/>(.+)</w>', lines[j])
                    punc = re.search('<ana.+/>.+</w>(.)', lines[j])
                    if lal:
                        f.write(lal.group(1))
                    if punc:
                        f.write(punc.group(1))
                    f.write(' ')
                    if j == i-1 or j == i:
                        f.write('\t')
                f.write('\n')
                                        
def main():
    avg(file('karenina.xml'))
    out('file_2.xml', freq(file('karenina.xml')))
    abl(file('karenina.xml'), 'file.xml')

if __name__ == '__main__':

    main()
