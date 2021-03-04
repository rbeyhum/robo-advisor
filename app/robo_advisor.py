# app/robo_advisor.py file

import requests
import os
import datetime 
import json



user_ticker = input("Please enter the stock ticker that you want to analyze: ")

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&apikey="+ALPHAVANTAGE_API_KEY


response = requests.get(request_url)
parsed_response = json.loads(response.text) 

#print(type(response))
#print(response.status_code)
#print(response.text)


run_time_date = datetime.datetime.now()
latest_day = parsed_response["Meta Data"]["3. Last Refreshed"]

print("-------------------------")
print("SELECTED TICKER: "+user_ticker)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: "+run_time_date.strftime("%I:%M %p")+" on",run_time_date.strftime("%B %d")+", "+run_time_date.strftime("%Y"))
print("-------------------------")
print("LATEST DAY: "+latest_day)
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

print("Run at: "+run_time_date.strftime("%I:%M %p")+" on",run_time_date.strftime("%B %d")+", "+run_time_date.strftime("%Y"))