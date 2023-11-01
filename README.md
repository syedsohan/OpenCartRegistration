# Selenium Registration Automation

This is a simple example of using Python and the Selenium WebDriver to automate registration on a website. This script will fill out all fields.

## Table of Contents
- [Selenium Registration Automation](#selenium-registration-automation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [License](#license)

## Introduction

This repository contains a Python script for automating the registration process on a website using the Selenium WebDriver. The script demonstrates how to:

- Open a web page
- Fill out a registration form with test data
- Validate the registration process

It includes dynamic waits, error handling, and detailed logging for reliable and robust automation. You can use this code as a starting point for automating similar registration workflows on other websites.

## Prerequisites

> [!IMPORTANT]  
> Starting with Selenium 4, you do not need to install the WebDriver separately. The Selenium library will automatically download and use the appropriate WebDriver for your chosen browser.

Before using this automation script, you need to have the following:

- Python 3.x installed (https://www.python.org/downloads/)
- The Selenium Python library (install using `pip install selenium`)
- Appropriate WebDriver for your chosen browser (e.g., ChromeDriver for Google Chrome)

## Installation

1. Clone this repository to your local machine

   ```bash
   git clone https://github.com/your-username/selenium-registration-automation.git
   ```

2. Navigate to the project folder
   
   ```bash
   cd repository
   ```

3. Setup the project
   
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the script to configure your specific test data and URL:

    ```python
    url = "https://demo.opencart.com/index.php?route=account/register&language=en-gb"
    registration_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "SecurePassword123",
    }
    ```

2. Run the script
   
   ```bash
   python opencart.py
   ```

3. Monitor the console and the log file for registration success or failure messages.

## Configuration

You can customize the script by editing the following variables in the code:

* `url`: The URL of the registration page.
* `wait_timeout`: Timeout for waiting for elements to become clickable (in seconds).
* `short_wait`: A shorter timeout for specific actions (in seconds).
* WebDriver path and setup (e.g., ChromeDriver setup. You can use other browsers as well).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Support

This project needs a ⭐️ from you. Don't forget to leave a star ⭐️

If you like this project, please consider <b>Buying Me a Coffee.</b> 

Thanks for the Support. 😍


<div align="center">
<a href="https://www.buymeacoffee.com/syedsohan" target="_blank"><center><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;"></center></a>
</div>
