from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
class Login:
    def login(self):
        # 实例化浏览器
        self.d= webdriver.Chrome()
        # 打开登录界面
        self.d.get("http://192.168.12.205/login")
        # WebDriverWait(self.d,60.1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input'))
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input').clear()
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input').send_keys("admin")
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[2]/div/div/input').clear()
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[2]/div/div/input').send_keys('admin')
        # sleep(1)
        #点击提交登录系统
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/button').click()
        sleep(2)