"""
Shaishav Shah
This file will update live prices for a specified Ticker (eg. AAPL, FB, etc) and write these in an .csv file
Modules Required:
 - Pandas
 - BeautifulSoup
 - DateTime Module
"""


import os, os.path,csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


# Making a function which can later be added into a stock class as a method.


def getLivePrice(ticker): # Getting the live prices
    url = 'https://ca.finance.yahoo.com/quote/{0}'.format(ticker) # The url used
    response = requests.get(url) # Using requests module to get the content
    yahoo_price_html = BeautifulSoup(response.content,'html.parser') # Converting content into html code
    # print(yahoo_price_html)
    tag_with_price_and_time = yahoo_price_html.find_all(class_ = 'My(6px) Pos(r) smartphone_Mt(6px)')[0] # This is the class I need to search through, obtained through inspect element in chrome
    price = tag_with_price_and_time.find_all('span')[0].text # Price is in the 1st span element, therefore this works
    time = datetime.now().strftime("%M:%S")
    return price,time



def write_to_csv(value1, value2, ticker):
    # making directory to store Stock Data
    if not os.path.exists('StockData'):
        os.mkdir('StockData')
    #
    with open(os.path.join(os.getcwd()+"/StockData",'liveprices{0}.csv'.format(ticker)),'a+') as f: # Creates file in this directory
        f.writelines(value1 + "," + value2 + "\n")
        f.close()

def read_csv():
    with open(os.path.join(os.getcwd()+"/StockData",'liveprices{0}.csv'.format(ticker)),'r') as f:
        data = csv.reader(f)
        for row in data:
            print(row)
        print('\n')
        f.close()


if __name__ == "__main__":
    from time import sleep
    ticker = 'AMD'
    for i in range(5):
        sleep(0.7) # I calculated this time to be the difference 1 and time it takes to grab data from google
        value,time = getLivePrice(ticker)
        write_to_csv(time,value,ticker)
        read_csv()



