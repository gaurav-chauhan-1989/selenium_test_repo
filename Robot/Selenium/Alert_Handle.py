from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path='E:\Selenium\chromedriver.exe')
driver.get('http://demo.automationtesting.in/Alerts.html')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@class='btn btn-danger']").click()
alert=driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@class='btn btn-info']").click()
time.sleep(1)
alert=driver.switch_to.alert
alert.dismiss()
