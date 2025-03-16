from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(2)

driver.switch_to.frame("iframeResult")
time.sleep(2)

content = driver.find_element(By.TAG_NAME, "p")
print("Contenido del frame:", content.text)
time.sleep(2)

driver.switch_to.default_content()
time.sleep(2)
driver.quit()