from urllib.request import urlopen
import re
import urllib

url=input('Enter url: ')
html=urlopen(url).read().decode('utf-8')

pattern=re.compile(r'http://dl.*m4a')
get=re.findall(pattern,html)

link=get[0]
urllib.request.urlretrieve(link,'download.m4a')
