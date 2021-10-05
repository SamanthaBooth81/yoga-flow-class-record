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

    lesson_day = (
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday")

    """
    I used the following webpage helped with the while loop:
    https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python
    """
    while True:
        day_data_str = input("Enter lesson day here: ")
        day_input = day_data_str.title()
        day = str(day_input)

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

    while True:
        print("Please input the date of your lesson.")
        input_date = input("Enter the date in format 'dd/mm/yy': ")
        day, month, year = input_date.split('/')

        try:
            if datetime.datetime(int(day), int(month), int(year)):
                print(f"{input_date} is valid \n")
                break
            else:
                if day > 31:
                    raise ValueError()
        except ValueError as e:
            print(f"invalid data: {e}, please try again \n")

        """
        HELP! ValueError: not enough values to unpack (expected 3, got 2)
        """


def lesson_time_data():
    """
    Input and validate time data from the user
    Return an error if incorrect data submitted
    """

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

    while True:
        print("Please provide the duration of your lesson in minutes.")
        print("This could be either 45, 60, 90 or 120 minutes. Example: 60")
        duration_data_str = input("Enter lesson duration here: ")
        prices = SHEET.worksheet("prices")

        try:
            lesson_length = prices.findall(duration_data_str)
            if (lesson_length):
                print(f"{duration_data_str} is valid \n")
                break
            else:
                raise Exception()
        except Exception:
            print("invalid data, please try again \n")


capacity = SHEET.worksheet("capacity")


def lesson_location_data():
    """
    Input and validate location data from the user
    Return error if incorrect data submitted
    """

    print("Please provide the location of your lesson.")
    print("For example: Camden Town \n")
    location_data_str = input("Enter your data here: ")
    location_data = location_data_str.title()

    """
    Used the below link to find out how to find all
    data in a spreadsheet to compare it to the user
    input
    https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value
    """

    while True:
        try:
            location = capacity.findall(location_data)
            if (location):
                print(f"{location_data} is valid \n")
                break
        except ValueError:
            print(f"{location_data_str} is invalid")


def lesson_attendance_data():
    """
    Input and validate attendance data from the user
    Return error if incorrect data submitted
    """

    while True:
        print("Please provide the number of students who attended.")
        lesson_attendance_str = input("Enter student attendance here: ")
        lesson_attendance = int(lesson_attendance_str)

        try:
            if lesson_attendance <= 20:
                print(f"{lesson_attendance} is valid.")
                break
            else:
                raise ValueError(
                    "please input a number less than 21."
                    )
        except ValueError as e:
            print(f"Incorrect data input, {e}")
            return True


def lesson_data():
    # lesson_day_data()
    # lesson_date_data()
    lesson_time_data()
    lesson_duration_data()
    # lesson_location_data()
    # lesson_attendance_data()


lesson_data()
