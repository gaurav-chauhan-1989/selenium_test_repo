import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('E:\Selenium\chromedriver.exe')
driver.get('https://www.techlistic.com/p/demo-selenium-practice.html')
driver.maximize_window()
driver.implicitly_wait(10)
rows = len(driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr"))
col = len(driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td"))
l = []
for i in range(2,rows+1):
    for j in range(1, col+1):
        a = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr["+str(i)+"]/td["+str(j)+"]")
        l.append(a.text)
print(l)
driver.close()





