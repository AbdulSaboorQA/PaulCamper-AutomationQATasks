
# PaulCamper QA Automation Tasks

These instructions will get you a copy of the project up and running on your local machine for testing purposes.


## Prerequisites

1- Install the following:
- Java
- NodeJS and NPM
- Python and its virtualenv
- Selenium WebDriver
- PyCharm IDE
- Appium 
- Appium Server GUI
- Android Studio
- Chrome Browser

2- Additional required packages/plugins for Selenium:

- Pytest: Pytest Unittest framework
- pytest-html: Pytest HTML Reports

3- Additional required packages/plugins for Appium:

- Unittest: Unittest framework
- HTMLTestRunner




## Test Task 1

Compose and write test-scenarios on the web-page https://paulcamper.com/rent-camper/ for following search filters using Selenium & Python language:

● Validate that the Select All Check Box works Programmatically using Python Selenium

● Flow → Vehicle→Body Style→ “Select All” → checkbox
Please use the PageObject pattern for the implementation.

At the end of the testing task the
working code is expected, which can be copied and run on the local machine.


### Solution

I implemented the following test scenarios using

- Selenium as automation tool
- Python as language
- Pytest as automation framework
- PyCharm as the IDE
- and POM as pattern

1 . Verify that the "Select All" checkbox is present and is checked on clicking:
- Navigate to the "Vehicle -> Body Style" page
- Find the "Select All" checkbox element
- Click on the "Select All" checkbox element
- Verify that the "Select All" checkbox is checked

2 . Verify that the "Select All" checkbox is checked and on clicking again it unchecks:
- Navigate to the "Vehicle -> Body Style" page
- Find the "Select All" checkbox element
- Verify that the element is clickable
- Click on the "Select All" checkbox element
- Verify that the "Select All" checkbox is checked
- Once Verified, click again on the “Select All” Checkbox.
- Verify that the “Select All” checkbox is unchecked.

3 . Verify that the "Select All" checkbox checks all the body style options:
- Navigate to the "Vehicle -> Body Style" page
- Find the "Select All" checkbox element
- Click the "Select All" checkbox
- Verify that all the body style checkbox options are checked

4 . Verify that the "Select All" checkbox un checks all the body style options:
- Navigate to the "Vehicle -> Body Style" page
- Find the "Select All" checkbox element
- Click the "Select All" checkbox
- Verify that all the body style options are selected
- Click again on the "Select All" checkbox
- Verify that all the body style checkbox options are un checked

5 . Verify that the checking all the other body style options checkboxes checks the “Select All” checkbox:
- Navigate to the "Vehicle -> Body Style" page
- Click on each body style checkboxes one by one
- Verify that all the body style checkbox options are checked
- Verify that “Select All” checkbox is checked.

6 . Verify that the un-checking all the other body style options checkboxes un-checks the “Select All” checkbox:
- Navigate to the "Vehicle -> Body Style" page
- Click on each body style checkboxes one by one
- Verify that all the body style checkbox options are checked
- Verify that “Select All” checkbox is checked.
- Click on each body style checkboxes one by one again
- Verify that all the body style checkbox options are un-checked
- Verify that “Select All” checkbox is also un-checked.


#### Task1 Automation Script

The test automation scripting for the above mention task is in the folder name "Task1WebAutomation".

Note: Before cloning the code and running it locally please make sure to have the right tools and plugins installed as mentioned for smooth run.




## Test Task 2

Compose and write a test-scenario to access web-page https://paulcamper.com/rent-camper/ in Mobile Browser Using the Mobile Automation Approach.

Test Steps:

1 . Open Mobile Browser for Android or iOS.

2 . Navigate to https://paulcamper.com/rent-camper/.

3 . Assert rent-camper page is displayed.


### Solution

I implemented the above mentioned test scenario using:

- Appium as automation tool
- Python as language
- PyCharm as the IDE
- Unittest as automation framework
- Selenium Webdriver as a wrapper
- Android Studio for Android Emulator
- Appium Server GUI for starting the server
- and POM as the pattern.


#### Task2 Automation Script

The test automation scripting for the above mention task is in the folder name "Task2MobileAutomation".

Note: Please update the "deviceName" in the "desired_capabilities" in "test_rent_camper_page.py" file in the function "test_rent_camper_page_displayed" according to the connected emulator name.

After cloning the code for running it locally please make sure to have the right tools and plugins installed as mentioned for smooth run. 
