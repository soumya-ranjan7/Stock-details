from bs4 import BeautifulSoup
import requests
import json

                                               # stock name


url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+s+"&illiquid=0&smeFlag=0&itpFlag=0"       #URL of trading site

source_code = requests.get(url)                                                                              #source code
plain_text = source_code.text                                                                                            

soup = BeautifulSoup(plain_text,"html.parser")


 
p  = soup.find('div',{'id':'responseDiv'})                             #scraping values 
data = json.loads(p.string)
info=data['data']
info1 = info[0]

    
Last_price = info1["lastPrice"]    

PreviousDay_Closing_price = info1["previousClose"]
    
Opening_price = info1["open"]

Highest_of_day = info1["dayHigh"]

Lowest_of_day = info1["dayLow"]

Closing_price = info1["closePrice"]
    

Percentage_change = info1["pChange"]

stock_detail=["Last price ", "PreviousDay Closing price" , "Opening price" , "Highest of day" , "Lowest of day ", "Closing price" , "Percentage change"]
stock_price=[Last_price , PreviousDay_Closing_price , Opening_price , Highest_of_day , Lowest_of_day , Closing_price , Percentage_change ] 
   
