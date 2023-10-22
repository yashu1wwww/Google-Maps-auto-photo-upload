from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import random
import os

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
time.sleep(4)
driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")
time.sleep(4)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("oxford school melbourne") #replace with your search place
search_box.send_keys(Keys.RETURN)

time.sleep(6)

driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[19]/div/button').click() #click on add photos button

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[7]/div[2]/div/iframe"))) 

time.sleep(4)

driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\yashw\Desktop\new\photos\childhood.jpg") #replace with your photo path

time.sleep(4)

