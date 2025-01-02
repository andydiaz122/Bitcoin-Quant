# This program finds how many green vs red 1hr,10AM(Eastern Time) candles have occured
# since December 12, 2021

import sys, csv


# grab data from csv file
file = open("COINBASE_BTCUSD_1HR.csv")
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)

# grab general time
# split string and grab hourly time
# find open and close price at 10AM of each day
time_general = []
time_specific = []
temp_holder = []
rows = []


for row in csvreader:
	rows.append(row)			
	time_general.append(row[0])
	temp_holder = row[0].split('T')
	time_specific.append(temp_holder[1])		# time_specific is a list of strings


# pars through time_specific
# grab first two digits
# if hourly time == 10, grab correspinding open and close price
price_open = []
price_close = []
counter = 0
full_time = []
time_digits = []
for i in time_specific:	
	if(i[0] == '2' and i[1] == '0'):
		price_open.append(rows[counter][1])
		price_close.append(rows[counter][4])
	else:
		pass
	
	counter = counter + 1

# subtract -> price_close - price_open = difference in price 
# if difference in price is positive then add tally to positive_day_tally
# elseif price is negative add tally to negative_day_tally
# else add tally to same_price_tally
price_difference = []
positive_day_tally = 0
negative_day_tally = 0
same_price_tally = 0
for i in range(int(len(price_open)/1.1),len(price_open)):
	result = float(price_close[i]) - float(price_open[i])
	if result > 0:
		positive_day_tally += 1
	elif  result < 0:
		negative_day_tally += 1
	else:
		same_price_tally += 1 
	price_difference.append(result)

# print amount of green 1hr candles vs red 1hr, 10AM candles
print("# of green 10AM 1HR candles = ", positive_day_tally)
print("# of red 10AM 1HR candles = ", negative_day_tally)
print("ratio of green/red = ", float(positive_day_tally/negative_day_tally))
print("same price = ", same_price_tally	)
file.close()