# usyd-libcal-auto-booking-public

## Introduction

Automatically book a study space at the University of Sydney Library using Playwright And Github Actions.


It will book the following study spaces:

Study room 202 @ Fisher Library 11:00 - 13:00, 14 days from now

Study room M108 @ Law Library 13:00 - 15:00, 14 days from now

Desk 17 @ Law Library 10:00 - 16:00, 2 days from now


Execute at Sydney time 00:30, 01:30 if daylight saving.

## How to use

prepear the seats you want to book as the following format:

```json
{
    "tasks": [
        {
            "num_days_from_now": 14,
            "booking_page_url": "https://usyd.libcal.com/spaces?lid=3330&gid=0&c=0",
            "seat_full_xpath": "/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[10]/td/div/div[2]/div[23]/a/div/div/div"
        },
        {
            "num_days_from_now": 14,
            "booking_page_url": "https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0",
            "seat_full_xpath": "/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[10]/td/div/div[2]/div[27]/a/div/div/div"
        },
        {
            "num_days_from_now": 2,
            "booking_page_url": "https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0",
            "seat_full_xpath": "/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[28]/td/div/div[2]/div[21]/a/div/div/div"
        },
        {
            "num_days_from_now": 2,
            "booking_page_url": "https://usyd.libcal.com/spaces?lid=3331&gid=0&c=0",
            "seat_full_xpath": "/html/body/div[2]/main/div/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[28]/td/div/div[2]/div[27]/a/div/div/div"
        }
    ]
}
```

- `num_days_from_now`: The number of days from today to book the seat.
- `booking_page_url`: The URL of the booking page.
- `seat_full_xpath`: The XPath of the seat you want to book.

To obtain the xpath, you can use the browser's developer tools. For example, in Chrome, you can right-click on the element and select "Copy" -> "Copy XPath".

Then you can run the script by executing the following command:

```bash
uv sync 
uv run -m playwright install --with-deps
uv run booking.py --unikey <UNIKEY> --password <>UNI_PASSWORD> --totp $<>UNI_TOPT_SECERT> \
--booking-seats-json-path <PATH_TO_JSON_FILE> 
```

Here the UNI_TOPT_CODE this is the code you can get by adding google authenticator to your okta account.

Note this code here is not the 6 digit code you get from the google authenticator app, it is the secret that generates the 6 digit code. In other words, it is the code embedded in the QR code when use sign up for the google authenticator app. Use bitwarden to scan the QR code can reveal the code. The code should be 16 characters long, all uppercase, with numbers and letters.