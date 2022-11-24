from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random

options = webdriver.ChromeOptions()


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




def start(login, ps):
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options,
    )

    driver.get('https://web.leber11.com/login/?redirect_after_login=/')
    
    
    driver.set_window_size(974, 1040)
    driver.find_element(By.ID, "mobile_number").click()
    driver.find_element(By.ID, "mobile_number").send_keys(login)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(ps)
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "(//a[contains(text(),\'体温チェック\')])[3]").click()
    driver.find_element(By.LINK_TEXT, "体温チェック").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0")
    dropdown.find_element(By.XPATH, random.choice(l)).click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0")
    dropdown.find_element(By.XPATH, "//option[. = '07:00']").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.LINK_TEXT, "良い").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.LINK_TEXT, "休日").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, ".col-12 > .list-unstyled").click()
    driver.find_element(By.LINK_TEXT, "いない").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()
    time.sleep(3)
    driver.close()

def start1(login, ps):
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options,
    )

    driver.get('https://web.leber11.com/login/?redirect_after_login=/')

    driver.set_window_size(974, 1040)
    driver.find_element(By.ID, "mobile_number").click()
    driver.find_element(By.ID, "mobile_number").send_keys(login)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(ps)
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "(//a[contains(text(),\'体温チェック\')])[3]").click()
    driver.find_element(By.LINK_TEXT, "体温チェック").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0")
    dropdown.find_element(By.XPATH, random.choice(l)).click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-0")
    dropdown.find_element(By.XPATH, "//option[. = '07:00']").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.LINK_TEXT, "良い").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.LINK_TEXT, "出席する").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, ".col-12 > .list-unstyled").click()
    driver.find_element(By.LINK_TEXT, "いない").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-1mg04hm-9").click()
    driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()
    time.sleep(3)
    driver.close()
