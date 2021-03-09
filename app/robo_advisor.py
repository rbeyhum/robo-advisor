# app/robo_advisor.py file

import requests
import os
import datetime 
import json
import csv 
from pandas import read_csv
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

# this function is used to convert from normal number to a currency (as to say)

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"

run_time_date = datetime.datetime.now()

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

def analysis(prices_dict):

    latest_day = prices_dict["Meta Data"]["3. Last Refreshed"]
    tsd = prices_dict["Time Series (Daily)"]
    all_dates = list(tsd.keys())
    sorted_dates = sorted(all_dates, reverse=True)
    matching_date = sorted_dates[0] #since first item in the list is the most recent date
    latest_close_price = tsd[matching_date]["4. close"]
    high_prices = []
    low_prices = []

    #for loop to find the recent high and recent low
    for date in all_dates:
        high_price = tsd[date]["2. high"]
        low_price = tsd[date]["3. low"]
        high_prices.append(float(high_price))
        low_prices.append(float(low_price))

    recent_high = max(high_prices)
    recent_low = min(low_prices)

    results = {"Latest Price": latest_close_price, 
                "Recent High": recent_high,
                "Recent Low": recent_low,
                "Latest day": latest_day}
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for date in all_dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume": daily_prices["5. volume"]
            })
    return results

while True:
    user_ticker = input("Please input the stock ticker you would like to analyze: ")
    # data validation (prelim) - if an invalid input then no HTTP request
    if user_ticker.isalpha() or 1<= len(user_ticker) >=5:
        ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&apikey="+ALPHAVANTAGE_API_KEY
        response = requests.get(request_url)
        parsed_response = json.loads(response.text) 
        
        # valid input, however the ticker does not exist 
        if list(parsed_response.keys())[0] == "Error Message":
            print("OOPS, the stock ticker you input does not exist. Please try again! ")
            exit
        else:
            analytics = analysis(parsed_response)
            # initializing a string in order to print it later on (for the recommendation)
            # worked on the recommendation part with Susanna 
            recommendation = ""
            recommendation_reason = ""
            risk_acceptable = input("Please enter a valid risk threshold for you investment where the value must be between 1 and 10: ")
            percentage_risk = float(risk_acceptable)/20
            if (float(analytics["Latest Price"])-float(analytics["Recent Low"]))/float(analytics["Recent Low"]) > percentage_risk:
                recommendation+= "NO BUY!"
                recommendation_reason+= "This stock's risk is greater than your risk threshold."
            else:
                recommendation+= "BUY!"
                recommendation_reason+= "This stock's risk lies within your desired risk threshold."
            break
        
    else: 
        print("OOPS, this is an invalid input. Make sure to input a valid stock ticker.")
        exit
    # second part of input validation is making sure - will be nested inside the else statement 

        
print("-------------------------")
print("SELECTED TICKER: "+user_ticker.upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: "+run_time_date.strftime("%I:%M %p")+" on",run_time_date.strftime("%B %d")+", "+run_time_date.strftime("%Y"))
print("-------------------------")
print("LATEST DAY: ",analytics["Latest day"])
print("LATEST CLOSE: ",to_usd(float(analytics["Latest Price"])))
print("RECENT HIGH: ",to_usd(analytics["Recent High"]))
print("RECENT LOW: ",to_usd(analytics["Recent Low"]))
print("-------------------------")
print("RECOMMENDATION:",recommendation)
print("RECOMMENDATION REASON:",recommendation_reason)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

# whether user wants to see lineplot of prices
data_vis_in = input("Would you like to view a line graph that plots the prices of your desired stock over time? [y/n]")
if data_vis_in == "y":
    prices_df = pd.read_csv(csv_file_path)
    prices_df["timestamp"] = pd.to_datetime(prices_df["timestamp"], format="%Y-%m-%d") #got help from Carlo
    sns.lineplot(data=prices_df, x="timestamp", y="close")
    plt.xlabel("Date")
    plt.ylabel("Closing Price of "+user_ticker)
    plt.title("Prices of "+user_ticker+" over time")
    print("Please close graph once you are done analyzing it!")
    plt.show()
    exit
else:
    exit



# whether the user wants to see extra analysis

added_bonus = input("Would you like to see a more detailed analysis for your desired ticker? [y/n]")

if added_bonus == "y":
    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
    request_url_new = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&outputsize=full&apikey="+ALPHAVANTAGE_API_KEY
    response_new = requests.get(request_url_new)
    parsed_response_new = json.loads(response_new.text)
    tsd_new = parsed_response_new["Time Series (Daily)"]
    all_dates_new = list(tsd_new.keys())
    sorted_dates_new = sorted(all_dates_new, reverse=True)
    
    #print(tsd_new)
    high_prices_new = []
    low_prices_new = []
    
    
    #while num_days < 252:
    for datenew in sorted_dates_new[0:252]: #this is a rough estimate for 52 weeks
        high_price_new = tsd_new[datenew]["2. high"]
        low_price_new = tsd_new[datenew]["3. low"]
        high_prices_new.append(float(high_price_new))
        low_prices_new.append(float(low_price_new))
        
        

    fifty_two_high = max(high_prices_new)
    fifty_two_low = min(low_prices_new)
    
    print("CAREFUL! Stock splits here are not accounted for.")
    print("-------------------------")
    print("52 WEEK HIGH: ", to_usd(fifty_two_high)) 
    print("52 WEEK LOW: ",to_usd(fifty_two_low))

else:
    exit

    



