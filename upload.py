from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:8080")

driver = webdriver.Chrome(options=option)

time.sleep(3)

driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")

time.sleep(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys("St. Philomena's High School, Kengeri") #replace with which you want to do auto photo upload
search_box.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[19]/div/button').click() #click on add photos button

time.sleep(9)

driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\yashw\Desktop\new\photos\childhood.jpg") #replace with your path

time.sleep(4)
