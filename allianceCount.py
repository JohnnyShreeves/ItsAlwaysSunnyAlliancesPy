import requests
import os

f = open('episodeLinks.txt', 'r')
c=0
for link in f:
    pageText = requests.get(link.strip()).text
    tmp = open('tmp.txt', 'w')
    tmp.write(pageText)
    tmp.close()
    tmp = open('tmp.txt', 'r')
    for line in tmp:
        if line.find('Alliance') != -1:
            #####   Process the content of Alliances section, maybe with tree and lxml
            print(link.strip())
            c += 1
            break
    tmp.close()
    os.remove('tmp.txt')
f.close()
print(c)

# page = requests.get('https://itsalwayssunny.fandom.com/wiki/Mac_and_Dennis:_Manhunters').text
# tmp = open('tmp.txt', 'w')
# tmp.write(page)
# tmp.close()
# tmp = open('tmp.txt', 'r')
# for line in tmp:
#     if line.find('Alliance') != -1:
#         print('x1')
# tmp.close()


