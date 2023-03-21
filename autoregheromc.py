import random #line:1:import random
import getpass #line:2:import getpass
import os #line:3:import os
import string #line:4:import string
from selenium import webdriver #line:5:from selenium import webdriver
from selenium .webdriver .common .keys import Keys #line:6:from selenium.webdriver.common.keys import Keys
from selenium .webdriver .common .by import By #line:7:from selenium.webdriver.common.by import By
from selenium .webdriver .common .action_chains import ActionChains #line:8:from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver .chrome .options import Options #line:9:from selenium.webdriver.chrome.options import Options
from os import path #line:10:from os import path
from json import load #line:11:from json import load
import time #line:12:import time
class Data :#line:14:class Data:
    def __init__ (OO0O0O0OO00O00OOO ):#line:16:def __init__(self):
        OO0O0O0OO00O00OOO .CONFIG_PATH =("settings.json"if path .exists ("settings.json")else input (">> Nhập tệp tin chứa thông tin (Có dạng .json): "))#line:21:)
        OO0O0O0OO00O00OOO .loader ()#line:22:self.loader()
    def loader (O0OO000OO00000OO0 ):#line:24:def loader(self):
        print (">> Đang tải tập tin...")#line:25:print(">> Đang tải tập tin...")
        with open (O0OO000OO00000OO0 .CONFIG_PATH ,"r")as OO00OOOO00O000OOO :#line:26:with open(self.CONFIG_PATH, "r") as file:
            OO0O00OOO000O0000 =load (OO00OOOO00O000OOO )#line:27:data = load(file)
            O0OO000OO00000OO0 .user =OO0O00OOO000O0000 ["user"]#line:28:self.user = data["user"]
            O0OO000OO00000OO0 .passwords =OO0O00OOO000O0000 ["password"]#line:29:self.passwords = data["password"]
characters =string .ascii_letters +string .digits #line:33:characters = string.ascii_letters + string.digits
username_length =random .randint (4 ,8 )#line:36:username_length = random.randint(4, 8)
username =''.join (random .choice (characters )for OO0OO0O0000O0OO00 in range (username_length ))#line:37:username = ''.join(random.choice(characters) for i in range(username_length))
email_length =random .randint (8 ,20 )#line:40:email_length = random.randint(8, 20)
email =''.join (random .choice (string .ascii_lowercase )for OO0000O00O0000O0O in range (email_length ))+'@gmail.com'#line:41:email = ''.join(random.choice(string.ascii_lowercase) for i in range(email_length)) + '@gmail.com'
password =Data ().passwords #line:44:password = Data().passwords
print (">> Open browser")#line:47:print(">> Open browser")
options =webdriver .ChromeOptions ()#line:48:options = webdriver.ChromeOptions()
options .add_extension ('.\Recaptcha.crx')#line:49:options.add_extension('.\Recaptcha.crx')
options .add_experimental_option ('excludeSwitches',['enable-logging'])#line:50:options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver =webdriver .Chrome (options =options )#line:51:driver = webdriver.Chrome(options=options)
driver .get ('https://id.heromc.net/member/dangky.php');#line:54:driver.get('https://id.heromc.net/member/dangky.php');
print (">> nigga")#line:57:print(">> nigga")
username_field =driver .find_element (By .NAME ,'User_name');#line:58:username_field = driver.find_element(By.NAME, 'User_name');
username_field .send_keys (username )#line:59:username_field.send_keys(username)
email_field =driver .find_element (By .NAME ,'User_email');#line:61:email_field = driver.find_element(By.NAME, 'User_email');
email_field .send_keys (email )#line:62:email_field.send_keys(email)
password_1 =driver .find_element (By .NAME ,'User_password');#line:64:password_1 = driver.find_element(By.NAME, 'User_password');
password_1 .send_keys (password )#line:65:password_1.send_keys(password)
password_2 =driver .find_element (By .NAME ,'User_repeatPassword');#line:67:password_2 = driver.find_element(By.NAME, 'User_repeatPassword');
password_2 .send_keys (password )#line:68:password_2.send_keys(password)
captcha_frame =driver .find_element (By .XPATH ,'//iframe[contains(@src, "recaptcha")]')#line:71:captcha_frame = driver.find_element(By.XPATH, '//iframe[contains(@src, "recaptcha")]')
driver .switch_to .frame (captcha_frame )#line:72:driver.switch_to.frame(captcha_frame)
captcha_checkbox =driver .find_element (By .XPATH ,'//div[@class="recaptcha-checkbox-border"]')#line:74:captcha_checkbox = driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
action =webdriver .common .action_chains .ActionChains (driver )#line:75:action = webdriver.common.action_chains.ActionChains(driver)
action .move_to_element (captcha_checkbox ).click ().perform ()#line:76:action.move_to_element(captcha_checkbox).click().perform()
time .sleep (3 )#line:77:time.sleep(3)
getpass .getpass (">> Hãy giải captcha và bấm enter")#line:80:getpass.getpass(">> Hãy giải captcha và bấm enter")
driver .switch_to .default_content ()#line:83:driver.switch_to.default_content()
dangky_button =driver .find_element (By .ID ,'dangky')#line:84:dangky_button = driver.find_element(By.ID, 'dangky')
dangky_button .click ()#line:85:dangky_button.click()
time .sleep (3 )#line:86:time.sleep(3)
driver .quit ()#line:89:driver.quit()
print (">> Đang lưu thông tin vào file Accounts.txt...")#line:92:print(">> Đang lưu thông tin vào file Accounts.txt...")
with open ('Accounts.txt','w')as f :#line:93:with open('Accounts.txt', 'w') as f:
    f .write ('Username: '+username +' '+'Password: '+str (password ))#line:94:f.write('Username: ' + username + ' ' + 'Password: ' + str(password))
    print (">> Tạo tài khoản thành công! Tài khoản được lưu trong file Accounts.txt!")
