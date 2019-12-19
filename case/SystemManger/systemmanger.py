from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from common.img import screenshot
from common.raiseout import raiseout
class system():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        #点击系统功能
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[4]/div/i[2]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[4]/ul/li').click()
        sleep(1)

    def add(self,username,beizhu):
        #点击新建
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(username)
        sleep(1)
        #选择运维角色
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #输入备注
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            self.d.close()
            return t
        except Exception as msg:
            print(u"异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()

#创建的运维人员户登录系统
    def login_yw(self,name):
        self.d.find_element_by_css_selector(
            "#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath(
            '//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        # 选择运维角色
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        # 输入备注
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("运维人员")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        sleep(1)
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        pwd=name[-6:]
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        try:
            self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/button').click()
            sleep(2)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/div').text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()

#创建的运营人员户登录系统
    def login_yy(self,name):
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        # 选择运营角色
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        # 输入备注
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("运营人员")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        sleep(1)
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        pwd=name[-6:]
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        try:
            self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/button').click()
            sleep(2)
            m=self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div/ul/li/ul/li').text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def alter(self,name,beizhu):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').click()
        sleep(1)
        #修改用户名
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').clear()
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        #修改角色
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        #修改备注
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        #点击提交
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
        t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
        self.d.close()
        return t

    def select_name(self,name):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]/span').text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:用户不存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def select_juese(self,name):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/input').send_keys(name)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]/span').text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:用户不存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def delete(self):
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]').click()
        try:
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60,1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            self.d.close()
            return m
        except Exception as msg:
            screenshot(self.d, 'yewu')
            raiseout()


if __name__ == '__main__':
    # system().add("asas7ccdd7vc")
    # system().alter("usermame","11")
    # system().select_juese("运营人员")
    system().delete()
    # system().login_yy("ub7llksdb")