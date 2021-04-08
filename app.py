from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://translate.google.com.br/?sl=pt&tl=en&op=translate')

#search
elent = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
elent.send_keys('casa nova')

time.sleep(3)

#ante de pega o valor deve espera ate esta pronto
outside = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text

#guarda a informação onde quizer
print('--->', outside)


driver.close()