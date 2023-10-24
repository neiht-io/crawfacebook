import random
import pickle
import  csv
import openpyxl
from infro_raw import object_infor_user_list
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()

#enabled/disabled cookies/notifications/click accept.
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

#chrome to stay open
option.add_experimental_option("detach", True)

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
# 1. Khai bao bien browser
browser  = webdriver.Chrome(options=option)

browser.get("http://facebook.com")

# 2.Load cookie from file

cookies = pickle.load(open("my_cookie.pkl","rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# 3. Refresh the browser
browser.get("http://facebook.com")

sleep(random.randint(1,3))

new_object_info_list = []
# ------------------------------------------

#Lặp qua danh sách các đối tượng trong object_infor_user_list
for obj in object_infor_user_list:
    commenter_url = obj.get("commenter_url", None)  # Lấy URL của commenter từ object

    # Kiểm tra xem có commenter_url trong object hay không
    if commenter_url:
        # Điều hướng đến trang commenter_url
        browser.get(commenter_url)
        sleep(random.randint(1, 3))

        # user_live, user_from, user_gender, và user_birthday từ trang web
         # click vô about
        about = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]")
        about.click()
        sleep(random.randint(1,3))


        naN ="Không xác định" #biến này là giá trị không xác định

        # lấy nơi sống
        try:
            get_live = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/div/span/a/span")
            user_live = get_live.text
        except NoSuchElementException:
            user_live = naN
        sleep(random.randint(1,3))

        #lấy quê quán

        try:
            get_from = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div[2]/div/span/a/span")
            user_from= get_from.text
        except NoSuchElementException:
            user_from = naN
        sleep(random.randint(1,3))


        # click thông tin cơ bản chỗ nay get thêm birthday nữa
        gender_click = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[5]/a")
        gender_click.click()
        sleep(random.randint(1,3))

        #get_gender
        try:
            gender = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]")
            user_gender = gender.text
        except NoSuchElementException:
            user_gender = naN
        sleep(random.randint(1,3))

        #get_birthday
        try:
            birthday = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[4]/div/div/div[2]/div/div/div/div/div[1]")
            user_birthday = birthday.text
        except NoSuchElementException:
            user_birthday = naN
        sleep(random.randint(1,3))

        new_obj = {
            "comment_id": obj["comment_id"],
            "commenter_name": obj["commenter_name"],
            "commenter_url": obj["commenter_url"],
            "user_live": user_live,
            "user_from": user_from,
            "user_gender": user_gender,
            "user_birthday": user_birthday
        }

        # Thêm dictionary mới vào danh sách new_object_info_list
        new_object_info_list.append(new_obj)

        sleep(random.randint(1, 3))

browser.close()

for a in new_object_info_list:
    print(a)

