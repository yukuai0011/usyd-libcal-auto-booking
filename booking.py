from zmq import CHANNEL
from playwright.sync_api import sync_playwright

import os

import pyotp

UNIKEY = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOPT_CODE = os.getenv("TOPT_CODE")

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False, CHANNEL="msedge-beta")
        page = browser.new_page()

        no_error = False

        while not no_error:
            try:
                page.goto("https://sso.sydney.edu.au")
                # click button based on Xpath
                page.locator(
                    "/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input"
                ).first.fill(UNIKEY)
                page.locator(
                    "/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input"
                ).first.fill(PASSWORD)
                page.locator(
                    "/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div/span/div/label"
                ).click()
                page.wait_for_timeout(1000)
                page.locator(
                    "/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a"
                ).click()
                page.wait_for_timeout(1000)
                # calculate totp
                totp = pyotp.TOTP(TOPT_CODE)
                page.locator(
                    "/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input"
                ).first.fill(totp.now())

                no_error = True
            except Exception as e:
                pass

        browser.close()