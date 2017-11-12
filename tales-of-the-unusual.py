#! python3
# qiqiguaiguatales-of-the-unusual.py - Downloads tales-of-the-unusual comic.
import requests, os, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
url = 'https://www.dongmanmanhua.cn/thriller/tales-of-the-unusual/%E7%AC%AC201%E8%AF%9D-%E7%97%A3%E8%BF%9E%E9%AC%BC-4/viewer?title_no=296&episode_no=202'  # starting url
os.makedirs('tales-of-the-unusual',exist_ok=True) # store comics ./tales-of-the-unusual
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
# proxy
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

# Download the page
logging.debug('Downloading page %s...' % url)
res = requests.get(url,headers=headers,proxies=proxies)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html')

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
            res = requests.get(comicUrl,headers=headers,proxies=proxies)
            res.raise_for_status()
            #Save the image to ./tales-of-the-unusual.
            imageFile = open(os.path.join('tales-of-the-unusual', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        except requests.exceptions.MissingSchema:
            continue
        
print('Done.')