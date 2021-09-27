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

# def get_lesson_data():
#     """
#     Collects lesson data from the user
#     """
#     print("Please provide lesson data from todays classes.")
#     print("The data should contain the day, date, time, duration in mins, location and attendance separated by commas")
#     print("Example: Monday,27/09/2021,08:00,60,Camden Town,15\n")

#     lesson_data_str = input("Enter your data here: ")
#     print(f"The data provided is {lesson_data_str}")

# get_lesson_data()

def get_lesson_data():
    """
    Collects lesson data from the user, 
    each item pf data will need to be validated differently 
    which is why I've created separate inputs
    """
    print("Please provide day of your lesson.")
    print("This should be between Monday to Sunday only\n")
    day_data_str = input("Enter your data here: ")
    print("\n")

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

    print(f"The lesson data provided is: \nDay: {day_data_str}, Date: {date_data_str}, Time: {time_data_str}, Duration: {duration_data_str}, Location: {location_data_str}, Attendance: {attendance_data_str}")

get_lesson_data()

