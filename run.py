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

def get_lesson_data():
    """
    Collects lesson data from the user
    """
    print("Please provide lesson data from todays classes.")
    print("The data should contain the day, date, time, duration in mins, location and attendance separated by commas")
    print("Example: Monday,27/09/2021,08:00,60,Camden Town,15\n")

    lesson_data_str = input("Enter your data here: ")
    print(f"The data provided is {lesson_data_str}")

get_lesson_data()