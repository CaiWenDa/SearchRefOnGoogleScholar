from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import TimeoutException
import time
from browser_client import BrowserClient

def fetch_citation(title: str, browser, index: int):
    url = f"https://scholar.google.com/scholar?oi=gsb95&q={title}&lookup=0&hl=zh-CN"
    try:
        browser.get(url)
        browser.wait_for_element(By.CLASS_NAME, "gs_or_cit")
        browser.driver.find_element(By.CLASS_NAME, "gs_or_cit").click()
        browser.wait_for_element(By.CLASS_NAME, "gs_citr")
        cite = browser.driver.find_element(By.CLASS_NAME, "gs_citr").text
        return f'[{index}] ' + cite + '\n'
    except TimeoutException as timeout_err:
        print(f'[{index}] 超时错误，检查网络连接或者是否需要人机验证')
        raise timeout_err # 终止主程序
    except InvalidSessionIdException as window_err:
        print(f'[{index}] 找不到会话，检查浏览器是否被关闭')
        raise window_err # 终止主程序
    except Exception as err:
        print(f'[{index}]', err)
        return f'[{index}] ' + title.strip() + '***ERROR***\n'

def main():
    browser = BrowserClient('chrome')
    try:
        with open("ref_titels.txt", "rt") as files, open("saved_cites.txt", "wt", encoding='utf-8') as cite_file:
            for i, line in enumerate(files, 1):
                result = fetch_citation(line.strip(), browser, i)
                cite_file.write(result)
                time.sleep(3)
    except Exception as e:
        print("异常信息:", e)
    finally:
        browser.close()

if __name__ == "__main__":
    main()
