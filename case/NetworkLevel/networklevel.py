# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
class z_w():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        # 点击数据模版管理
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div'))
        self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div').click()
        sleep(2)
        #点击专网等级模版
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[3]/ul/li[1]').click()
        sleep(1)

    def add01(self,name,ip,port):#手动输入
        #点击添加模版
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        #输入模版名称
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        #选择专网等级
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span').click()
        #选择专网行业
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #选择场景
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[1]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #选择业务
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        # 选择协议
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[2]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        # 输入ip
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[3]/div/div/input').send_keys(ip)
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[4]/div/div/input').send_keys(ip)
        sleep(1)
        # 输入端口号
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[5]/div/div/input').send_keys(port)
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[6]/div/div/input').send_keys(port)
        sleep(1)
        # 输入参数
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[8]/div[1]/div/div/div/input').send_keys('1')
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[8]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[9]/div[1]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[9]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        #API_PCI
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[10]/div[1]/div/div/span[3]/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[10]/div[2]/div/div/span[3]/span').click()
        sleep(1)
        #APR_PL
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[11]/div/div/div/input').send_keys("1")
        sleep(1)
        #点击提交
        try:
            self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            self.d.close()
            return t
        except Exception as msg:
            print(u"异常原因:专网等级模版名称不能重复")
            screenshot(self.d, 'zhuanwang')
            raiseout()


    def add02(self,name):#引用模版
        # 点击添加模版
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form')
        # js1 = "window.scrollTo(0, document.body.scrollHeight)"  # 滑动滚动条到底部
        # self.d.execute_script(js1)
        # sleep(2)
        # # 输入模版名称
        # js2 = "window.scrollTo(0,0)"
        # self.d.execute_script(js2)
        # self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        # sleep(1)
        #点击引用模版
        WebDriverWait(self.d,60,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/button'))
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/button').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[2]/div/div[2]/div/div/div[3]/div[3]/button[1]').click()
        sleep(1)
        # 输入模版名称
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        #选择专网等级
        ele= self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span')
        self.d.execute_script("arguments[0].scrollIntoView(false);", ele)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span').click()
        sleep(1)
        # 选择专网行业
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #选择场景
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[1]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        # 点击提交
        try:
            self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            self.d.close()
            return t
        except Exception as msg:
            screenshot(self.d, 'zhuanwang')
            raiseout()

    def select_1(self,name):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div/button[2]').click()
        sleep(1)
        m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/button[2]/span').text
        self.d.close()
        return m

    def select_2(self):
        #选择行业为船舶--等级L1
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]'))
        self.d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/span/span/i').click()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]'))
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #点击提交
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/span').text
            # if "暂无数据" in m:
            #     print("测试成功,未找到数据")
            # else:
            #     print("测试失败")
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:该元素存在")
            screenshot(self.d, 'zhuanwang')
            raiseout()


    def delete(self):
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]').click()
        sleep(2)
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/button[3]/span'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/button[3]/span').click()
        sleep(1)
        try:
            self.d.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:专网等级模版正在被使用无法删除")
            screenshot(self.d, 'zhuanwang')
            raiseout()



if __name__ == '__main__':
    # z_w().add01("测试一","10.1.1.2","33")
    # z_w().add02("引用测试")
    # z_w().select_2()
    z_w().delete()