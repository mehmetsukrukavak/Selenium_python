from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
'''
driver.get("https://google.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))

input_element = driver.find_element(By.NAME, "q")
input_element.send_keys(".net 8")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))
button_element = driver.find_element(By.NAME, "btnK")
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))

button_element.click()
'''
driver.get("https://atilsamancioglu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")

blog_page.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
read_Button = driver.find_element(By.CLASS_NAME, "button")
read_Button.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID, "archives-2")))
article_list = driver.find_element(By.ID, "archives-2")
print(len(article_list.text.splitlines()))
