import re
with open("text2.html", encoding='utf-8') as f:
    text = f.read()
    reg = ['<.+?>', '&nbsp', '\[.+?\]', '\r\n(\r\n)+', '\d*\d']
    for regex in reg:
        text = re.sub(regex, '', text)
    with open("text3.html", 'w', encoding='utf-8') as f:
        f.write(text)
 
