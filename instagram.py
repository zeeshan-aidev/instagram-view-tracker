from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


def open_reels(driver, url):
    driver.get(url)

    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.TAG_NAME,"body"))
    )

    time.sleep(3)


def scroll_to_bottom(driver):

    last = 0

    while True:

        driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);"
        )

        time.sleep(2)

        reels = driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/reel/')]"
        )

        if len(reels)==last:
            break

        last=len(reels)


def count_reels(driver):

    reels = driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'/reel/')]"
    )

    return len(reels)


def convert_number(text):

    text=text.replace(",","").strip().upper()

    if text.endswith("K"):
        return int(float(text[:-1])*1000)

    if text.endswith("M"):
        return int(float(text[:-1])*1000000)

    return int(float(text))


def get_total_views(driver):

    total=0

    values=[]

    spans=driver.find_elements(
        By.XPATH,
        "//span"
    )

    for span in spans:

        text=span.text.strip()

        if not text:
            continue

        if re.fullmatch(r"\d+(\.\d+)?[KM]?",text):

            values.append(text)

    for value in values:

        total+=convert_number(value)

    return total