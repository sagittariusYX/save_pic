#!/usr/bin/python
import os, urllib, urlparse
import zipfile
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Pool

import utils
import log

LOG = log.get_logger()

# URL
SAMPLEURL = []
ori_num = int(raw_input('Input start page :')) - 1
end_num = int(raw_input('Input final page :'))
for i in range(ori_num,end_num):
    SAMPLEURL.append(utils.get_config('urladdr','URLSAMPLE')%i)

# TARGETDIR
TARGETDIR = utils.get_config('downpath','DOWNDIR')
if os.path.isdir(TARGETDIR):
    pass
else:
    os.mkdir(TARGETDIR)


def get_url_list(url):
    aList = []
    for eachUrl in url:
        soup = BeautifulSoup(urllib.urlopen(eachUrl).read())
        map(aList.append, [str(item.get('src', item.get('data-src'))) for item in soup("img")])
    return tuple(aList)

def download_pic(url):
    img_name = urlparse.urlparse(url)[2].split('/')[4]
    try:
        urllib.urlretrieve(url, os.path.join(TARGETDIR,img_name))
        LOG.info(img_name + ' ok!')
    except:
        LOG.error('error: ' + img_name + ' failed!')

def zip_pic(dir):
    f = zipfile.ZipFile(utils.get_config('zippath','ZIPDIR'),'w',zipfile.ZIP_DEFLATED)
    try:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                f.write(os.path.join(TARGETDIR, filename))
        f.close()
        LOG.info('zip finished!')
        print 'zip finished!'
    except:
        LOG.error('error: zip failed!')

def main():
    # import pdb
    # pdb.set_trace()

    urlList = get_url_list(SAMPLEURL)
    start_time = datetime.now()

    pool = Pool(len(urlList))
    pool.map(download_pic,urlList)
    pool.close()
    pool.join()

    zip_pic(TARGETDIR)

    end_time = datetime.now()
    # print Finished time
    print ('[' + str(len(urlList)) + ' pictures finished in ' + str(end_time - start_time) + ']')

if __name__ == "__main__":
    main()
