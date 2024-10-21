from amazoncaptcha import AmazonCaptcha  # library that converts the captcha to text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=r'C:\Users\anshc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.amazon.com/errors/validateCaptcha')

soup1 = BeautifulSoup(driver.page_source, "html.parser")
link = soup1.find('img')['src']

input_box = driver.find_element_by_id(("captchacharacters"))

while True:  # using while so that if the captcha appears again the code will be repeated
    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()  # getting the solution of the captcha in text format
    input_box.send_keys(solution)  # input the solution to the textbox
    time.sleep(2)
    input_box.send_keys(Keys.ENTER)  # press the submit key
    try:
        input_box = driver.find_element_by_id(("captchacharacters")) # checking whether we are in the captcha page 
    except:
        break   # if we are not in the captcha page then break
    
time.sleep(10)
driver.close()