from urllib.request import urlopen
import re
import urllib

preurl='https://www.bing.com'
html=urlopen(preurl).read().decode('utf-8')

pattern=re.compile(r'/az/hprichbg.*?jpg')
bgpath=re.findall(pattern,html)

link=preurl+bgpath[0]
urllib.request.urlretrieve(link,'download.jpg')
