import re
##with open("Философия — Википедия.html", encoding='utf-8') as f:
##    text = f.read()
##    text = re.sub( 'философи(.)', 'астрологи\\1', text)
##    text = re.sub( 'Философи(.)', 'Астрологи\\1', text)    
##    with open("astrology.html", 'w', encoding='utf-8') as f:
##        f.write(text)
        
def original(filename):
    with open( filename, encoding='utf-8') as f:
        text = f.read()
    return text
    
def changed(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return text

def regex( a, b, file):
    file = re.sub( a, b, file)
    return file

def main():
    philosophy = original('philosophy.html')
    philosophy = regex('Философи(.)', 'Астрологи\\1', philosophy)
    philosophy = regex('философи(.)', 'астрологи\\1', philosophy)
    philosophy = regex('ФИЛОСОФИ(.)', 'АСТРОЛОГИ\\1', philosophy) #на всякий случай....
    changed('astrology.html', philosophy)


if __name__ == '__main__':
    main()
