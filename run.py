"""
Below code required to link into google sheets spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials
import datetime


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
    print("This should be between monday to sunday only\n")

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
            print("\n")
            break
        else:
            print("Incorrect data, please choose a day in the week \n")


def lesson_date_data():
    """
    Input and validate date data from the user
    Return an error if incorrect
    """

    print("Please input the date of your lesson.")
    inputDate = input("Enter the date in format 'dd/mm/yy': ")
    day, month, year = inputDate.split('/')

    while True:
        isValidDate = False
        try:
            datetime.datetime(int(day), int(month), int(year))
            isValidDate = True
        except ValueError:
            isValidDate = False
            print("invalid data")

        if(isValidDate):
            print("Input date is valid \n")
            break
        else:
            print("Input date is not valid")


def lesson_time_data():
    """
    Input and validate time data from the user
    Return an error if incorrect
    """

    timeformat = "%H:%M"

    while True:
        print("Please provide time (00:00) of your lesson. \n")
        time_data_str = input("Enter time here: ")

        timeformat = ("%H:%M")
        isValidTime = False

        try:
            validtime = datetime.datetime.strptime(time_data_str, timeformat)
            if(validtime):
                isValidTime = True
                print(f"{time_data_str}")
                break
            else:
                print("incorrect time data added")
        except Exception:
            print(f"{time_data_str} is incorrect")


def lesson_data():
    lesson_day_data()
    lesson_date_data()
    lesson_time_data()


lesson_data()
