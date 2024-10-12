import argparse
import json

import pyotp
from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Browser

import multiprocessing.pool

print("123")

parser = argparse.ArgumentParser(description="USYD LibCal Auto Booking Script")
parser.add_argument("--unikey", required=True, help="Your USYD Unikey")
parser.add_argument("--password", required=True, help="Your USYD password")
parser.add_argument("--totp", required=True, help="Your TOTP secret code")
parser.add_argument(
    "--booking-seats-json-path",
    required=True,
    help="Path to the JSON file containing the booking seats",
)
args = parser.parse_args()

unikey = args.unikey
uni_password = args.password
uni_topt_secret = args.totp
booking_seats_json_path = args.booking_seats_json_path

with open(booking_seats_json_path, "r") as f:
    booking_seats = json.load(f)


print("123")


def book_seat(
    browser: Browser,
    booking_page_url: str,
    seat_full_xpath: str,
    num_days_from_now: int = 1,
):
    booking_page = browser.new_page()
    booking_page.goto(booking_page_url)
    print(f"Navigated to {booking_page_url}")

    for _ in range(int(num_days_from_now)):
        booking_page.locator(
            "xpath=/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[1]/div[1]/div/button[2]"
        ).click()

    booking_page.locator(f"xpath={seat_full_xpath}").click()

    booking_page.locator(
        "xpath=/html/body/div[2]/main/div/div/div/div[4]/form/fieldset/div[2]/button"
    ).click()

    booking_page.wait_for_timeout(1000)

    booking_page.locator(
        "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[4]/fieldset/div/div[1]/label/input"
    ).click()

    booking_page.locator(
        "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[5]/div/select"
    ).select_option("Arts and Social Sciences")

    booking_page.locator(
        "xpath=/html/body/div[2]/main/div/div/div/div/div[2]/form/fieldset/div[6]/div/button"
    ).click()

    booking_page.wait_for_timeout(1000)


with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser: Browser = browser_type.launch()
        sign_in_page = browser.new_page()

        sign_in_page.goto("https://sso.sydney.edu.au")
        print("Navigated to sso.sydney.edu.au")
        # click button based on Xpath
        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input"
        ).first.fill(unikey)
        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input"
        ).first.fill(uni_password)

        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div/span/div/label"
        ).click()

        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
        ).click()
        sign_in_page.wait_for_timeout(1000)
        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/a"
        ).click()
        sign_in_page.wait_for_timeout(1000)
        # calculate totp
        totp = pyotp.TOTP(uni_topt_secret)
        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input"
        ).first.fill(totp.now())
        sign_in_page.locator(
            "xpath=/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input"
        ).click()

        sign_in_page.wait_for_timeout(5000)

        tasks: list[tuple[Browser, str, str, int]] = [
            (
                browser,
                booking_seat["booking_page_url"],
                booking_seat["seat_full_xpath"],
                int(booking_seat["num_days_from_now"]),
            )
            for booking_seat in booking_seats
        ]

        with multiprocessing.pool.ThreadPool(processes=4) as pool:
            pool.starmap_async(book_seat, tasks).get()

        browser.close()
