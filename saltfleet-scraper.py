import os
from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve

URL = 'https://saltfleetdeca.commons.hwdsb.on.ca/sample-page/'
OUTPUT_DIR = '/Users/andrewwang/Dropbox/Case Studies'  # path to output folder, '.' or '' uses current folder

u = urlopen(URL)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")
downloaded = 1
nfiles = len(soup.select('a[href^="https://s3.amazonaws.com/"]'))
for link in soup.select('a[href^="https://s3.amazonaws.com/"]'):
    href = link.get('href')
    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx', '.pdf', '.doc', '.xlsx', '.docx']):
        continue

    filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])

    print("Downloading %d of %d..." % (downloaded, nfiles) )
    urlretrieve(href, filename)
    downloaded += 1
print('Done.')

# /Users/andrewwang/Documents/DECA/Exams/Finance