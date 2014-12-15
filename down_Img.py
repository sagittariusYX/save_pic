import os, urllib, urlparse
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Pool

import utils

# URL
SAMPLEURL = []
ori_num = int(raw_input('Input start page :')) - 1
end_num = int(raw_input('Input final page :'))
for i in range(ori_num,end_num):
    SAMPLEURL.append(utils.get_config('urladdr','URLSAMPLE')%i)

# DOWNPATH
DOWNPATH = utils.get_config('downpath','DOWNDIR')
if os.path.isdir(DOWNPATH):
    pass
else:
    os.mkdir(DOWNPATH)


def get_url_list(url):
    aList = []
    for eachUrl in url:
        soup = BeautifulSoup(urllib.urlopen(eachUrl).read())
        for item in soup.find_all('img'):
            aList.append(str(item.get('src',item.get('data-src'))))
    return tuple(aList)

def download_pic(url):
    img_name = urlparse.urlparse(url)[2].split('/')[4]
    try:
        urllib.urlretrieve(url, os.path.join(DOWNPATH,img_name))
        print (img_name + ' ok!')
    except:
        LOG.error('error: ' + img_name + ' failed!')

def main():
    # import pdb
    # pdb.set_trace()

    urlList = get_url_list(SAMPLEURL)
    start_time = datetime.now()

    pool = Pool(len(urlList))
    pool.map(download_pic,urlList)
    pool.close()
    pool.join()

    end_time = datetime.now()
    # print Finished time
    print ('[' + str(len(urlList)) + ' pictures finished in ' + str(end_time - start_time) + ']')

if __name__ == "__main__":
    main()
