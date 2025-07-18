# 自动化测试项目（Automation Testing Project）
本项目是一个针对 Demo OrangeHRM 网站登录功能的自动化测试套件。它使用 Selenium WebDriver 和 Page Object Model（页面对象模型，POM）设计模式，验证多种登录场景，包括错误凭证的提示信息、成功登录以及页面跳转等。

## 项目功能（Features）
1. 错误信息验证：确保当输入为空或不合法时，页面会显示正确的错误提示。
2. 成功登录验证：检查在正确输入凭证后是否成功跳转到用户仪表盘（Dashboard）。
3. 页面对象模型（POM）：提升脚本的可维护性与可复用性。

## 项目结构（Project Structure）
AutomationTestingProject/

├── pages/                         # Encapsulates page logic and locators

│   └── login_page.py              # Handles login page interactions

├── tests/                         # Contains test scripts

│   └── test_login.py              # Tests login scenarios

├── main.py                        # Entry point for running all tests

├── requirements.txt               # Project dependencies

└── README.md                      # Project documentation

## 环境要求（Prerequisites）
Python 3.7 或更高版本
Google Chrome 浏览器
ChromeDriver（版本需与浏览器兼容）

## 安装与配置（Setup and Installation）
1. 克隆仓库：
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2. 安装依赖：
pip install -r requirements.txt
3. 下载并配置 ChromeDriver：
确保 chromedriver 已加入系统的 PATH，或将其放在项目目录下。

## 使用方法（Usage）
运行 main.py 文件以执行所有测试：
python main.py

## 测试场景（Test Scenarios）
空白凭证：验证是否显示 “必填” 的错误提示。
无效凭证：检查输入错误的用户名或密码后，是否显示错误信息。
有效凭证：验证成功登录后是否跳转到仪表盘。

## 示例输出（Example Output）
测试结果：控制台中显示测试成功或失败信息。
截图记录：可在 screenshots/ 文件夹中查看调试截图。

## 项目依赖（Dependencies）
本项目使用以下库：
Selenium：用于浏览器自动化操作
unittest：用于组织和管理测试用例
安装依赖：
pip install selenium

## 测试网站（Demo Website）
本测试项目使用以下网站作为测试目标：
https://opensource-demo.orangehrmlive.com/




# Automation Testing Project
This project is an automation testing suite for the login functionality of the Demo OrangeHRM website. It validates various scenarios, such as error messages for incorrect credentials, successful login, and page redirections, using Selenium WebDriver and the Page Object Model (POM) design pattern.


### Features
1. Error message validation: Ensures proper feedback for empty and invalid login credentials.
2. Successful login verification: Checks redirection to the dashboard upon successful login.
3. Page Object Model: Enhances script maintainability and reusability.


### Project Structure
AutomationTestingProject/

├── pages/                         # Encapsulates page logic and locators

│   └── login_page.py              # Handles login page interactions

├── tests/                         # Contains test scripts

│   └── test_login.py              # Tests login scenarios

├── main.py                        # Entry point for running all tests

├── requirements.txt               # Project dependencies

└── README.md                      # Project documentation


### Prerequisites
Python 3.7 or higher
Google Chrome browser
ChromeDriver (compatible with your Chrome version)


### Setup and Installation
1. Clone this repository:
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2. Install dependencies
pip install -r requirements.txt
3. Download and set up ChromeDriver:
Ensure chromedriver is in your PATH or place it in the project directory.


### Usage
Run the tests by executing the main.py file:
python main.py
Test Scenarios
1. Empty credentials: Verifies the "Required" error message.
2. Invalid credentials: Checks the error message for incorrect username or password.
3. Valid credentials: Validates successful login and dashboard redirection.
Example Output
1. Test Results: Test success/failure is displayed in the console.
2. Screenshots: Check the screenshots/ folder for visual debugging.


### Dependencies
The following libraries are used in this project:
1. Selenium: For browser automation
2. unittest: For test case management
To install them, run:
pip install selenium


### Demo Website
This project is tested on the Demo OrangeHRM site: https://opensource-demo.orangehrmlive.com/


### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.


### License
This project is open source and available under the MIT License.
