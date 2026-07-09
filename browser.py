from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import CHROME_PATH, USER_DATA


def start_browser():

    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_PATH

    options.add_argument(f"--user-data-dir={USER_DATA}")

    options.add_argument("--start-maximized")

    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.execute_script("""
        Object.defineProperty(navigator,'webdriver',{
            get:()=>undefined
        })
    """)

    return driver