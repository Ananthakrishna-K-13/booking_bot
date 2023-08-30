""" import os
os.environ['PATH']+=r"path_to_browserDriver" """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://uitestingplayground.com/")
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT,"Progress Bar").click()
driver.find_element(By.ID,"startButton").click()
print(driver.find_element(By.ID,"progressBar").text)

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element((By.ID,"progressBar"),"75%")
)
driver.find_element(By.ID,"stopButton").click()
