from selenium import webdriver
import time

options = webdriver.ChromeOptions() #gets rid of bitchass error
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

list = open("tickerstest.txt", "r+")
comp_list = open("company.txt", "w")

def transfer(ticker):
    browser.get("http://wikipedia.org/wiki/"+str(ticker))
    time.sleep(1) #allows selenium to process shit bc slow
    comp_url = browser.current_url
    comp_list.write(comp_url+'\n')
    print(comp_url+'\n')

for line in list:
    transfer(line)

