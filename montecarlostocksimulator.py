import pandas_datareader.data as web #used to read data and find stock prices. we will be using the closing stock values
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot') #style of plot for our graph

#user information for the ticker symbol, start dates and end dates
tsymbol = input("what stock would you like to simulate? ")
ystart = int(input("what year would you like to start from? "))
mstart = int(input("which month of that year? "))
dstart = int(input("which day of that year? "))
yend = int(input("what year would you like to end on? "))
mend = int(input("which month of that year? "))
dend = int(input("which day of that year? "))

start = dt.datetime(ystart, mstart, dstart) #start date for the simulation
end = dt.datetime(yend, mend, dend) #end date for the simulation

prices = web.DataReader(tsymbol, 'google', start, end)['Close'] #getting the data from google for the stock open and close price
returns = prices.pct_change() #the returns of each change

last_price = prices[-1]

#number of simulations
num_simulations = 10
num_days = 365

simulation_df = pd.DataFrame()

#simulating possible outcomes
for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series

#printing the possible outcomes to a graph
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: ' + tsymbol)
plt.plot(simulation_df)
plt.axhline(y=last_price, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
