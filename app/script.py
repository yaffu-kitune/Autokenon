from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

l = (
    "//option[. = '36.0°C']",
    "//option[. = '36.1°C']",
    "//option[. = '36.2°C']",
    "//option[. = '36.3°C']",
    "//option[. = '36.4°C']",
    "//option[. = '36.5°C']",
    "//option[. = '36.6°C']",
    "//option[. = '36.7°C']",
    )




def start(login, ps, week):
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
    command_executor='https://selenium.yaffugit.net/wd/hub',
    options=chrome_options
    )


    if week == True:
        switch = ".css-1dbjc4n:nth-child(4) > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-901oao"
    elif week == False:
        switch = ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-901oao"


    driver.implicitly_wait(10)

    driver.get("https://web.leber.jp/")
    driver.set_window_size(1936, 1048)
    driver.find_element(By.CSS_SELECTOR, ".r-jwli3a").click()
    driver.find_element(By.CSS_SELECTOR, ".css-11aywtz").click()
    driver.find_element(By.CSS_SELECTOR, ".css-11aywtz").send_keys(login)
    driver.find_element(By.CSS_SELECTOR, ".r-nsiyw1").click()
    driver.find_element(By.CSS_SELECTOR, ".r-1awozwy > .css-11aywtz").click()
    driver.find_element(By.CSS_SELECTOR, ".r-1awozwy > .css-11aywtz").send_keys(ps)
    driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n > .css-901oao").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(2) > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n:nth-child(2) > .css-1dbjc4n:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".r-1b43r93").click()
    driver.find_element(By.CSS_SELECTOR, ".r-1ff274t").click()
    driver.find_element(By.CSS_SELECTOR, ".r-ku1wi2:nth-child(1)").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".r-ku1wi2:nth-child(1)")
    dropdown.find_element(By.XPATH, random.choice(l)).click()
    driver.find_element(By.CSS_SELECTOR, ".r-1loqt21 > .r-x9px8g").click()
    driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(2) > .css-1dbjc4n:nth-child(2) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(2) > .css-901oao:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".r-ku1wi2:nth-child(1)").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".r-ku1wi2:nth-child(1)")
    dropdown.find_element(By.XPATH, "//option[. = '07:00']").click()
    driver.find_element(By.CSS_SELECTOR, ".r-1loqt21 > .r-x9px8g").click()
    driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-901oao").click()
    driver.find_element(By.CSS_SELECTOR, ".r-y47klf").click()
    driver.find_element(By.CSS_SELECTOR, switch).click()
    driver.find_element(By.CSS_SELECTOR, ".r-y47klf").click()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-901oao").click()
    driver.find_element(By.CSS_SELECTOR, ".r-y47klf").click()
    driver.find_element(By.CSS_SELECTOR, ".r-37igu").click()
    driver.find_element(By.CSS_SELECTOR, ".r-14lw9ot > .r-10jnvle").click()
    driver.close()