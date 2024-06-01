from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())


def download_files_from_directory(url : str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    actions = ActionChains(driver)
    driver.get(url)  
    directories = driver.find_elements(By.XPATH,"//div[@class='filename']//a")
    for directory in directories:
        actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        time.sleep(2)
    driver.close()
    for window in driver.window_handles:
        driver.switch_to.window(window)
        links = driver.find_elements(By.XPATH, "//a[contains(title, 'Download')]")
        for link in links:
            link.click()
            time.sleep(2)
        time.sleep(3)
    driver.quit()
