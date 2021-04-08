from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://translate.google.com.br/?sl=pt&tl=en&op=translate'

texto = 'casa nova'

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get(url)

#campo de entradas de texto
elent = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')

#inserido texto a ser traduzindo
elent.send_keys(texto)

#ante de pega o valor deve espera ate esta pronto
time.sleep(4)

#campo de texto traduzindo
outside = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text

#guarda a informação onde quizer
print('--->', outside)


driver.close()