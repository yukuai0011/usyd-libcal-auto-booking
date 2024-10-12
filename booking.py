import argparse

import pyotp
from playwright.sync_api import sync_playwright

print("123")

parser = argparse.ArgumentParser(description="USYD LibCal Auto Booking Script")
parser.add_argument("--unikey", required=True, help="Your USYD Unikey")
parser.add_argument("--password", required=True, help="Your USYD password")
parser.add_argument("--totp", required=True, help="Your TOTP secret code")
parser.add_argument(
    "--num-days-from-now", required=True, help="Number of days from now to book"
)
parser.add_argument(
    "--booking-page-url", required=True, help="Number of hours from now to book"
)
parser.add_argument(
    "--seat-full-xpath", required=True, help="Xpath of the button to book a full seat"
)

args = parser.parse_args()

unikey = args.unikey
uni_password = args.password
uni_topt_code = args.totp
num_days_from_now = args.num_days_from_now
booking_page_url = args.booking_page_url
seat_full_xpath = args.seat_full_xpath

print("123")

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()

        page.goto("https://sso.sydney.edu.au")
        print("Navigated to sso.sydney.edu.au")
        # click button based on Xpath
        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input"
        ).first.fill(unikey)
        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input"
        ).first.fill(uni_password)

        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div/span/div/label"
        ).click()

        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
        ).click()
        page.wait_for_timeout(1000)
        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a"
        ).click()
        page.wait_for_timeout(1000)
        # calculate totp
        totp = pyotp.TOTP(uni_topt_code)
        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input"
        ).first.fill(totp.now())
        page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
        ).click()

        page.wait_for_timeout(5000)

        page.goto(booking_page_url)
        print(f"Navigated to {booking_page_url}")

        for _ in range(int(num_days_from_now)):
            page.locator(
                "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
            ).click()

        page.locator(f"xpath={seat_full_xpath}").click()

        page.locator(
            "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
        ).click()

        page.wait_for_timeout(1000)

        page.locator(
            "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label/input"
        ).click()

        page.locator(
            "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
        ).select_option("Arts and Social Sciences")

        page.locator(
            "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
        ).click()

        browser.close()
