import os
import csv
import pandas

csv_filepath = "APPL.csv"

df = pandas.read_csv(csv_filepath)

historical_data = df.to_dict("records")


averages = []
prices = []
for x in historical_data:
    if historical_data.index(x) >= 50:
        
        prices = []
        for y in historical_data:
            if historical_data.index(x)-historical_data.index(y) < 50:
                if historical_data.index(x)-historical_data.index(y) > -1:
                    prices.append(y)
                    date = y['Date']
        average_value = sum(x['Close'] for x in prices) / len(prices)
        average_dictionary = {'Date': date, 'Average': average_value}
        averages.append(average_dictionary)          

        