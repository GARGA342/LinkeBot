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

input()

elem = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[2]')
elem.click()

sleep(4)
driver.execute_script("window.scrollTo(0, 2000);")