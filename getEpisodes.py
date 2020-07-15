import requests

sunnyURL = 'https://itsalwayssunny.fandom.com/wiki/Category:It%27s_Always_Sunny_in_Philadelphia_Episodes'
urlPrefix = 'https://itsalwayssunny.fandom.com'
links = []

# download HTML content and save locally
page = requests.get(sunnyURL)

f = open('episodeList.html', 'w')
f.write(page.text)
f.close()

# extract episode links from raw HTML (very manual scrape)
f = open('episodeList.html', 'r')

for line in f:
    if line[0:41] == '<div style="font-size:130%;"><b>"<a href=':
        titlePos = line.index('title=')
        links.append(line[42:titlePos-2])
f.close()

# save full episode URLs to file
f = open('episodeLinks.txt', 'w')
for x in links:
    link = urlPrefix + x + '\n'
    f.write(link)
f.close()
