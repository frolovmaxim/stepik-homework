from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    
    x_element1 = browser.find_element_by_id("num2")
    x1 = int(x_element1.text)
    
    y = x + x1
    y = str(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)
    
    browser.find_element_by_tag_name("button").click()
    
    
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла