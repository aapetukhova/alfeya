##reading files in the folder! os
##finding info - regex
##writing to .csv

import os
import re
import collections

def regex(reg):
    path = './news/'
    file_list = os.listdir(path)
    spisok = []
    for file in file_list:
        filename = os.path.join(path, file)
        with open(filename, encoding='windows-1251') as f:
            info = f.readlines()    
            for item in info:
                r  = re.findall(reg, item)
                if r:
                    for item in r:
                        spisok.append(item)
    return spisok

def out(filename, docs, titles, authors, years, topics, tags):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('doc_id')
        f.write(',')        
        f.write('title')
        f.write(',')
        f.write('author')
        f.write(',')
        f.write('created')
        f.write(',')
        f.write('topic')
        f.write(',')
        f.write('tagging')
        f.write('\n')
        for i in range(0, len(docs)):
            f.write(docs[i])
            f.write(',')
            f.write(titles[i])
            f.write(',')
            f.write(authors[i])
            f.write(',')
            f.write(years[i])
            f.write(',')
            f.write(topics[i])
            f.write(',')
            f.write(tags[i])
            f.write('\n')

##def abbs():
##    

            

def main():
    ids = regex('<meta content="(.+)" name="docid"')
    ts = regex('<title>(.+)</title>')
    aus = regex('<meta content="(.+)" name="author"')
    cs = regex('<meta content="(.+)" name="created"')
    tops = regex('<meta content="(.+)" name="topic"')
    tas = regex('<meta content="(.+)" name="tagging"')    
    out('out.csv', ids, ts, aus, cs, tops, tas) 

if __name__ == '__main__':
    main()
    
            
            
    
            
    
