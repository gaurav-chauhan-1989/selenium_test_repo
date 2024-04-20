from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.get('http://demo.automationtesting.in/Alerts.html')
driver.maximize_window()

e1=driver.find_element(By.XPATH,"//a[@href='SwitchTo.html']")
e2=driver.find_element(By.XPATH,"//a[@href='Frames.html']")
actions=ActionChains(driver)
actions.move_to_element(e1).move_to_element(e2).click().perform()
driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('Hello')
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[@href='#Multiple']").click()
fm1=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(fm1)
fm2=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(fm2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('Hiiii')
