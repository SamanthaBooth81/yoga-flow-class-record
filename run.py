"""
Below code required to link into google sheets spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('yoga _flow_class_record')


def lesson_day_data():
    """
    Input and validate day data from the user
    Return an error if incorrect
    """

    print("Please provide day of your lesson.")
    print("This should be between Monday to Sunday only\n")

    lesson_day = [
        "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]

    """
    I used the following webpage helped with the while loop:
    https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python
    """
    while True:
        day_data_str = input("Enter lesson day here: ")
        day = str(day_data_str)

        day_data = False
        for i in lesson_day:
            if day == i:
                day_data = True

        if day_data:
            print("Correct")
        else:
            print("Incorrect")


def date_data():
    """
    Input and validate date data from the user
    Return an error if incorrect
    """

    print("Please provide date of your lesson.")
    print("The date format should be DD/MM/YYYY \n")
    

lesson_day_data()
