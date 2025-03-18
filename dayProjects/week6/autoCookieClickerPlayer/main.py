from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookies_label = driver.find_element(By.ID, value="money")
cookies = 0
cookie_button = driver.find_element(By.ID, value="cookie")

bot_continue = True

while bot_continue:
    for i in range(100):
        start_time = time.time()
        while True:
            cookie_button.click()
            passed_time = time.time() - start_time
            if passed_time >= 2:
                break
        cookies = int(cookies_label.text.replace(",", ""))
        purchaseable_buttons = []
        try:
            purchases = [int(cost.text.split()[-1].replace(",", "")) <= cookies for cost in driver.find_elements(By.CSS_SELECTOR, value="#store div b") if len(cost.text.split()) > 0]
            if purchases.__contains__(True):
                last_index = 0
                if purchases.count(True) > 1:
                    for _ in range(purchases.count(True) - 1):
                        last_index = purchases.index(True, last_index + 1)
                try:
                    buy_buttons = [item for item in driver.find_elements(By.CSS_SELECTOR, value="#store div") if item.get_attribute("class") != "amount"]
                    buy_buttons[last_index].click()
                except StaleElementReferenceException:
                    print("Stale Buy Button")
                    continue
        except StaleElementReferenceException:
            print("Stale Costs")
            continue
    cookies_per_second = 0
    try:
        cookies_per_second = driver.find_element(By.ID, value="cps").text.split()[-1]
    except StaleElementReferenceException:
        cookies_per_second = driver.find_element(By.ID, value="cps").text.split()[-1]
    if input(f"Should the bot continue? Current cookies/s: {cookies_per_second}. (Y/N): ").lower() != "y":
        bot_continue = False

driver.close()
driver.quit()