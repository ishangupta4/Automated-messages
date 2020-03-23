# Automated-messages
This python script helps user to send messages on whatsapp to the mentioned user multiple times at once automatically.

## Setup
To use this app you have to set up selenuim for python.
I used selenium for chrome to test the code on chrome browser. One can use the different browser by changing the driver. For example to use Firefox:

```python
driver = webdriver.Chrome()
```
#### Selenium Setup
To download the selenium chromedriver, clic on [link to selenium!](https://chromedriver.chromium.org/downloads)

Install the python library for selenium:
###### Linux
use this command in terminal
```
pip3 install selenium
```
###### windows
use this command in command prompt (after setting the path variable)
```
pip install selenium
```

## How to use
* make sure the class names and xpath used are also similar for your web version of whatsapp. As of March 23, 2020 it is working, but may get modified by whatsapp in future
* **Run** the python file *wbot.py*
* Scan the QR code from your phone
* Enter the name of user or group to whome you want to send messages
* Enter the content of message
* Enter the number of times you want to send the message
* press **enter**

*If you find any bug in the code, do let me know*
contact me here:
**email** - *ishangupta004@gmail.com*
**twitter** - *@ishangupta04*