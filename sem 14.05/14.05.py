import os

def search():
    a = []
    b = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        for dir_ in dirs:
            if 'r' in dir_:
                b.append(dir_)
                for file in files:
                    if 'd' in file:
                        print(file)
        for file in files:
            if 'd' in file:
                a.append(file)
##                if 'r' in dirs:
##                    print(file)            
    n = len(a)
    m = len(b)
    print(n, m)
##    print(a)
##    print(b)

##    return n, m

def main():
    search()

if __name__ == '__main__':
    main()



    
    
                
