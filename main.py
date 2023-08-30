from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

options =  webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver,timeout=5)

driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

driver.implicitly_wait(10)
driver.find_element(By.ID,"langSelect-EN").click()
driver.implicitly_wait(10)
cookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")
items = [driver.find_element(By.ID,"product"+str(i)) for i in range(1,-1,-1)] 


for i in range(5000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split()[0])
    for item in items:
        value = int(item.text.split()[1])
        if value <=count:
            upgrade = ActionChains(driver)
            upgrade.move_to_element(item)
            upgrade.click()
            upgrade.perform()


