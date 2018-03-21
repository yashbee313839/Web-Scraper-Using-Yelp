import xlwt
import xlrd
import time
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
loc=''
def m(loc):
    base_url="https://www.yelp.com/search?find_desc=Restaurants&find_loc="
    page=0
    url=base_url + loc + "&start=" + str(page)
    r=requests.get(url)
    bsoup=BeautifulSoup(r.text,'html.parser')
    my_data=[]
    while page<201:
        arr=bsoup.find_all('div',{'class':'biz-listing-large'})
        for biz in arr:
            d={}
            name1=biz.find_all('a',{'class':'biz-name'})[0].text
            add=biz.find_all('address')[0].text.replace(' ','')
            phone=biz.find_all('span',{'class':"biz-phone"})[0].text.replace(' ','')
            d['ALL_name']=name1
            d['Full adress']=add
            d['Phone']=phone
            my_data.append(d)
        page+=10
    return my_data
l=input("Enter city name : ")
time.sleep(1)
print("Creating :) ")
result=m(l)
time.sleep(2)
data1=pd.DataFrame(result)
data1.columns=['Full name','Adress','Mobile no']
data1.to_excel('C:\Python34\{}_file.xls'.format(l))
print('The File has been created')
print('Press y/n to see your file')
ch=input()
f='C:\Python34\{}_file.xls'.format(l)
if ch=='y':
    print('Please wait')
    os.startfile(f)
if ch=='n':
    print("Thank you!")
