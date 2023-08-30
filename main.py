from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

options =  webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver,timeout=5)

driver.get("https://www.wikipedia.org")
print(driver.title)

search = driver.find_element(By.ID,'searchInput')
wait.until(lambda d:search.is_displayed())
search.send_keys("modi")
search.send_keys(Keys.RETURN)
list = driver.find_element(By.ID,"mw-panel-toc-list")
wait.until(lambda d:list.is_displayed())
print(list.text)
""" driver.quit() """


