# Login-Automation-with-Selenium

Automated Testing Project

Overview：
This project automates the testing of login and form functionalities for the Demo OrangeHRM website using Selenium.

Features：
1. Login Page Error Validation:
Verifies error messages when the username or password fields are empty or incorrect.
2. Successful Login Validation:
Checks redirection and presence of unique elements after a successful login.
3. Test Report Generation:
Captures screenshots and logs to summarize test results.
4. Page Object Model (POM):
Implements POM to separate test logic from page operations for better maintainability.


automation_project/
│
├── main.py                     # Main script to run tests (主入口脚本)
├── requirements.txt            # Dependencies (项目依赖)
├── pages/                      
│   └── login_page.py           # Login page POM class (POM 类)
├── tests/
│   └── test_login.py           # Login test cases (测试用例)
├── .gitignore                  
└── README.md                   # Documentation
