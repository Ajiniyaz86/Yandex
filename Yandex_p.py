from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://passport.yandex.ru/')

search_box=driver.find_element_by_id('passp-field-login')
search_box.send_keys('y4ndexx-test')
search_box.submit()
time.sleep(3)

search_box2=driver.find_element_by_id('passp-field-passwd')
search_box2.send_keys('!@34QWer')
search_box2.submit()
time.sleep(10)

driver.quit