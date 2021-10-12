<h1 align="center">Yoga Flow Class Record</h1>

![Responsiveness Screenshot](Link TBC)

**Live Site:**
[Yoga Flow Class Record Terminal](Link TBC)

**Repository:**
[Yoga Flow Class Record Repository](https://github.com/SamanthaBooth81/yoga-flow-class-record)

# About
This project collects lesson data from the user for the purpose of calculating and updating student attendance and earnings within the spreadsheet. Alongside managing financial data, this projects aims to aid decision making with regards to their current schedule dependant on class size vs. studio capacity, and location. 

It is made with the intention of helping a small business owner keep their financial information in order and return to the user their busiest days. This should in turn help with both short term and long term decision making surrounding their current timetable such as:
- reducing current personal lesson days (for the business owner)
- taking on new staff 
- expansion of the lessons on offer
- expansion of the locations on offer

# Table of Contents

[User Experience](#user-experience)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Validator Testing](#validator-testing)

[Performancce Testing](#performance-testing)

[Bugs Found](#bugs-found)

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)

# User Experience
## User Stories
- As a small business owner I want to:
    * Keep track of the growth of the business
    * Calculate earnings per lesson
    * Run basic analytics based on class size and earnings to aid with business decisions 
    * Plan for the future growth of the business 

# Features
## Inputting Data
- Input of lesson data including:
    * Date
    * Date
    * Time
    * Duration
    * Location 
    * Attendance 

##  Calculations
- Calculate earnings per class and update spreadsheet 
- Calculate the 4 busiest days on average in the week
- Calculate the busiest location

## Features to be Implemented
- Further automation of repetitive data input
- Calculations of the busiest period over a larger scale of time 
- Code to add other venues and their capacity to the capacity worksheet
- Code to add another class duration and cost to the price worksheet 

# Technologies Used

## Languages Used

[Python](https://www.python.org/)

## Frameworks, Libraries and Programmes Used 

[GitHub](https://github.com/) - Used to hold a repository of my project and deploy the live website to Git Pages, making it public.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to GitHub repositiry, Heroku is a cloud application platform used to deploy this project so this backend language can be utilised/tested. 

[Google Sheets](https://workspace.google.com/intl/en_uk/products/sheets/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-bkws-all-all-trial-e-t1-1010042&utm_content=text-ad-crnurturectrl-none-DEV_c-CRE_146161043432-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Sheets%20~%20General%20%232-KWID_43700012539607188-kwd-11403239008-userloc_20485&utm_term=KW_google%20sheets-g&ds_rl=1289227&ds_rl=1259922&ds_rl=1289227&gclid=Cj0KCQjwtMCKBhDAARIsAG-2Eu-ikZjdKWgK9omCfFHENiM0V260I6vw4zlmpc1cabn0Jyru79bRzmkaAjFMEALw_wcB&gclsrc=aw.ds)

[Google Sheets API](https://developers.google.com/sheets/api)


# Testing

## Functionality 

# Validator Testing


# Performance Testing
The performance testing of the site was completed using WebPageTest with the location set as London and browser Google Chrome.

The following results was received:

<img src="assets/images/performance-testing.png" height="100px">

Areas of improvement are Security and Cache Static Content which are not part of this projects scope but I will work on these for future projects.

# Bugs Found 

No bugs found. 

# Deployment 

# Credit
## Content 

I used [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to test user input against the lesson_day list.

I used [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to help with the while loop when writing the lesson day function. 

I used this [Gspread Documentation](https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value) to find out how to link to a column of data in a spreadsheet.

# Acknowledgments
Thank you to all who encouraged and supported me as I created my first game, espcially to my mentor for his guidance and patience. 
