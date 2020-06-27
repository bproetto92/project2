import os
import csv
import pandas

import matplotlib
from matplotlib import pyplot
from matplotlib import dates
import datetime
import matplotlib.pyplot as plt


# utility function to convert float or integer to usd-formatted string (for printing)

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

#USER INPUT FOR STOCK / COMPANY

file = input("Please select one of the following Stocks - AAPL, GOOG, NFLX, FB: ")

if file != "AAPL":
    if file != "GOOG":
        if file != "NFLX":
            if file != "FB":
                print("Sorry, your selection does not match any stocks")
                exit()

csv_filepath = file+".csv"

df = pandas.read_csv(csv_filepath)

historical_data = df.to_dict("records")

#Calculating List of 50-day moving averages
averages1 = []
prices = []
for x in historical_data:
    if historical_data.index(x) >= 200:
        prices = []
        for y in historical_data:
            if historical_data.index(x)-historical_data.index(y) < 50:
                if historical_data.index(x)-historical_data.index(y) > -1:
                    prices.append(y)
                    date = y['Date']
        average_value = sum(x['Close'] for x in prices) / len(prices)
        average_dictionary = {'Date': date, 'Average': average_value}
        averages1.append(average_dictionary)          

#Calculating List of 200-day moving averages
averages2 = []
averages2plot = []
prices = []
for x in historical_data:
    if historical_data.index(x) >= 200:
        prices = []
        for y in historical_data:
            if historical_data.index(x)-historical_data.index(y) < 200:
                if historical_data.index(x)-historical_data.index(y) > -1:
                    prices.append(y)
                    date = y['Date']
        average_value = sum(x['Close'] for x in prices) / len(prices)
        average_dictionary = {'Date': date, 'Average': average_value}
        averages2.append(average_dictionary)     


#CREATING MOVING AVERAGES PLOTS


datelist = []
pricelist = []

for x in averages2:
    converted_date = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d']))
    datelist.append(x['Date'])
    prices = (x['Average'])
    pricelist.append(prices)


converted_dates = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d']))
x_axis = converted_dates
formatter = dates.DateFormatter('%Y-%m-%d')
plt.plot( x_axis, pricelist, marker=' ', color = 'blue', linewidth=2,label="200-day moving average")

datelist = []
pricelist = []

for x in averages1:
    converted_date = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d']))
    datelist.append(x['Date'])
    prices = (x['Average'])
    pricelist.append(prices)



converted_dates = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d']))
x_axis = converted_dates
formatter = dates.DateFormatter('%Y-%m-%d')
plt.plot( x_axis, pricelist, marker=' ', color = 'red', linewidth=2,label="50-day moving average")

plt.legend(loc="upper left")
plt.title(file+' Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#CALCULATING AND REPORTING MOMENTUM INDICATORS
print("-----------------------------------------")
print("Welcome to the Momemtum Stock Analysis Tool")
print("-----------------------------------------")
print("The following Momentum Events for Stock",file,"have occurred recently:")

#Finding Date of Gold Cross
for x in averages1:
    if averages1.index(x) != len(averages1):
        if averages1[averages1.index(x)]['Average'] < averages2[averages1.index(x)]['Average']:
            if averages2[averages1.index(x)+1]['Average'] < averages1[averages1.index(x)+1]['Average']:
                print("A Gold Cross occurred on", averages1[averages1.index(x)+1]['Date'])


#Finding Date of Death Cross
for x in averages1:
    if averages1.index(x) != len(averages1)-1:
        if averages1[averages1.index(x)]['Average'] > averages2[averages1.index(x)]['Average']:
            if averages2[averages1.index(x)+1]['Average'] > averages1[averages1.index(x)+1]['Average']:
                print("A Death Cross occurred on", averages1[averages1.index(x)+1]['Date'])

print("-----------------------------------------")