import os
import csv
import pandas

csv_filepath = "APPL.csv"

df = pandas.read_csv(csv_filepath)

historical_data = df.to_dict("records")

print(historical_data[0])

prices = []
for x in historical_data:
    if historical_data.index(x) == 50:
        for y in historical_data:
            print(y)
            if historical_data.index(x)-historical_data.index(y) < 50:
                if historical_data.index(x)-historical_data.index(y) > 0:
                    prices = prices.append(y)


print(prices)

        