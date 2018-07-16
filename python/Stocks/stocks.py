
# imports the libraries
import matplotlib.pyplot as plt
import pandas as pd
import csv
import datetime
from yahoo_quote_download import yqd


# 3 inputs:
# 1) a ticker as an string – 'APPL' for example
# 2) the start date of the analysis – 'YYYYMMDD'
# 3) the end date of the analysis - 'YYYYMMDD'
# outputs a bar-chart with the following properties:
# a) the x-axis is days of the day
# b) the y-axis is the number of times the price of that day has been the maximum in that week

def stocks():
    # asks the user for the ticker, the start date, and the end date
    ticker = input('Enter the ticker (DJI, IBM, GOOGL, etc): ')
    start_date = input('Enter the start date (YYYY/MM/DD or (YYYY-MM-DD): ')
    end_date = input('Enter the end date (YYYY/MM/DD) or (YYYY-MM-DD): ')

    # formats the dates in the folowing format: 'YYYYMMDD'
    start_date = start_date.replace('-', '')
    start_date = start_date.replace('/', '')
    end_date = end_date.replace('-', '')
    end_date = end_date.replace('/', '')

    def makeData(ticker, start_date, end_date):
        # makes an array (index 0 corresponds to Monda; index 4 corresponds to Friday)
        def makeWeekday():
            return ([0] * 5)
        # creates and opens a .csv file
        with open('data.csv', 'w') as myfile:
            wr = csv.writer(myfile, delimiter='\n')
            # gets the data from the 'load_yahoo_quote' library and writes it into the .csv file
            wr.writerow(yqd.load_yahoo_quote(ticker, start_date, end_date))
        # creates a pandas dataframe to store the data in the .csv file in it
        df = pd.read_csv('data.csv')
        # counts how many days, the day of the weeks has been the maximum in that week
        weekdays = makeWeekday()
        # keeps track of the price in days of the week
        this_week = makeWeekday()
        # itterates over the rows of the dataframe
        for index, row in df.iterrows():
            # gets the date from the dataframe
            date_str = row['Date']
            format_str = '%Y-%m-%d'
            # creates a datetime object from the date
            date_object = datetime.datetime.strptime(date_str, format_str)
            # find what day of the week the date is – 0 for Monday; 4 for Friday
            day_index = date_object.date().weekday()
            # using the value provided in the 'Low' column of the row. However, 'Low' can be substituted with one of the following: 'High,' 'Open,' 'Close'
            day_value = df.at[index, 'Low']
            # adds the value of the day to the list
            this_week[day_index] = day_value
            # executes the code once the week is over; that is once friday is reached.
            if day_index == 4:
                # finds the maximum value in that week
                max_day_value = min(this_week)
                # find the index of that week, which corresponds to what day of the week the maximum value was
                max_day_index = this_week.index(max_day_value)
                # adds 1 to that day of the week
                weekdays[max_day_index] += 1
                # resets the 'this_week' list since the week is finished
                this_week = makeWeekday()
        # returs how many days each day of the week has had the maximum price of the week
        return weekdays
    # recives as input a list, indexed by day of the week, that stores how many times each day of the week has had the maximum price of the week
    # outputs a bar-graph, showing the data
    # x-axis: day of the week (Mon-Fri)
    # y-axis: number of times the day has had the maximum price of the week

    def plotData(data):
        # used to label each bar of the bar-graph
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        # used to format the colors of each bar of the bar-graph
        colors = ['#39e600', '#0066ff', '#ff3300', '#00ffff', '#ff00ff']
        # iterates over the data (days of the week)
        for i in range(len(data)):
            # makes a bar in the bar-graph
            plt.bar(i, data[i], color=colors[i])
        # adds the labels for bars on the x-axis
        plt.xticks(range(0, 5), days)
        # displays the graph to the user
        plt.show()
    # fist generates the data; then, plots the data on a graph
    return plotData(makeData(ticker, start_date, end_date))


stocks()
