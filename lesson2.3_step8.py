from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
message = browser.find_element_by_id("book").click()

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element  =  browser.find_element_by_id("input_value")
x = x_element.text

input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))

option1 = browser.find_element_by_css_selector("[type='submit']").click()