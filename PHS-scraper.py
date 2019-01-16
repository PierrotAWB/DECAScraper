import os
from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve

#MULTI
event = ['pfn', 'pmk', 'pht', 'pbm']
for e in event: 
	print ('***' + e + '***')
	URL = 'http://prestondeca.weebly.com/' + e + '.html'
	s = e.upper()
	OUTPUT_DIR = '/Users/andrewwang/Dropbox/Case Studies/Principles/' + s  # path to output folder, '.' or '' uses current folder

#SINGLE
#URL = 'http://prestondeca.weebly.com/bfs.html'
#OUTPUT_DIR = '/Users/andrewwang/Dropbox/Case Studies/Finance/BFS'

	u = urlopen(URL)
	try:
	    html = u.read().decode('utf-8')
	finally:
	    u.close()

	soup = BeautifulSoup(html, "html.parser")
	downloaded = 1
	nfiles = len(soup.select('a[href^="/uploads/"]'))
	for link in soup.select('a[href^="/uploads"]'):
	    href = link.get('href')
	    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx', '.pdf', '.doc', '.xlsx', '.docx']):
	        continue

	    filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])

	    href = "http://prestondeca.weebly.com" + href

	    print("Downloading %d of %d..." % (downloaded, nfiles) )
	    urlretrieve(href, filename)
	    downloaded += 1
	print('Done.')
print('Complete!')