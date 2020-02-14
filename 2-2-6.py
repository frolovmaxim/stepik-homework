from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x1 = int(x_element.text)
    
    p = calc(x1)
    
    line1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", line1)
    line1.send_keys(p)
    
    browser.find_element_by_id("robotCheckbox").click()
    
    browser.find_element_by_id("robotsRule").click()
   
    
    browser.find_element_by_tag_name("button").click()
    
    
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла