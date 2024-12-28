from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import  load_dotenv
import os
load_dotenv()
def setup_driver():
    options = Options()
    
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def fetch_trends(driver):
    twid = os.getenv('TWID')
    auth_token = os.getenv('AUTH_TOKEN')
    ct0 = os.getenv('CT0')
    driver.get("https://twitter.com")
    cookies = [
        {'name': 'twid', 'value': twid, 'domain': '.x.com'},
        {'name': 'auth_token', 'value': auth_token, 'domain': '.x.com'},
        {'name': 'ct0', 'value': ct0, 'domain': '.x.com'}
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://x.com/explore/tabs/trending")

    try:
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="trend"]'))
        )
        trends = [element.text for element in elements]
        return trends
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


