from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button = browser.find_element_by_id('book').click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element_by_id('input_value').text
answer = browser.find_element_by_id('answer').send_keys(calc(x))
submit = browser.find_element_by_id('solve').click()
