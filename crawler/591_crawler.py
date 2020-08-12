from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='/Users/yingcheng/Downloads/chromedriver', options=chrome_options)
driver.get("https://sale.591.com.tw/")
time.sleep(5)

driver.find_element_by_xpath("//*[@id='goodhouse-popbox']/div[2]").click()

#driver.find_element_by_xpath("//*[@id='keywords']").send_keys("新竹")
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[1]/div[1]/div/span').click()

driver.find_element_by_xpath('//*[@id="filter"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id="filter"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[4]/a').click()



#driver.quit()
