# USUN-Ceasefire
This is a bot to send messages to USUN expressing our greatest disapproval of the US being the only country to vote against a ceasefire!

## Prerequisites

You need Python 3.x and pip (Python package installer) installed on your system.

## Installing Selenium

You can install Selenium Python bindings via pip:

```bash
pip install selenium
```
## Setting up ChromeDriver
If you're using Chrome, download ChromeDriver from here: https://sites.google.com/a/chromium.org/chromedriver/

After downloading, extract the file and set its location in your system's PATH variable. You can do this in Python code like this:

```python
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Replace '/path/to/chromedriver' with the actual path
```
## Usage
I could go on the CSUN website and spam it with messages manually, but why would I do that when I could make a bot. 
