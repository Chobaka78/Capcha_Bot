#/
# Bot.py
# Usman Farooqi
# Sept, 27, 2020
#/
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe" # Location of the driver on local c drive (change to your pc)

driver = webdriver.Chrome(PATH)
driver.get("https:google.com") # Link to th website that is going to be controlled by the bot 
print(driver.title)
driver.quit()