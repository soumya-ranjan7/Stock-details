from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def GetStock():
    return render_template("GetStock.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    new_text = text.upper()
    return render_template("StockInfo.html",)

if __name__ == '__main__':
    app.run(debug=True)
