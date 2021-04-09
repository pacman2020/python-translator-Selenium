from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://web.whatsapp.com/'

texto = ['Pacman-2020']

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get(url)

sleep(7)
search = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')

sleep(3)
search.send_keys('Pacman-2020')

sleep(2)
search.send_keys(Keys.RETURN)

sleep(3)
campo = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
sleep(2)
campo.send_keys('teste bot')
sleep(2)
campo.send_keys(Keys.RETURN)
# driver.close()