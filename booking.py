import os

import pyotp
from playwright.sync_api import sync_playwright

print("123")

UNIKEY = os.getenv("UNIKEY")
UNI_PASSWORD = os.getenv("UNI_PASSWORD")
UNI_TOPT_CODE = os.getenv("UNI_TOPT_CODE")

print(UNIKEY)
print("123")
