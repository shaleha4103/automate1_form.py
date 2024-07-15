from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = webdriver.Chrome()

web.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')
web.maximize_window()
time.sleep(5)

full_name = 'Shaleha Khan'
contact_number = '9321534350'
email_address = 'shaleha.kjhan22@comp.sce.edu.in''i
address = 'New Gautam Nagar, near sunni bareli masjid Govandi'
pin_code = '400043'
date_of_birth = '04/10/2003'
gender = 'Female'
verification_code = 'GNFPYC'

name = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(full_name)

cnumber = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
cnumber.send_keys(contact_number)

email_elem = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_elem.send_keys(email_address)

add = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
add.send_keys(address)

pcode = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pcode.send_keys(pin_code)

dob = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
dob.send_keys(date_of_birth)

gen = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gen.send_keys(gender)

vcode = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
vcode.send_keys(verification_code)

submit = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit.click()

try:

    confirmation_message = WebDriverWait(web, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Thank you")]'))
    )
    print("Form submitted successfully and confirmation message appeared.")
except:
    print("Form submission failed or confirmation message did not appear.")

web.quit()
