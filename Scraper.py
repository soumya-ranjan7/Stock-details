from bs4 import BeautifulSoup
import requests
import re

s=input()                                               # stock name

url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+s+"&illiquid=0&smeFlag=0&itpFlag=0"       #URL of trading site

source_code = requests.get(url)                                                                              #source code
plain_text = source_code.text                                                                                            

soup = BeautifulSoup(plain_text,"html.parser")                                                    


 
for p in soup.findAll('span',{'id':'lastPrice'}):                             #scraping values 
    Last_price = p.string

for p in soup.findAll('div',{'id':'previousClose'}):
    PreviousDay_Closing_price = p.string

for p in soup.findAll('div',{'id':'open'}):
    Opening_price = p.string

for p in soup.findAll('div',{'id':'dayHigh'}):
    Highest_of_day = p.string


for p in soup.findAll('div',{'id':'dayLow'}):
    Lowest_of_day = p.string

for p in soup.findAll('div',{'id':'closePrice'}):
    Closing_price = p.string    
    
for p in soup.findAll('a',{'id':'pChange'}):
    Percentage_change = p.string
   
