author = {"php":"Rasmus Lerdorf",\
    "perl":"Larry Wall",\
    "tcl":"John Ousterhout",\
    "awk":"Brian Kernighan",\
    "java":"James Gosling",\
    "parrot":"Simon Cozens",\
    "python":"Guido van Rossum"}
#Либо так:
langs = author.keys()
langs.sort()
for language in langs:
    print language," - ",author[language]
#либо так:
for key in sorted(author.iterkeys()):
    print "%s: %s" % (key, author[key])
    
>>> awk  -  Brian Kernighan
>>> java  -  James Gosling
>>> parrot  -  Simon Cozens
>>> perl  -  Larry Wall
>>> php  -  Rasmus Lerdorf
>>> python  -  Guido van Rossum
>>> tcl  -  John Ousterhout
# Если вам нужна коллекция с доступом по ключу — словарь подходит для этого лучше всего. Если вам нужна коллекция для хранения произвольных объектов произвольной вложенности — словарь в этом вам поможет.
