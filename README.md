<h1 align="center">Yoga Flow Class Record</h1>

<img src="assets/images/responsive_img.png" height="400px"> 

**Live Site:**
[Yoga Flow Class Record Terminal](https://yoga-flow-class-record.herokuapp.com/)

**Repository:**
[Yoga Flow Class Record Repository](https://github.com/SamanthaBooth81/yoga-flow-class-record)

# About
This project collects lesson data from the user for the purpose of updating lesson data and calculate earnings. 

It is made with the intention of helping a small business owner keep their financial information in order and keep track of total earnings, both for the lesson added and a running total so far.

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
    * Keep track of the business earnings
    * Plan for the future growth of the business 

# Features
## Input Data
Input of lesson data including:
1. Day
2. Date
3. Time

<img src="assets/images/terminal_1.png" height="250px"> 
<img src="assets/images/heroku_deployment_10.png" height="250px"> 


4. Duration
5. Location 

<img src="assets/images/terminal_2.png" height="300px"> 

6. Attendance and calculations

<img src="assets/images/terminal_3.png" height="300px"> 

##  Calculations
- Calculate earnings per class and update spreadsheet
- Calculate the total of all inputted lessons

## Features to be Implemented
- Calculations of the busiest days in the week
- Analytics of the current timetable over the month to decipher:
    - Average student attendance per day
    - Busiest time period throughout the month
    - busiest time period throughout the year

The above should aid with decision making, such as making adjustments to the current timeable, running of workshops (when and where is best) and identifying capacity to add locations/lessons. 


# Technologies Used

## Languages Used

[Python](https://www.python.org/)

## Frameworks, Libraries and Programmes Used 

[GitHub](https://github.com/) - Used to hold a repository of my project and deploy the live website to Git Pages, making it public.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to GitHub repositiry, Heroku is a cloud application platform used to deploy this project so this backend language can be utilised/tested. 

[Google Sheets](https://workspace.google.com/intl/en_uk/products/sheets/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-bkws-all-all-trial-e-t1-1010042&utm_content=text-ad-crnurturectrl-none-DEV_c-CRE_146161043432-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Sheets%20~%20General%20%232-KWID_43700012539607188-kwd-11403239008-userloc_20485&utm_term=KW_google%20sheets-g&ds_rl=1289227&ds_rl=1259922&ds_rl=1289227&gclid=Cj0KCQjwtMCKBhDAARIsAG-2Eu-ikZjdKWgK9omCfFHENiM0V260I6vw4zlmpc1cabn0Jyru79bRzmkaAjFMEALw_wcB&gclsrc=aw.ds) to create an online based spreadsheet.

[Google Sheets API](https://developers.google.com/sheets/api) to link into my spreadsheet.

[datetime](https://docs.python.org/3/library/datetime.html) to work with the date and time.

[Colorama](https://www.youtube.com/watch?v=u51Zjlnui4Y) is used to add colour to the terminal.


# Testing

## Functionality 

I have manually tested the projecy by:
- running through a PEP8 linter
- intentionally added incorrect data to ensure the code rejects it 
- Tested both in Gitpod and Heroku terminals

# Validator Testing

The code was validated using [PEP8](http://pep8online.com/). No errors were retruned. 

# Bugs Found 

During testing I found that the date was not in the dd/mm/yy format I thought I had set it as. To fix this I changed the order of the following line of code from "day, month, year" to be "year, month, date":

<ins>my_date = date(int(year), int(month), int(day))</ins>

I also found that some user input errors were terminating the code although I used a while loop. To fix this I identified which lines of code were causing the errors using the Traceback in the terminal. What I found was the code that was causing the break in the loop wasn't within the while loop. To fix this I placed the code in the loop and function began to work as expected.  

Currently, there are no bugs found, however, the below pylint errors were appearing in the Problems tab:

<img src="assets/images/pylint_problems.png" height="150px"> 

I attempted to remove the errors however the variables I have stored globally were not working when moved into the module. Therefore I had to use the global keyword within the following functions:
- lesson_duration_data()
- lesson_location_data
- lesson_attendance_data

# Deployment 

This project was deployed using the Code Institutes mock terminal for Heroku. 

I followed the following steps:
1. Login to Heroku and Create a New App.

<img src="assets/images/heroku_deployment_1.png" height="120px"> 

2. Give the App a name, it must be unique, and select a region. 

<img src="assets/images/heroku_deployment_2.png" height="180px"> 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Click on 'Settings' among the tabs at the top of the page. The following sets must be dione before deployment.

<img src="assets/images/heroku_deployment_3.png" height="180px"> 

5. Next, scroll down to Config Vars (also knownas Environment Variables). In order for Heroku to access my spreadsheet it must have access to the contents of the creds.json file. As this file is to be kept secure it cannot be found in my GitHub repository. To enable access securely, sensitive data is stored in a Config Vars. 

<img src="assets/images/heroku_deployment_4.png" height="120px"> 

6. Click 'Reveal Config Vars'. Where it says 'KEY', input CREDS and 'VALUE', input the contents of the creds.json file. Then click 'ADD'. 
I also had to add a second Config Vars of KEY: PORT and VALUE: 8000, to improve compatability with the Code Institute [Template](https://github.com/Code-Institute-Org/python-essentials-template) I am using.

7. Scroll down to Buildpacks. This adds futher required dependencies outside of the requirements.txt file. Click 'Add Buildpack', select 'python' first and then click 'Save Changes'. 
Then, add a second Buildpack, 'nodejs', to handle the mock terminal provided by The Code Institute.

<img src="assets/images/heroku_deployment_5a.png" height="180px"> 

**The order of these Buildpacks is intentional, ensure Python is on top and nodejs underneath. The order can be changed by clicking and dragging.** 

<img src="assets/images/heroku_deployment_5b.png" height="150px"> 

8. Go to the 'Deploy' section using the tabs at the top. Find the 'Deployment Method' section and choose GitHub. Then, I connected to my relevant GitHub Repository by searching the repository name and clicking 'Connect'.

<img src="assets/images/heroku_deployment_6.png" height="120px"> 

<img src="assets/images/heroku_deployment_6a.png" width="800px"> 

9. Scroll down to the Automatic and Manual Deploys sections. I have enabled Automatic Deploys as I want my project to automatically redeploy if push any changes back into my repository. I then clicked 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed my code. 

<img src="assets/images/heroku_deployment_7.png" height="180px"> 

10. Once my code was finished deploying I clicked view, to see my newly deployed project in the terminal. 

<img src="assets/images/heroku_deployment_8.png" height="150px"> 
<img src="assets/images/heroku_deployment_9.png" height="250px"> 

# Credit
## Content 

I used [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to test user input against the lesson_day list.

I used [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to help with the while loop when writing the lesson day function. 

I used this [Gspread Documentation](https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value) to find out how to link to a column of data in a spreadsheet.

# Acknowledgments
Thank you to all who encouraged and supported me as I created my first game, espcially to my mentor for his guidance and patience and tutor support at The Code Institute who helped when I was stuck. 
