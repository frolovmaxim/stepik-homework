from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_tag_name("button").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x1 = browser.find_element_by_id("input_value").text
    y = calc(int(x1))
    
    browser.find_element_by_id("answer").send_keys(y)
    
    browser.find_element_by_tag_name("button").click()
    
    
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла