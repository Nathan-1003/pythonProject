from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options=Options()

options.chrome_executable_path="/Users/menglungtsai/Desktop/chromedriver_mac_arm64/chromedriver"

driver=webdriver.Chrome(options=options)

driver.set_window_size(1024, 768)

driver.get("https://www.ptt.cc/bbs/Stock/index.html")

print(driver.page_source) #取網頁原始碼

time.sleep(3)
