# If you want to install the driver automatically, import:
# from webdriver_manager.chrome import ChromeDriverManager
# then define the driver like this:
# driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os
import time
from pythonping import ping

def restart(binary_location,driver_location,password):
    print("Start restarting process")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.binary_location = binary_location

        driver = webdriver.Chrome(driver_location, options=chrome_options)
        driver.delete_cookie("192.168.0.1")
        driver.get("https://192.168.0.1")
        driver.find_element_by_id ("Password").send_keys(password)
        driver.find_element_by_id("LoginBtn").click()
        if driver.find_element_by_id("InvalidMsg").is_displayed():
            print("Wrong password")
            exit()
        if len(driver.find_elements_by_xpath("//input[@type='button' and @value='OK']")) != 0:
            driver.find_elements_by_xpath("//input[@type='button' and @value='OK']")[0].click()
        driver.find_elements_by_xpath("//input[@type='button' and @value='No']")[0].click()
        driver.get("https://192.168.0.1/?status_restart&mid=StatusRestart")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "PAGE_RESTART_RESTART"))
        )
        driver.find_elements_by_xpath("//input[@type='button' and @id='PAGE_RESTART_RESTART']")[0].click()
        driver.find_elements_by_xpath("//input[@type='button' and @id='PAGE_RESTART_POPUP_APPLY']")[0].click()
        print("Restart successfully!")
    finally:
        driver.quit()

def main():
    try:
        response_list = ping("8.8.8.8",timeout=5,count=5)
        if not response_list.success(2):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            config = configparser.ConfigParser()
            config.read(dir_path + '/config.cfg')
            binary_location = config['default']['binary_location']
            driver_location = config['default']['driver_location']
            password        = config['default']['password']
            restart(binary_location,driver_location,password)
        else:
            print("Internet connection is UP. Nothing to do.")
    except (OSError,RuntimeError) as e:
        print(format(e))

if __name__ == "__main__":
    main()