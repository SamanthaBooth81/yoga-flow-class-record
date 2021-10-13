"""
Below code required to link into google sheets spreadsheet and datetime
"""
import datetime
from datetime import date
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init()

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

"""
new_lesson_data adds user input into a list which is pushed back
into the spreadsheet when all data is collected.
"""
new_lesson_data = []
print(Fore.LIGHTMAGENTA_EX)
print("Hello, welcome to Yoga Flow Class Record.\n")
print("\033[39m")


def lesson_day_data():
    """
    Input and validate 'day' data from the user and
    returns an error if incorrect data submitted.

    I used the Stack Overflow to help with the below while loop.
    Page linked in the Readme file.
    """

    print("Please provide the day of your lesson in full.")
    print("Example: monday not mon")

    lesson_day = (
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday")

    while True:
        day_data_str = input("Enter lesson day here: ")
        input_day = day_data_str.title()
        day = str(input_day)

        day_data = False

        if day in lesson_day:
            day_data = True
            print("\n")

        if day_data:
            # append user input to a list of user inputs
            new_lesson_data.append(input_day)
            break
        else:
            print(Fore.RED)
            print(f"{Fore.RED}Invalid data: {day}")
            print("\033[39m")
            print("Please input a day in the week")


def lesson_date_data():
    """
    Input and validate 'date' data from the user and
    return an error if incorrect data submitted
    """
    while True:
        print("Please input the date of your lesson")
        input_date = input("Enter the date in format 'dd/mm/yy': ")

        try:
            day, month, year = input_date.split('/')
            my_date = date(int(year), int(month), int(day))
            if my_date:
                print("\n")
                # append user input to a list of user inputs
                new_lesson_data.append(input_date)
                break
        except ValueError as e:
            print(Fore.RED)
            print(f"Invalid data: {e}")
            print("\033[39m")
            print("Please try again \n")


def lesson_time_data():
    """
    Input and validate 'time' data from the user and
    return an error if incorrect data submitted
    """

    while True:
        print("Please provide time (00:00) of your lesson.")
        time_data_str = input("Enter time here: ")

        timeformat = ("%H:%M")

        try:
            validtime = datetime.datetime.strptime(
                time_data_str, timeformat)
            if validtime:
                print("\n")
                # append user input to a list of user inputs
                new_lesson_data.append(time_data_str)
                break
        except ValueError as e:
            print(f"{Fore.RED}Invalid data: {e} \n")
            print("\033[39m")


def lesson_duration_data():
    """
    Input and validate 'duration' data from the user and
    return error if incorrect data submitted
    """

    while True:
        print("Please provide the duration of your lesson in minutes.")
        print("Example: 60")
        try:
            duration_data_str = int(input("Enter lesson duration here: "))
            class_duration = prices.col_values(1)
            del class_duration[0]
            duration_int = list(map(int, class_duration))

            if duration_data_str in duration_int:
                print("\n")
                # append user input to a list of user inputs
                new_lesson_data.append(duration_data_str)

                # duration_index Stores globally the index
                # of the duration input by the user from the
                # list pulled from the worksheet. This will
                # be used when calculating earnings for that lesson.
                global duration_index
                duration_index = 0
                duration_data_index = duration_int.index(duration_data_str)
                duration_index = duration_data_index
                break
            else:
                print(Fore.RED)
                print(f"{duration_data_str} is not a valid duration\n")
                print("\033[39m")
        except ValueError as e:
            print(f"{Fore.RED}invalid data: {e}please try again \n")
            print("\033[39m")


def lesson_location_data():
    """
    Input and validate 'location' data from the user and
    return error if incorrect data submitted

    Used the below link to find out how to link to a
    column of data in a spreadsheet:
    https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value
    """

    while True:
        print("Please provide the location of your lesson.")
        print("For example: Camden Town")
        location_data_str = input("Enter your data here: ")
        location_data = location_data_str.title()

        try:
            class_location = capacity.col_values(1)
            del class_location[0]
            if location_data in class_location:
                print("\n")
                # append user input to a list of user inputs
                new_lesson_data.append(location_data)

                # location_index Stores globally the index of the location
                # input by the user from the list pulled from the worksheet.
                # This will be used when inputting student attendance to
                # identify the capacity of the studio and run an error if
                # attendance input is too high.

                global location_index
                location_index = 0
                location_data_index = class_location.index(location_data)
                location_index = location_data_index
                break
            else:
                raise ValueError()
        except ValueError:
            print(Fore.RED)
            print(f"Invalid data: {location_data_str}, please try again\n")
            print("\033[39m")


def lesson_attendance_data():
    """
    Input and validate 'attendance' data from the user and
    return error if incorrect data submitted
    """
    while True:
        # column of capacity data for each location
        location_capacity = capacity.col_values(2)
        # deletes the first item in column of data
        del location_capacity[0]

        try:
            print("Please provide the number of students who attended.")
            lesson_attendance_str = input(
                "Enter student attendance here: ")
            lesson_attendance = int(lesson_attendance_str)

            # Get the capacity using the index stored in location_index
            capacity_index = int(location_capacity[location_index])

            global attendance_total
            attendance_total = 0
            attendance_input = lesson_attendance
            attendance_total = attendance_input

            if lesson_attendance <= capacity_index:
                # append user input to a list of user inputs
                new_lesson_data.append(lesson_attendance)
                break
            else:
                while True:
                    print(Fore.YELLOW)
                    print(f"{lesson_attendance} is above studio capacity\n")
                    higher_capacity = input("Do you wish to continue [y/n]?")
                    add_higher_cap = higher_capacity.upper()
                    print("\033[39m")
                    while True:
                        if add_higher_cap == "Y":
                            new_lesson_data.append(lesson_attendance)
                            return False
                        else:
                            return lesson_attendance_data()
        except ValueError as e:
            print(Fore.RED)
            print(f"Data invalid: {e}, please try again\n")
            print("\033[39m")


def calculate_earnings():
    """
    Calculate the earnings for the lesson using the attendance
    and duration input by the user and the price list
    on the linked spreadsheet
    """

    lesson_price = prices.col_values(2)
    del lesson_price[0]

    price = int(lesson_price[duration_index])

    lesson_earnings = price * attendance_total

    print(Fore.GREEN)
    print(
        f"\nThe earnings made for this class is: £{lesson_earnings}")
    print("\033[39m")
    # append calculation to a list of user inputs
    new_lesson_data.append(lesson_earnings)


def update_attendance_worksheet(data):
    """
    Push user inputs and calculations stored in the
    new_lesson_data list back into the attendance worksheet
    """

    print(Fore.BLUE)
    print("Updating worksheet... \n")
    # appends user inputs and calulations into the attendance worksheet
    worksheet_update = SHEET.worksheet("attendance")
    worksheet_update.append_row(data)

    print("Attendance worksheet updated \n")
    print("\033[39m")


def lesson_data():
    """ Runs all the functions
    """
    lesson_day_data()
    lesson_date_data()
    lesson_time_data()
    lesson_duration_data()
    lesson_location_data()
    lesson_attendance_data()
    data = new_lesson_data
    calculate_earnings()
    update_attendance_worksheet(data)
    return add_more_data()


def add_more_data():
    """ Loops back to the beginning if
    the user has more data to add.
    """
    add_data = input("Do you want to add more data [y/n]?")
    new_data = add_data.upper()
    while True:
        if new_data == "Y":
            new_lesson_data.clear()
            print("\n")
            return lesson_data()
        else:
            print(Fore.LIGHTMAGENTA_EX)
            print("\nThank you, goodbye for now...\n")
            break


lesson_data()
