from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
class z_d():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        # 点击运维管理
        # WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/div'))
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/div').click()
        # sleep(2)
        # 点击终端用户
        WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[2]').click()

    def add(self,phone,im,beizhu):
        #点击添加用户
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(2)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(phone)
        sleep(2)
        #输入IMSI
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys(im)
        sleep(1)
        # 选择所属专网华西
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        #选择场景手术
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #选择业务
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        #输入备注
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        #点击提交
        try:
            self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span").click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            self.d.close()
        except Exception as msg:
            print(u"异常原因:终端用户手机号不能重复")
            screenshot(self.d, 'zhongduan')
            raise
        else:
            return t

    def alter(self):
        #点击编辑默认修改列表第一条数据
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.table-pagination > div.el-table.el-table--fit.el-table--striped.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_2_column_18 > div > button:nth-child(1)"))
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.table-pagination > div.el-table.el-table--fit.el-table--striped.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_2_column_18 > div > button:nth-child(1)").click()
        sleep(1)
        #修改IMSI
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys("1111")
        sleep(1)
        #修改备注
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/textarea').send_keys("22")
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            self.d.close()
            return t
        except Exception as msg:
            screenshot(self.d, 'zhongduan')
            raise

    def select(self):
        #查询终端用户[手机号]
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys("18899991111")
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[6]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]').text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:未找到该元素")
            screenshot(self.d, 'zhongduan')
            raise msg

    def pladd(self):
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div').click()
        sleep(1)
        #下载模版
        try:
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/form/div[1]/a').text
            self.d.close()
        except Exception as msg:
            screenshot(self.d, 'zhongduan')
            raise msg
        else:
            return m

    def pldaoru(self,wenjian):
        #点击批量导入
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span').click()
        sleep(1)
        self.d.find_element_by_name("file").send_keys(wenjian)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div/div[3]/div/button[1]').click()
            sleep(2)
            WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_css_selector("body > div.el-message.el-message--success"))
            m=self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            print(m)
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:终端用户手机号不能重复")
            screenshot(self.d, 'zhongduan')
            raise

    def delete(self):#默认删除第一个元素
        WebDriverWait(self.d, 30, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]').click()
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span'))
        self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
        #确认删除
        try:
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            self.d.close()
            return m
        except Exception as msg:
            print(u"异常原因:无法删除")
            screenshot(self.d, 'zhongduan')
            raise

    def betch_delete(self):
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span'))
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span[1]').click()
        sleep(1)
        #点击确认删除
        self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_css_selector('.el-message'))
        m=self.d.find_element_by_css_selector('.el-message').text
        print(m)
        if "成功" in m:
            print("success")
        else:
            print("fail")


if __name__ == '__main__':
    # z_d().add("13399991111","9999","11")
    # z_d().alter()
    # z_d().pldaoru()
    # z_d().pladd()r
    z_d().betch_delete()