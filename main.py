from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome("/Path/to/chromedriver", options=chrome_options)
    driver.delete_cookie("192.168.0.1")
    driver.get("https://192.168.0.1")
    driver.find_element_by_id ("Password").send_keys("yourpassword")
    driver.find_element_by_id("LoginBtn").click()
    if len(driver.find_elements_by_xpath("//input[@type='button' and @value='OK']")) != 0:
        driver.find_elements_by_xpath("//input[@type='button' and @value='OK']")[0].click()
    driver.find_elements_by_xpath("//input[@type='button' and @value='No']")[0].click()
    driver.get("https://192.168.0.1/?status_restart&mid=StatusRestart")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PAGE_RESTART_RESTART"))
    )
    driver.find_elements_by_xpath("//input[@type='button' and @id='PAGE_RESTART_RESTART']")[0].click()
    # driver.find_elements_by_xpath("//input[@type='button' and @id='PAGE_RESTART_POPUP_APPLY']")[0].click()

    time.sleep(3)
finally:
    driver.quit()