import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service('C:/Users/chromedriver-win32/chromedriver.exe')
chrome_option = Options()
chrome_option.add_experimental_option('detach',True)
chrome_option.add_experimental_option('excludeSwitches',['enable-logging'])
chrome_option.add_argument('--ignore-certificate-error')
chrome_option.add_argument('--ignore-ssl-error')

driver = webdriver.Chrome(service=s,options=chrome_option)


#list of all indian international airports
all_airport = ['BLR-Bengaluru','DEL-Delhi','GOI-Goa', 'AYJ-Ayodhya', 'ISK-Nashik', 'COK-Kochi',
    'GAY-Gaya', 'BHO-Bhopal', 'ATQ-Amritsar', 'NAG-Nagpur', 'SXR-Srinagar',
     'TRV-Thiruvananthapuram',  'IXM-Madurai', 'TRZ-Tiruchirappalli',
    'CJB-Coimbatore', 'STV-Surat', 'HYD-Hyderabad', 'VTZ-Visakhapatnam', 'RPR-Raipur', 'IXA-Agartala', 
    'IXZ-Port Blair', 'IDR-Indore', 'BBI-Bhubaneswar', 'JAI-Jaipur', 'GAU-Guwahati', 'IMF-Imphal',
    'LKO-Lucknow', 'IXE-Mangaluru', 'CNN-Kannur', 'MAA-Chennai', 'PNQ-Pune', 'AMD-Ahmedabad', 'CCJ-Kozhikode']



def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height  
       

def wait():
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "divFlightList")))
    except Exception:
        time.sleep(3)
        



for airport1 in all_airport:
    for airport2 in all_airport:
        if airport1 != airport2:
            driver.get(f'https://flight.easemytrip.com/FlightList/Index?srch={airport1}-India|{airport2}-India|16/07/2025&px=1-0-0&cbn=0&ar=undefined&isow=true&isdm=true&lang=en-us&CouponCode=&ompAff=&bc=&ISWL=&isRL=true&CCODE=IN&curr=INR&apptype=B2C')
            wait()
            
            #Xpath of all cabin class            
            class_options = [
                '//*[@id="OPT_ECONOMY"]',
                '//*[@id="OPT_PREMIUM_ECONOMY"]',
                '//*[@id="OPT_BUSINESS"]',
                '//*[@id="OPT_FIRST_CLASS"]'
            ]

            for option_xpath in class_options:
                try:  
                    
                    # select a cabin class   
                    driver.find_element(by=by.By.XPATH, value=option_xpath).click()
                    wait()
                    
                    # search selected cabin class flights
                    driver.find_element(by=by.By.XPATH, value='//*[@id="divSearchFlight"]').click()
                    wait()

                    scroll_to_bottom()
                    
                    html = driver.page_source
                    
                    with open(f'{airport1}.html', 'a', encoding='utf-8') as f_file:
                        f_file.write(html)
                    
                except Exception:
                    break