Automation Testing Project
This project is an automation testing suite for the login functionality of the Demo OrangeHRM website. It validates various scenarios, such as error messages for incorrect credentials, successful login, and page redirections, using Selenium WebDriver and the Page Object Model (POM) design pattern.

Features
1. Error message validation: Ensures proper feedback for empty and invalid login credentials.
2. Successful login verification: Checks redirection to the dashboard upon successful login.
3. Page Object Model: Enhances script maintainability and reusability.

Project Structure
AutomationTestingProject/
├── pages/                         # Encapsulates page logic and locators
│   └── login_page.py              # Handles login page interactions
├── tests/                         # Contains test scripts
│   └── test_login.py              # Tests login scenarios
├── screenshots/                   # Stores screenshots generated during tests
├── main.py                        # Entry point for running all tests
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation

Prerequisites
Python 3.7 or higher
Google Chrome browser
ChromeDriver (compatible with your Chrome version)

Setup and Installation
Clone this repository:
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

Install dependencies:
pip install -r requirements.txt

Download and set up ChromeDriver:
Ensure chromedriver is in your PATH or place it in the project directory.

Usage
Run the tests by executing the main.py file:
python main.py

Test Scenarios
Empty credentials: Verifies the "Required" error message.
Invalid credentials: Checks the error message for incorrect username or password.
Valid credentials: Validates successful login and dashboard redirection.

Example Output
Test Results: Test success/failure is displayed in the console.
Screenshots: Check the screenshots/ folder for visual debugging.

Dependencies
The following libraries are used in this project:
Selenium: For browser automation
unittest: For test case management
To install them, run:
pip install selenium

Demo Website
This project is tested on the Demo OrangeHRM site: https://opensource-demo.orangehrmlive.com/

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is open source and available under the MIT License.
