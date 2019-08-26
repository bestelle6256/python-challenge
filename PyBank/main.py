# 1) read the csv file
# 2) create a list to store all the dates (loop through the rows in csvreader, list.append = row[0])
# 3) create a list to store all the profit/loss (similar approach)
# 4) create a list to store all the daily change (list_daily_change[k]=list_daily_value[j]-[j-1])
# 5) count how many month (len(list_date))
# 6) sum all the elements in list_daily_value
# 7) avg daily_value = sum/n
# 8) loop through list_daily_change and figure out the max and min
# 9) print out everything

import os
import csv
import math

# read csv file
file_path = "budget_data.csv"
list_date = []
list_daily_value = []
list_daily_change = []
total_n = 0
total_pnl = 0
avg_pnl = 0

with open(file_path,"r",newline="") as file_handle:
    csvreader = csv.reader(file_handle, delimiter = ",")
    header = next(csvreader, None) 

    # creat a list for all the dates and daily value
    # data = []
    for row in csvreader:
        # data.append(row)
        list_date.append(row[0])
        list_daily_value.append(float(row[1]))

    total_n = len(list_date) # total_n = 86
    print(total_n)

    # create a list for all the daly change

    list_daily_change = [0.0]
    # print (list_daily_value[0])
    list_daily_change[0] = list_daily_value[0] # daily change for month 1 = the value of month 1
    print ("first month's change is ", list_daily_change[0])

  

    for i in range(1,total_n): # Range(1,86), looping through 1 to 85, create a new column for daily change
        list_daily_change.append(list_daily_value[i] - list_daily_value[i-1])
    
    # for j in range(8):
        # print(type(list_daily_change[j]),list_daily_change[j])
    

    total_pnl = sum(list_daily_value)
    avg_change = sum(list_daily_change)/total_n

    print("Total months: ",total_n)
    print("Total profit and loss: $",total_pnl)
    print("Average Change = $",avg_change)
    
    # ---------------------------

    max_pnl = list_daily_change[0]
    min_pnl = list_daily_change[0]

    max_index = None
    min_index = None

    for j in range(total_n): # loop through list_daily_change to find out the max and min 
        if list_daily_change[j]>max_pnl:
            max_pnl = list_daily_change[j]
            max_index = j

        if list_daily_change[j]<min_pnl:
            min_pnl = list_daily_change[j]
            min_index = j

    
    print("greatest increase is $",list_date[max_index],max_pnl)
    print("greatest decrease is $",list_date[min_index],min_pnl)