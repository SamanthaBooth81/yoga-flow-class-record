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
    Collects lesson data from the user. 
    Each item of data will need to be validated differendly. 
    Therefore I have created separate inputs.
    """
    print("Please provide day of your lesson.")
    print("This should be between Monday to Sunday only\n")
    day_data_str = input("Enter your data here: ")
    print("\n")

    validate_data(day_data_str)

    print("Please provide date of your lesson.")
    print("This should be in the format DD/MM/YYYY \n")
    date_data_str = input("Enter your data here: ")
    print("\n")

    print("Please provide time of your lesson.")
    print("This should be in the format 00:00 \n")
    time_data_str = input("Enter your data here: ")
    print("\n")

    print("Please provide the duration of your lesson in minutes.")
    print("This should be in the format 00, example 60 \n")
    duration_data_str = input("Enter your data here: ")
    print("\n")

    print("Please provide the location of your lesson.")
    print("For example: Camden Town \n")
    location_data_str = input("Enter your data here: ")
    print("\n")

    print("Please provide the total number of students who attended your lesson.")
    print("For example: 12 \n")
    attendance_data_str = input("Enter your data here: ")
    print("\n")

    print(
        f"The lesson data provided is: \nDay: {day_data_str}, Date: {date_data_str}, Time: {time_data_str}, Duration: {duration_data_str}, Location: {location_data_str}, Attendance: {attendance_data_str}")


# def validate_lesson_data():
#     """
#     Valuate the lesson data provided by the user
#     and returns an error if incorrect
#     """

#     day = ["monday", "tuesday", "wednesday",
#            "thursday", "friday", "saturday", "sunday"]
#     try:
#         if day =! validate_lesson_data(day_data_str):
#             print("data is correct")
#     except ValueError:
#         print("You have provided incorrect data, please choose a day, example: Monday")

def validate_data(day):
    """
    Validate the lesson data provided by the user 
    and returns an error if incorrect 
    """
    lesson_day = [
        "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]

    try:
        for day_data_str in lesson_day:
            if lesson_day != day:
                print(f"{day_data_str} is incorrect")
                break
    except ValueError:
        print("Incorrect data, please choose a day between Monday - Sunday")


get_lesson_data()
