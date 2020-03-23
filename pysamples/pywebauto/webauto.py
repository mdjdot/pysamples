"""
https://www.selenium.dev/documentation/en/
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(10)
    input = driver.find_element_by_id('kw')
    input.send_keys('selenium')
    query = driver.find_element_by_id('su')
    query.click()
    # wait = WebDriverWait(driver=driver, timeout=10)
    # wait.until(driver.find_element_by_id('page'))
    driver.save_screenshot('1.png')
    
    driver.execute_script('window.scrollTo(100,400)')
    
    time.sleep(5)
    driver.quit()
    
    


