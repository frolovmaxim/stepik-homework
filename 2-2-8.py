from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_name("firstname").send_keys("Maxim")
    
    browser.find_element_by_name("lastname").send_keys("Frolov")
   
    browser.find_element_by_name("email").send_keys("dfydfgh@drfgdfg.gg")
    
    #current_dir = os.path.abspath(os.path.dirname(__file__))    
    #file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_id("file").send_keys("C://file.txt")
    
    
    
    browser.find_element_by_tag_name("button").click()
    
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла