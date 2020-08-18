from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import random
from selenium.webdriver.support.ui import Select


print("Made By Krazy")
n = int(input("Enter Number of Email You Need: "))

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)


driver.get("https://getnada.com/")
sleep(5)

i = 0

while i < n:
    html = driver.page_source
    soup = BeautifulSoup(html, "html5lib")
    mail = soup.find("span", {"class" : "address what_to_copy"})

    with open("Emails.txt", "a") as f:
        f.write(mail.get_text() + '\n')
        f.close()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add Inbox')]"))).click()
    sleep(2)
    element = Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='domain']"))))
    element.select_by_index(random.randint(0, 11))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[1]/footer/a[2]"))).click()
    sleep(3)
    i += 1
