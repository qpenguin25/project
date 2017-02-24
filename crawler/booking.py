from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import requests
from Queue import Queue
from threading import Thread
from bs4 import BeautifulSoup  

####   爬蟲實施抓取網頁
def worker():
    while not queue.empty():
        url=queue.get()
        crawler(url) 
        
        
####   爬蟲程序        
def crawler(url):
    driver = webdriver.Chrome(executable_path='/opt/selenium/chromedriver-2.25')
    time.sleep(1)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    item_list=soup.select('.sr_flex_layout')
    for item in item_list:
        try:
            print item.select('.sr-hotel__name')[0].text.rstrip().strip().encode('utf-8')
            res1=requests.get('http://www.booking.com'+item.select('a')[0]['href'])
            soup1= BeautifulSoup(res1.text)
            print soup1.select('#showMap2 > span')[1].text.replace('\n','').encode('utf-8')
            print 'http://www.booking.com'+item.select('a')[0]['href'].encode('utf-8')
            print item.select('b')[0].text.rstrip().strip().encode('utf-8')
            print item.select('.roomPrice')[0].select('.strike-it-red_anim')[0].text.strip('\n').encode('utf-8').replace('\n','').rstrip().encode('utf-8')
            print "------------------------------------------------------------------".encode('utf-8')
        except Exception as e:
            print "------------------------------------------------------------------".encode('utf-8')
    if queue.empty():
        driver.close()
    else:
        driver.close()
        worker()

            
####   開啟瀏覽器
s1 = datetime.now() ####### 起始時間
URL='http://www.booking.com/searchresults.zh-tw.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEGyAEM2AED6AEBqAID&sid=0ae4b8657dd9d1ddcf4c3d1b2ccb1e32&sb=1&src=searchresults&src_elem=sb&error_url=http%3A%2F%2Fwww.booking.com%2Fsearchresults.zh-tw.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEGyAEM2AED6AEBqAID%3Bsid%3D0ae4b8657dd9d1ddcf4c3d1b2ccb1e32%3Bcheckin_month%3D1%3Bcheckin_monthday%3D16%3Bcheckin_year%3D2017%3Bcheckout_month%3D1%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2017%3Bcity%3D-2637882%3Bclass_interval%3D1%3Bdest_id%3D-2632378%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Bhlrd%3D0%3Bhyb_red%3D0%3Binac%3D0%3Blabel_click%3Dundef%3Bnha_red%3D0%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Bredirected_from_city%3D0%3Bredirected_from_landmark%3D0%3Bredirected_from_region%3D0%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_pageview_id%3D91dc2ac63b4d00e8%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bss%3D%25E9%25AB%2598%25E9%259B%2584%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3D%25E5%258F%25B0%25E5%258C%2597%25E5%25B8%2582%26%3B&ss=%E8%87%BA%E7%81%A3&ssne=%E9%AB%98%E9%9B%84&ssne_untouched=%E9%AB%98%E9%9B%84&city=-2632378&checkin_year=2017&checkin_month=1&checkin_monthday=16&checkout_year=2017&checkout_month=1&checkout_monthday=17&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0'
driver = webdriver.Chrome(executable_path='/opt/selenium/chromedriver-2.25')
driver.get(URL)

####   創建一個 Queue
queue = Queue()


####  抓取每一頁 URL
try:
    while True:
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(2)
        element =WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".paging-next")))
        time.sleep(2)
        queue.put(driver.current_url)
        element.click()
except Exception as e:
    print e
    print "ok!"
    driver.close()
            
            
####   啟動THREAD
threads = map(lambda i: Thread(target=worker), xrange(7))
map(lambda th: th.start(), threads)
map(lambda th: th.join(), threads)

s2 = datetime.now() ####### 結束時間
print "All  Finish "+str(s2-s1)+"!!".encode('utf-8') ####### 總共爬取資料耗費時間
