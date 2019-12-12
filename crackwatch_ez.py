import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

home = str(Path.home()) + '\desktop'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--log-level=3')

driver = webdriver.Chrome(resource_path('./chromeDriver/chromedriver.exe'), options=options)#
driver.get('https://crackwatch.com/game/call-of-duty-modern-warfare/comments?comment=GccarQRCfE8QZywqR')

time.sleep(5)

driver.find_element_by_class_name('overlay-close').click() 
driver.execute_script('window.scrollTo(0, 0)')
driver.find_element_by_class_name('announcement-close').click()
driver.get_screenshot_as_file(home + '\main-page.png')

driver.quit()