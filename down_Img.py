#!/usr/bin/python
import os, urllib, urlparse
import zipfile
import gevent
from datetime import datetime
from bs4 import BeautifulSoup
# from multiprocessing import Pool
from gevent import monkey; monkey.patch_all()

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
try:
    if os.path.isdir(TARGETDIR):
        pass
    else:
        os.mkdir(TARGETDIR)
except:
    print 'dirname exists, change another name!'
    os._exit(0)


def get_url_list(url):
    aList = []
    for eachUrl in url:
        try:
            resp = urllib.urlopen(eachUrl)
        except URLError, e:
            LOG.error('error: ' + e.reason + ', ' + e.code())
        soup = BeautifulSoup(resp.read())
        map(aList.append, [str(item.get('src', item.get('data-src'))) for item in soup("img")])
    return tuple(aList)

def download_pic(url):
    img_name = urlparse.urlparse(url).path.split('/')[2]
    try:
        # urllib.urlretrieve(url, os.path.join(TARGETDIR,img_name))
        os.system("wget " + url + " -P " + os.path.join(TARGETDIR))
        LOG.info(img_name + ' ok!')
    except URLError, e:
        if 404 == e.code:
            LOG.error('error: ' + img_name + ' not found, moving on!')
        else:
            LOG.error('error: ' + img_name + ' : ' + e)

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
    start_time = datetime.now()
    urlList = get_url_list(SAMPLEURL)
    print urlList[0]

    # pool = Pool(len(urlList))
    # pool.map(download_pic,urlList)
    # pool.close()
    # pool.join()
    jobs = [gevent.spawn(download_pic, urlname) for urlname in urlList]
    gevent.joinall(jobs, timeout = 20)

    # zip_pic(TARGETDIR)

    end_time = datetime.now()
    # print Finished time
    print ('[' + str(len(urlList)) + ' pictures finished in ' + str(end_time - start_time) + ']')

if __name__ == "__main__":
    main()
