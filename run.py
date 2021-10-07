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

capacity = SHEET.worksheet("capacity")
prices = SHEET.worksheet("prices")

new_lesson_data = []
# location = input.location_data
# location_data = None
location_index = []


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
        input_day = day_data_str.title()
        day = str(input_day)

        day_data = False

        if day in lesson_day:
            day_data = True
            print(f"{day} is valid \n")

        if day_data:
            new_lesson_data.append(input_day)
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

        try:
            day, month, year = input_date.split('/')
            if datetime.datetime(int(day), int(month), int(year)):
                print(f"{input_date} is valid \n")
                new_lesson_data.append(input_date)
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
                new_lesson_data.append(time_data_str)
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
            class_duration = prices.col_values(1)
            del class_duration[0]

            if duration_data_str in class_duration:
                print(f"{duration_data_str} is valid \n")
                new_lesson_data.append(duration_data_str)
                break
            else:
                raise Exception()
        except Exception:
            print("invalid data, please try again \n")


def lesson_location_data():
    """
    Input and validate location data from the user
    Return error if incorrect data submitted
    """

    """
    Used the below link to find out how to find all
    data in a spreadsheet to compare it to the user
    input
    https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value
    """

    while True:
        print("Please provide the location of your lesson.")
        print("For example: Camden Town \n")
        location_data_str = input("Enter your data here: ")
        location_data = location_data_str.title()
        try:
            class_location = capacity.col_values(1)
            del class_location[0]
            if location_data in class_location:
                print(f"{location_data} is valid \n")
                new_lesson_data.append(location_data)
                location_data_index = class_location.index(location_data)
                location_index.append(location_data_index)
                break
            else:
                raise ValueError()

        except ValueError:
            print(f"{location_data_str} is invalid \n")


def lesson_attendance_data():
    """
    Input and validate attendance data from the user
    Return error if incorrect data submitted
    """
    while True:
        print("Please provide the number of students who attended.")
        lesson_attendance_str = input("Enter student attendance here: ")
        lesson_attendance = int(lesson_attendance_str)

        # column of capacity data for each location
        location_capacity = capacity.col_values(2)
        del location_capacity[0]  # delete the first item in column of data

        print(location_capacity.index)

        try:
            attendance_location = (location_capacity.index == location_index)
            if (attendance_location):
                if lesson_attendance <= location_capacity:
                    print("correct")
                    break
            else:
                print("incorrect")
                raise ValueError()
        except ValueError as e:
            print(f"Error: {e}, please try again")

    # while True:
        # print("Please provide the number of students who attended.")
        # lesson_attendance_str = input("Enter student attendance here: ")
        # lesson_attendance = int(lesson_attendance_str)

        # lesson_location = capacity.col_values(1)
        # del lesson_location[0]

        # location_capacity = capacity.col_values(2)
        # del location_capacity[0]

        # lesson_attendance_index = []

        # for i in range(0, len(lesson_location)):
        #     if lesson_location[i] == location_data:
        #         lesson_attendance_index.append(i)
        #         print(f"{lesson_attendance}")
        #         break
        #     else:
        #         print("incorrect")

        # try:
        #     if lesson_attendance <= 20:
        #         print(f"{lesson_attendance} is valid.")
        #         new_lesson_data.append(lesson_attendance)
        #         break
        #     else:
        #         raise ValueError(
        #             "please input a number less than 21. \n"
        #         )
        # except ValueError as e:
        #     print(f"Incorrect data input, {e}")


def update_attendance_worksheet(data):
    """
    Push user inputs from the above lesson_
    functions back into the attendance worksheet
    """

    print("Updating worksheet... \n")
    worksheet_update = SHEET.worksheet("attendance")
    worksheet_update.append_row(data)

    print("Attendance worksheet updated")


# def calculate_earnings():
#     """
#     Calculate the earnings for that lesson using
#     the attendance and duration input and the price list
#     on the linked spreadsheet
#     """

#     class_price = prices.col_values(2)
#     print(class_price)


def lesson_data():
    # lesson_day_data()
    # lesson_date_data()
    # lesson_time_data()
    # lesson_duration_data()
    lesson_location_data()
    lesson_attendance_data()
    # data = new_lesson_data
    # update_attendance_worksheet(data)
    # calculate_earnings()


lesson_data()
# print(new_lesson_data)
