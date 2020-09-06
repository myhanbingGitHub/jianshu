import requests

import requests
from bs4 import BeautifulSoup

def test_webpage(url):
    h={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    r = requests.get(url,headers=h)

    s = BeautifulSoup(r.text,'lxml')
    print(r.status_code)
    print(r.request.headers)



if __name__=='__main__':
    test_webpage('https://www.jianshu.com/p/d7ee1236f1d5')