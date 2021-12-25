import telebot
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://yandex.ua/pogoda/raihorodok?lang=ru&lat=48.900188&lon=37.724086')

weather = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/a/div[1]/span[2]')
print(weather.text)

input()





