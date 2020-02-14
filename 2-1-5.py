from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    text_area = browser.find_element_by_id("answer")
    text_area.send_keys(y)
    
    robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot.click()
    
    robot_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robot_rule.click()
    
    browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла