from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
import time
# 浏览器设置
executable_paths=r".\chromedriver.exe"
service = webdriver.ChromeService(executable_path=executable_paths)
option = webdriver.ChromeOptions()
# 添加保持登录的数据路径：安装目录一般在 %userprofile%\AppData\Local\Google\Chrome\User Data
option.add_argument(r"user-data-dir=C:\Users\Alison\AppData\Local\Google\Chrome\Selenium Data")
option.add_argument('--ignore-certificate-errors') 
option.add_argument('--ignore-ssl-errors')
# 初始化driver
driver = webdriver.Chrome(service=service)
# 最大化窗口（默认不是最大化）
driver.maximize_window()

with open("Ref_Titel.txt", "rt") as files:
    with open("cite3.txt", "wt", encoding='utf-8') as cite_file:
        i = 0
        for line in files:
            # print(line) line 结尾有\n
            # 设置浏览器需要打开的url
            # url = "https://scholar.lanfanshu.cn/scholar?hl=zh-CN&as_sdt=0%2C5&q=" + line + "&btnG="
            url = "https://scholar.google.com/scholar?oi=gsb95&q=" + line + "&lookup=0&hl=zh-CN"
            i += 1
            try:
                # 发送请求
                time.sleep(3)
                driver.get(url)
                # 定位浏览器窗口中元素
                driver.find_element(By.CLASS_NAME, "gs_or_cit").click()
                # 因为 gs_citr 在点击 gs_or_cit 后就被创建，但是里面的内容还没有生成
                # 所以必须添加一个可见的判断 ().is_displayed() 或 ().text != ''
                # 或其他写法 .until(().text) .until_not(().text != '') .until_not(().not_displayed)
                # until 返回值是它里面函数的返回值
                # 等待，直到 until() 内的条件为真才继续执行后面的代码
                el = WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CLASS_NAME, "gs_citr").is_displayed(), line)
                cite = driver.find_element(By.CLASS_NAME, "gs_citr").text
                cite_file.write('[%d] ' % i + cite + '\n')
                # print(not not cite, el)
            except Exception as err:
                print('[{}] '.format(i), err)
                cite_file.write('[%d] ' % i + line + '***ERROR***' + '\n')
                continue
