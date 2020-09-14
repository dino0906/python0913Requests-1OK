##漫畫擷取器,有幾頁就拿幾頁
from selenium import webdriver
import requests
import time

driver = webdriver.Chrome()
driver.get('https://comicbus.live/online/a-103.html?ch=471')
# print(driver.page_source) #檢查抓取OK

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml') #取得原始碼
# print(soup.select_one('#TheImg').get('src')) #檢查只抓取連結OK
print('http:' + soup.select_one('#TheImg').get('src')) #檢查手動的網址

page_num = int(soup.select_one('#pagenum').text.split('/')[1].strip('頁')) #找到頁數,取/後的數,去除字,轉換int


page_url = 'https://comicbus.live/online/a-103.html?ch=471-' #準備抓各頁面
for i in range(page_num): #從1~末,有幾頁就刷幾頁
    # print('{}{}'.format(page_url,i+1)) #檢查手動網頁
    driver.get('{}{}'.format(page_url,i+1))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img_url = 'http:' + soup.select_one('#TheImg').get('src')

    r = requests.get(img_url)
    with open('{}.jpg'.format(i+1), 'wb') as f: #因為是圖片,所以用wb
        f.write(r.content)
        print('總共{}頁,正下載第{}頁'.format(page_num,i+1))
    time.sleep(2)