from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MyWebDriver:
    def __init__(self):
        options = Options()
        options.chrome_executable_path = "/Users/menglungtsai/Desktop/chromedriver_mac_arm64/chromedriver"
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1024, 768)

        #print(driver.page_source) #取網頁原始碼

    def search_on_ptt(self):
        self.driver.get("https://www.ptt.cc/bbs/Stock/index.html")
        search = self.driver.find_element(By.NAME, "q") #安德說用這，會需要用到from selenium.webdriver.common.by import By
        #elem = driver.find_element_by_name("q")
        search.send_keys("TSMC")
        search.clear()
        search.send_keys("台積電")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        # print(self.driver.title)
        #titles = self.driver.find_elements(By.TAG_NAME, "a")    #列出該頁所有關於a的Name屬性
        #titles = self.driver.find_elements(By.XPATH,'//*[@id="main-container"]a')
        titles = self.driver.find_elements(By.XPATH,'//*[@id="main-container"]/div[2]//a')
        for title in titles:     # 遍歷元素並獲取文本內容
            a_text = title.text
            print(a_text)

        Previous = self.driver.find_element(By.XPATH, '//*[@id="action-bar-container"]/div/div[2]/a[2]')
        Previous.click()
        time.sleep(2)
        titles2 = self.driver.find_elements(By.XPATH,'//*[@id="main-container"]/div[2]//a')
        for title in titles2:     # 遍歷元素並獲取文本內容
            a_text2 = title.text
            print('Previous2',a_text2)

#<input class="query" type="text" name="q" value="" placeholder="搜尋文章⋯">

if __name__ == "__main__":
    web_driver = MyWebDriver() #將類別改為物件
    web_driver.search_on_ptt()
#
#
# //*[@id="main-container"]/div[2]/div[2]/div[2]
# //*[@id="main-container"]/div[2]/div[3]/div[2]

