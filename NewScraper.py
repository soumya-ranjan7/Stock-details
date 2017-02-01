from bs4 import BeautifulSoup
import requests
import json

s=input()                                               # stock name

url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+s+"&illiquid=0&smeFlag=0&itpFlag=0"       #URL of trading site

source_code = requests.get(url)                                                                              #source code
plain_text = source_code.text                                                                                            

soup = BeautifulSoup(plain_text,"html.parser")


 
for p in soup.find('div',{'id':'responseDiv'}):                             #scraping values 
    s=p.strip(' ')
    data=json.loads(s)
    info=data['data']
    info1=info[0]
    print(info1)
    
    

PreviousDay_Closing_price = info1["previousClose"]
    
Opening_price = info1["open"]

Highest_of_day = info1["dayHigh"]

Lowest_of_day = info1["dayLow"]

Closing_price = info1["closePrice"]
    

Percentage_change = info1["pChange"]
   
