import os
import csv
import pandas

csv_filepath = "APPL.csv"

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