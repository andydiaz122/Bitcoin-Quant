# This program finds how many green days vs red in btc history since April 2013

import sys
import csv 


# grab data from csv file
file = open ("BITFINEX_BTCUSD_1D.csv")
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader) 

# find open price and close price from each day
rows = []
price_open = []
price_close = []
for row in csvreader:
	rows.append(row)

price_open = [i[1] for i in rows]
price_close = [i[4] for i in rows]

# subtract -> price_close - price_open = difference in price 
# if difference in price is positive then add tally to positive_day_tally
# elseif price is negative add tally to negative_day_tally
# else add tally to same_price_tally
price_difference = []
positive_day_tally = 0
negative_day_tally = 0
same_price_tally = 0
for i in range(int(len(price_open)/1.25),len(price_open)):
#for i in range(len(price_open)):
	result = float(price_open[i]) - float(price_close[i])
	if result > 0:
		positive_day_tally = positive_day_tally + 1
	elif  result < 0:
		negative_day_tally = negative_day_tally + 1
	else:
		same_price_tally = same_price_tally + 1 
	price_difference.append(result)

# print amount of green days vs red days
print("# of green days = ", positive_day_tally)
print("# of red days = ", negative_day_tally)

file.close()