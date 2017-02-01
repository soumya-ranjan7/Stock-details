from flask import Flask
from flask import request
from flask import render_template
from bs4 import BeautifulSoup
import requests
import json


app = Flask(__name__)

@app.route('/')
def GetStock():
    return render_template("GetStock.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    stock_name = text.upper()

    url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+stock_name+"&illiquid=0&smeFlag=0&itpFlag=0"      
    source_code = requests.get(url)                                                                         
    plain_text = source_code.text                                                                                            

    soup = BeautifulSoup(plain_text,"html.parser")
    p  = soup.find('div',{'id':'responseDiv'})                        

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
    
    stock_details={"Last price ":Last_price, "PreviousDay Closing price":PreviousDay_Closing_price , "Opening price":Opening_price  , "Highest of day":Highest_of_day
                   , "Lowest of day ":Lowest_of_day, "Closing price":Closing_price , "Percentage change":Percentage_change}
       
    return render_template ("StockInfo.html",details=stock_details)




if __name__ == '__main__':
    app.run(debug=True)
