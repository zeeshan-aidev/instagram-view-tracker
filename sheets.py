import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDENTIALS

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect(sheet_url):
    creds = Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url)

    return sheet.sheet1


def get_accounts(sheet):
    rows = sheet.get_all_values()

    accounts = []

    for index, row in enumerate(rows[1:], start=2):
        if len(row) >= 9:
            url = row[8].strip()   # Column I

            if url:
                accounts.append({
                    "row": index,
                    "url": url
                })

    return accounts


def update_views(sheet, row, views):
    sheet.update(f"H{row}", [[views]])