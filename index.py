from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Chose driver to browse
driver = webdriver.Firefox(executable_path='/home/garga/Projects/Python/LinkeBot/geckodriver')

#Open website
driver.get("https://br.linkedin.com/")
sleep(2)

#Confirm Title
assert "LinkedIn" in driver.title

#Wait login by user (input email and password, click login button and set "enter" in terminal)
input()

#Find element and click
elem = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[2]')
elem.click()

#Wait 4 seconds and scroll page
sleep(4)
driver.execute_script("window.scrollTo(0, 2300);")

#Wait 2 seconds and repeatedly click the "connect" button
sleep(2)
while(True):
    elem = driver.find_element(By.XPATH, '//*[@id="ember482"]')
    elem.click()
    sleep(1)