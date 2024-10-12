import argparse
import json

import pyotp
from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Page

print("123")

parser = argparse.ArgumentParser(description="USYD LibCal Auto Booking Script")
parser.add_argument("--unikey", required=True, help="Your USYD Unikey")
parser.add_argument("--password", required=True, help="Your USYD password")
parser.add_argument("--totp", required=True, help="Your TOTP secret code")
parser.add_argument(
    "booking-seats-json-path",
    required=True,
    help="Path to the JSON file containing the booking seats",
)
args = parser.parse_args()

unikey = args.unikey
uni_password = args.password
uni_topt_code = args.totp
booking_seats_json_path = args.booking_seats_json_path

with open(booking_seats_json_path, "r") as f:
    booking_seats = json.load(f)


print("123")


def book_seat(
    page: Page,
    booking_page_url: str,
    seat_full_xpath: str,
    num_days_from_now: int = 1,
):
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

    page.wait_for_timeout(1000)


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

        for task in booking_seats["tasks"]:
            book_seat(
                page,
                task["booking_page_url"],
                task["seat_full_xpath"],
                task["num_days_from_now"],
            )

        browser.close()
