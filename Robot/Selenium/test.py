from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

s = Service('E:\Selenium\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.XPATH("//"))))
e1 = driver.find_element(By.ID, 'A1')
e2 = driver.find_element(By.XPATH, "//div[@id='x1']")
Actions = ActionChains(driver)
Actions.context_click(e1)
Actions.move_to_element(e1).click().perform()
Actions.drag_and_drop(e1, e2).perform()
Actions.double_click(e1).perform()
driver.execute_script("arguments[0].scrollIntoView();", e1)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
parent = driver.current_window_handle
s = driver.window_handles
for i in s:
    if i != parent:
        driver.switch_to.window(i)

driver.switch_to.window(parent)
