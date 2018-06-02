from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#open browser
driver = webdriver.Firefox()

#go to gmail
driver.get('https://mail.google.com')
body = driver.find_element_by_id('identifierId').send_keys('youremail@gmail.com')
python_button = driver.find_element_by_id('identifierNext')
python_button.click()
time.sleep(1)
driver.find_element_by_name('password').send_keys('yourpassword')
python_button = driver.find_element_by_id('passwordNext')
python_button.click()

