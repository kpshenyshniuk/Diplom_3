UI Automation Testing Project

This project is an automated UI testing framework for a web application using Selenium and Pytest.

Project Structure

Diplom_3/
│-- conftest.py        # Pytest configuration and fixtures
│-- locators.py        # Locators for web elements
│-- links.py           # URLs for the tested application
│-- helpers.py         # Utility functions for Selenium
│-- data.py            # Test data
│-- tests/             # Test cases
│   ├── test_main_page.py
│   ├── test_profile_page.py
│   ├── test_order_history_page.py
│-- allure-results/    # Directory for Allure test reports
│-- requirements.txt   # Project dependencies
│-- README.md          # Project documentation

Prerequisites

Ensure you have Python installed (preferably Python 3.8+). You also need to install the dependencies:

pip install -r requirements.txt

Running Tests

To execute tests with Pytest:

pytest tests/

Running Tests on Different Browsers

To run tests on Chrome:

pytest tests/ --browser=chrome

To run tests on Firefox:

pytest tests/ --browser=firefox

Generating Allure Reports

To generate an Allure report, run:

pytest --alluredir=allure-results
allure serve allure-results

Troubleshooting

Ensure that the correct WebDriver is installed for your browser.

If a test fails due to an element not being found, check the locators in locators.py.

Make sure the test environment matches the expected site structure.

Contributors

Author: [Pshenyshniuk Kostiantyn]
