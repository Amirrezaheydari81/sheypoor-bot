from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from unidecode import unidecode

# PROXY = "89.43.10.141:80"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome = webdriver.Chrome(chrome_options=chrome_options)

url = "https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85/%D8%A2%D8%B1%D8%A7%DB%8C%D8%B4%DA%AF%D8%B1-%D8%A7%D9%BE%DB%8C%D9%84%D8%A7%D8%B3%DB%8C%D9%88%D9%86-%DA%A9%D8%A7%D8%B1"

f = open("number.txt", "a")

driver = webdriver.Chrome()
driver.get(url)


showmore = driver.find_element(By.XPATH, '/html/body/main/section[3]/section/button')
showmore.click()
for x in range(1, 5):
    time.sleep(2)
    url = "/html/body/main/section[3]/div/div/div/article[" + str(x) +"]"
    driver.find_element(By.XPATH,url).click()


    time.sleep(2)
    callbtn = driver.find_element(By.XPATH,'/html/body/main/div[2]/div[2]/section/span[1]')
    callbtn.click()

    time.sleep(1)
    enNumber = unidecode(callbtn.text)
    f.write(enNumber + '\n')


    driver.execute_script("window.history.go(-1)")        
f.close()