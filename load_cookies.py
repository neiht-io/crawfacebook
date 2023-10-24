import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# 0. Declare the browser
browser = webdriver.Chrome()

# 1. Open faceboook
browser.get("http://facebook.com")

# 2. Truy to login


txtUser = browser.find_element(By.ID,"email")
txtUser.send_keys("mapca0429@gmail.com.") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element(By.ID,"pass")
txtPass.send_keys("Câmp0429")

txtPass.send_keys(Keys.ENTER)

sleep(3)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl","wb"))

browser.close()