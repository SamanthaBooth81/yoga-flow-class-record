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
    Return an error if incorrect data submitted
    """

    print("Please provide day of your lesson in full.")
    print("Example: monday not mon")

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
                print(f"{day} is valid \n")

        if day_data:
            break
        else:
            print("Incorrect data, please choose a day in the week \n")


def lesson_date_data():
    """
    Input and validate date data from the user
    Return an error if incorrect data submitted
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
            print(f"{inputDate} is valid \n")
            break
        else:
            print("Input date is not valid")


def lesson_time_data():
    """
    Input and validate time data from the user
    Return an error if incorrect data submitted
    """

    timeformat = "%H:%M"

    while True:
        print("Please provide time (00:00) of your lesson.")
        time_data_str = input("Enter time here: ")

        timeformat = ("%H:%M")

        try:
            validtime = datetime.datetime.strptime(time_data_str, timeformat)
            if(validtime):
                print(f"{time_data_str} is valid \n")
                break
        except Exception:
            print(f"{time_data_str} is incorrect")
            print("time should be input in 00:00 format \n")


def lesson_duration_data():
    """
    Input and validate duration data from the user
    Return error if incorrect data submitted
    """
    print("Please provide the duration of your lesson in minutes (00)")
    print("Example: 60 \n")
    duration_data_str = input("Enter lesson duration here: ")

    while True:
        duration = int(duration_data_str)
        try:
            if(duration):
                print(f"{duration_data_str} is valid")
                break
        except Exception:
            print("incorrect")


def lesson_location_data():
    """
    Input and validate location data from the user
    Return error if incorrect data submitted
    """

    print("Please provide the location of your lesson.")
    print("For example: Camden Town \n")
    location_data_str = input("Enter your data here: ")
    """
    https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
    """

    while True:
        capacity = SHEET.worksheet("capacity")
        location = capacity.col_values(1)
        try:
            value = [location_data_str == location]
            if (value):
                print(f"{location_data_str} is valid")
                break
        except ValueError:
            print(f"{location_data_str} is invalid")


def lesson_data():
    #     lesson_day_data()
    #     lesson_date_data()
    #     lesson_time_data()
    #     lesson_duration_data()
    lesson_location_data()


lesson_data()
