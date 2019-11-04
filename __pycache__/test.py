from selenium import webdriver


usernameStr = '28arpit2000sharma@gmail.com'
passwordStr = 'iluvdadu'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

# fill in username and hit the next button

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

password = browser.find_element_by_xpath('//input[@type="password"]')
password.send_keys(passwordStr)


signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
