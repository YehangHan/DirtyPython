#! python3
# qiqiguaiguatales-of-the-unusual.py - Downloads tales-of-the-unusual comic.
import requests, os, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
url = 'http://www.webtoons.com/zh-hant/thriller/tales-of-the-unusual/%E7%AC%AC199%E8%A9%B1-%E7%B8%AB%E7%97%A3%E9%AC%BC-2/viewer?title_no=290&episode_no=200'  # starting url
os.makedirs('tales-of-the-unusual',exist_ok=True) # store comics ./tales-of-the-unusual
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Referer': 'http://www.webtoons.com/zh-hant/thriller/tales-of-the-unusual/%E7%AC%AC199%E8%A9%B1-%E7%B8%AB%E7%97%A3%E9%AC%BC-2/viewer?title_no=290&episode_no=200'
    }


# Download the page
logging.debug('Downloading page %s...' % url)
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'lxml')

# Find the URL of the comic image.
comicElem = soup.select('#_imageList img')
if comicElem == []:
    logging.debug('Could not find comic images.')
else:
    logging.debug(len(comicElem))
    for elem in comicElem:
        comicUrl = elem.get('data-url')
        logging.debug('Downloading image %s...' % (comicUrl))
        try:
            res = requests.get(comicUrl,headers=headers)
            res.raise_for_status()
            #Save the image to ./tales-of-the-unusual.
            filebasename = os.path.basename(comicUrl)
            filename = filebasename.split('?')[0]
            imageFile = open(os.path.join('tales-of-the-unusual', filename),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        except requests.exceptions.MissingSchema:
            continue
        
print('Done.')