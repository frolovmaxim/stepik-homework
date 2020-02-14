from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    
    browser.find_element_by_id("book").click()
    
    
    x1 = browser.find_element_by_id("input_value").text
    y = calc(int(x1))
    
    browser.find_element_by_id("answer").send_keys(y)
    
    browser.find_element_by_id("solve").click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла