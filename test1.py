from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.google.com')
driver.close()
print("Test Finish")
