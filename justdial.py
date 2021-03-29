from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep 
from openpyxl import load_workbook, cell
import openpyxl
import csv
import xlsxwriter



import pandas as pd
import time
import os

MAX_PAGE_NUM=49 
# for 0 to page 50

nameList = []
addressList = []
numbersList = []
ratingList=[]


for pg in range(0,MAX_PAGE_NUM+1):
    page_num=("page-"+ str(pg))
    driver = webdriver.Chrome(executable_path=r"C:\Users\Rohan\Downloads\chromedriver")
    urlmod="https://www.justdial.com/Mumbai/Ayurvedic-Doctors/nct-10029616/" + page_num

    driver.get(urlmod)
    driver.switch_to.window(driver.window_handles[1])
    def strings_to_num(argument): 
        
        switcher = { 
            'dc': '+',
            'fe': '(',
            'hg': ')',
            'ba': '-',
            'acb': '0', 
            'yz': '1', 
            'wx': '2',
            'vu': '3',
            'ts': '4',
            'rq': '5',
            'po': '6',
            'nm': '7',
            'lk': '8',
            'ji': '9'
        } 
        
        return switcher.get(argument, "nothing")


    
    sleep(5) 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
    sleep(5)
    storeDetails = driver.find_elements_by_class_name('store-details')
    #myFile = open('csv-write-data.csv', 'w')
    



    #driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL, Keys.END);
    for i in range(len(storeDetails)):
        
        name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
        address = storeDetails[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')
        contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
        
        
        myList = []
        
        for j in range(len(contactList)):
            
            myString = contactList[j].get_attribute('class').split("-")[1]
        
            myList.append(strings_to_num(myString))

        nameList.append(name)
        addressList.append(address)
        numbersList.append("".join(myList))
    
    
    # driver.close()
    
    # driver.close()
    
    


print("Done")
#print(addressList)
#print(numbersList)



   

workbook = xlsxwriter.Workbook('D:\\dev_\justdial.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0    
for item in nameList:
   worksheet.write(row, column, item)
   
   row+=1

row = 0
column = 0 
for i in addressList :
   worksheet.write(row,1,i)
   row+=1

row = 0
column = 0 
for j in numbersList :
   worksheet.write(row,2,j)
   row+=1



#wk.save("")
workbook.close()
# intialise data of lists.



