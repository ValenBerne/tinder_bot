from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from user import mail, password
from selenium.webdriver.common.action_chains import ActionChains
import traceback

driver = webdriver.Chrome()
actions = ActionChains(driver)
 
main_window = driver.window_handles[0] #guarda la ventana principal para poder switchear
driver.maximize_window()
driver.get("https://www.tinder.com")
sleep(10)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click() #Acepto las cookies
sleep(5)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
 
login_popup = driver.window_handles[1]
driver.switch_to_window(login_popup)
mailTextBox = driver.find_element_by_xpath('//*[@id="email"]')
mailTextBox.send_keys(mail)
sleep(2)
passTextBox = driver.find_element_by_xpath('//*[@id="pass"]')
passTextBox.send_keys(password)
passTextBox.send_keys(Keys.RETURN)
sleep(5)
 
driver.switch_to_window(main_window)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
 
like = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
 
sleep(5)
for i in range(100):
    sleep(2)  
    try:
        sleep(2)
        actions.send_keys(Keys.SPACE)
        actions.perform()
    except:
        print(traceback.format_exc())
    try:
        sleep(2)
        actions.send_keys(Keys.SPACE)
        actions.perform()
    except:
        print(traceback.format_exc())
    try:
        sleep(2)
        actions.send_keys(Keys.SPACE)
        actions.perform()
    except:
        print(traceback.format_exc())
    sleep(2)
    like.click()