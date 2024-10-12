import os

import pyotp
from playwright.sync_api import sync_playwright

UNIKEY = os.getenv("UNIKEY")
UNI_PASSWORD = os.getenv("UNI_PASSWORD")
UNI_TOPT_CODE = os.getenv("UNI_TOPT_CODE")

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()

        no_error = False

        while not no_error:
            try:
                page.goto("https://sso.sydney.edu.au")
                # click button based on Xpath
                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input"
                ).first.fill(UNIKEY)
                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input"
                ).first.fill(UNI_PASSWORD)

                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div/span/div/label"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
                ).click()
                page.wait_for_timeout(5000)
                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a"
                ).click()
                page.wait_for_timeout(1000)
                # calculate totp
                totp = pyotp.TOTP(UNI_TOPT_CODE)
                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input"
                ).first.fill(totp.now())
                page.locator(
                    "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
                ).click()

                page.wait_for_timeout(1000)

                page.goto("https://usyd.libcal.com/spaces?lid=3330&gid=0&c=0")

                for _ in range(14):
                    page.locator(
                        "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
                    ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[10]/td/div/div[2]/div[23]/a/div/div/div"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
                ).select_option("Arts and Social Sciences")

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
                ).click()

                page.goto("https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0")

                for _ in range(14):
                    page.locator(
                        "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
                    ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[10]/td/div/div[2]/div[27]/a/div/div/div"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
                ).select_option("Arts and Social Sciences")

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
                ).click()

                page.goto("https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0")

                for _ in range(2):
                    page.locator(
                        "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
                    ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[28]/td/div/div[2]/div[21]/a/div/div/div"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
                ).select_option("Arts and Social Sciences")

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
                ).click()

                page.goto("https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0")

                for _ in range(2):
                    page.locator(
                        "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
                    ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[28]/td/div/div[2]/div[27]/a/div/div/div"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label"
                ).click()

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
                ).select_option("Arts and Social Sciences")

                page.locator(
                    "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
                ).click()

                no_error = True
            except Exception as e:
                pass

        browser.close()
