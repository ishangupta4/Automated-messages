from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

name = input('enter the name of chat: ')
msg = input('enter the message: ')
count = int(input('enter the number of times you want to send the message: '))

input('enter anything after scanning QR code!')

user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print("loop count: " + str(i+1))
    