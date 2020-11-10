import urllib.request
import urllib.parse
import re
url = 'https://www.finn.no/bap/forsale/ad.html?finnkode=197443473'



req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData)

paragraphs = re.findall(r'<h1 class = "u-tu">(.*?)</h1>',str(respData))

for par in paragraphs:
    print(par)
