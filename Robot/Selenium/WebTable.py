from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get('http://demo.automationtesting.in/WebTable.html')
driver.implicitly_wait(10)

try:
    rows=len(driver.find_elements(By.XPATH,"//div[@class='ui-grid-row ng-scope']"))                        # Get no. of rows
    print(rows)
    cols=len(driver.find_elements(By.XPATH,"//div[@class='ui-grid-cell-contents ng-binding ng-scope']"))
    cols=int(cols/rows)                                                            # Convert to integer     # Get no. of column in a row
    print(cols)
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            data=driver.find_element(By.XPATH,"//Div[@class='ui-grid-canvas']/div["+str(r)+"]/div[1]/div["+str(c)+"]").text
            print(data, end="    ")
        print( )

finally:
    driver.close()





