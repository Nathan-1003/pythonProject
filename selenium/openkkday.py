from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/menglungtsai/Desktop/chromedriver_mac_arm64/chromedriver")

driver.set_window_size(1024, 768)

driver.get("https://www.kkday.com/zh-tw")

#time.sleep(3)

print(driver.page_source) #取網頁原始碼

# search_box = driver.find_element_by_id("search_experience_value")
# search_box.send_keys("台北")
# search_box.submit()
#
# driver.implicitly_wait(10)
#
# search_results = driver.find_elements_by_css_selector("h3")
# for result in search_results:
#     print(result.text)
