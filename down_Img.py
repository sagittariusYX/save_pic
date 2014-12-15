import os, urllib, urlparse
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Pool

# global variable
sampleUrl = []
ori_num = int(raw_input('Input start page :')) - 1
end_num = int(raw_input('Input final page :'))
for i in range(ori_num,end_num):
    sampleUrl.append("http://www.dbmeizi.com/category/1?p=%d#"%i)

# For example:
# downPath = '/Users/yangxiao/Documents/python_py/saveImg/image/'
downPath = raw_input('Input picture download directory :\n')
if os.path.isdir(downPath):
    pass
else:
    os.mkdir(downPath)

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
        urllib.urlretrieve(url, os.path.join(downPath,img_name))
        print img_name + ' ok!'
    except:
        print 'warning: ' + img_name + ' failed!'

def main():
    # import pdb
    # pdb.set_trace()

    urlList = get_url_list(sampleUrl)
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
