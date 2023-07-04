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

    def search_on_xv(self):
        self.driver.get("https://www.xvideos.com/")
        #time.sleep(3)
        search = self.driver.find_element(By.NAME, "k") #安德說用這，會需要用到from selenium.webdriver.common.by import By
        #elem = driver.find_element_by_name("q")
        search.send_keys("台灣")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        print(self.driver.title)

        # tags = self.driver.find_elements(By.XPATH,'//*[@id="search-associates"]')
        # for tag in tags:     # 遍歷元素並獲取文本內容
        #     tag_text = tag.text
        #     print(tag_text)

        # titles = self.driver.find_elements(By.XPATH,'//div[@class="thumb-under"]//p[@class="title"]/a')
        # for title in titles:     # 遍歷元素並獲取文本內容
        #     title_text = title.text
        #     print(title_text)

        title1 = self.driver.find_element(By.XPATH,'//*[@id="video_74855398"]/div[2]/p[1]/a')
        print(title1)

if __name__ == "__main__":
    web_driver = MyWebDriver() #將類別改為物件
    web_driver.search_on_xv()