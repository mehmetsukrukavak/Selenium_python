from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pypi.org/")
print(driver.title)
find_element = driver.find_element(By.NAME, "q")
find_element.send_keys("selenium")
find_element.send_keys(Keys.RETURN)
elemment = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[3]/div/p")
print(elemment.text)


print(driver.page_source)