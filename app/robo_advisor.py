# app/robo_advisor.py file

import requests
import os
import datetime 
import json



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

    return results

while True:
    user_ticker = input("Please input the stock ticker you would like to analyze: ")
    #ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
    #request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&apikey="+ALPHAVANTAGE_API_KEY
    #response = requests.get(request_url)

    ## first part of input validation is to make sure that it is not a numeric input since no stock tickers contain numbers, even though input always returns a string OR less than 1 character/more than 5 characters

    #if user_ticker.isnumeric() or len(user_ticker) < 1 or len(user_ticker) > 5:
    #    print("OOPS, this is an invalid input. Make sure to input a valid stock ticker.")
    #    exit
    #    # no HTTP request here
    #else: 
    #    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
    #    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&apikey="+ALPHAVANTAGE_API_KEY
    #    response = requests.get(request_url)
    #    parsed_response = json.loads(response.text) 


    if user_ticker.isalpha() or 1<= len(user_ticker) >=5:
        ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default = "IBM")
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+user_ticker+"&apikey="+ALPHAVANTAGE_API_KEY
        response = requests.get(request_url)
        parsed_response = json.loads(response.text) 
        

        if list(parsed_response.keys())[0] == "Error Message":
            print("OOPS, the stock ticker you input does not exist. Please try again! ")
            exit
        else:
            analytics = analysis(parsed_response)
            break
        
    else: 
        print("OOPS, this is an invalid input. Make sure to input a valid stock ticker.")
        exit
    # second part of input validation is making sure - will be nested inside the else statement 

        


print("-------------------------")
print("SELECTED TICKER: "+user_ticker)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: "+run_time_date.strftime("%I:%M %p")+" on",run_time_date.strftime("%B %d")+", "+run_time_date.strftime("%Y"))
print("-------------------------")
print("LATEST DAY: ",analytics["Latest day"])
print("LATEST CLOSE: ",to_usd(float(analytics["Latest Price"])))
print("RECENT HIGH: ",to_usd(analytics["Recent High"]))
print("RECENT LOW: ",to_usd(analytics["Recent Low"]))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#print("Run at: "+run_time_date.strftime("%I:%M %p")+" on",run_time_date.strftime("%B %d")+", "+run_time_date.strftime("%Y"))

#print(type(response))
#print(response.status_code)
##print(response.text)
#breakpoint()
#

#
#latest_day = parsed_response["Meta Data"]["3. Last Refreshed"]
##
##
#tsd = parsed_response["Time Series (Daily)"]
#all_dates = list(tsd.keys())
### now here I must sort the dates that are stored inside the list in case the structure of the data changes
#sorted_dates = sorted(all_dates, reverse=True)
#matching_date = sorted_dates[0] #since first item in the list is the most recent date
##
##
#latest_close_price = tsd[matching_date]["4. close"]


