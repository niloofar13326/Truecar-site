import mysql.connector
import requests
from bs4 import BeautifulSoup
#import re
mydb=mysql.connector.connect(user="root",password="niloofar",host="localhost",database='truecar')
cursor=mydb.cursor()
name=input('what is your favourite brand?')
result=requests.get('https://www.truecar.com/shop/used/?filterType=brand')
soup=BeautifulSoup(result.text,'html.parser')
val=soup.find_all('div',attrs={'data-test':"modelSearchBrand"})

result3=requests.get('https://www.truecar.com/used-cars-for-sale/listings/')
soup3=BeautifulSoup(result3.text,'html.parser')
val3=soup3.find_all('div', attrs={'data-test':"vehicleCardTrim"})


count=0
list=[]
for n in range(0,100):
    print(n)
    a = val3[n]
    print(a.text)
    if n==0 or n==1:

        if name in a.text:
            print('count1',count)
            list.append(a.text)
            print(list)
            count = +1
            print('count2',count)
            if count == 20:
                print(2)
                break
    elif n>2:
        result2=requests.get('https://www.truecar.com/used-cars-for-sale/listings/'+'?page='+str(n)+'&sort[]=best_match')
        soup2 = BeautifulSoup(result2.text, 'html.parser')
        val2 = soup2.find_all('span', attrs={'class': "vehicle-header-make-model text-truncate"})
        a = val2[n]
        if name in a.text:
            print('count3',count)
            print(a.text)
            count=+1
            list.append(a.text)
            print(list)
            if count==20:
                print(2)
                break


