import os

# Module for reading CSV files
import csv

budget_csv= os.path.join('resources', 'budget_data.csv')

#function to find average of change in profit/loss
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
        return total / length
 
# budget_info(Date)
with open(budget_csv, 'r') as python_csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(python_csvfile, delimiter=',')

    header = next(csvreader)
    
   

    #define variables

    
    #lists to add columns profit loss and dates as well as change in profit loss to calculate average and min
    profit_loss = []
    date = []
    change = []
    months = 0

    #slice original data and change numbers to integer and separate dates into lists profit_loss and date
    #the number of rows = the number of months since it is 1 row per month
   
    for row in python_csvfile:
        profit_loss.append(int(row[9:-1]))
        date.append(row[0:8])
        months = months + 1

    
    #subtract the first number in the iteration from the second number and pass the average function to solve
    #for average change
    for i in range(len(profit_loss)-1):
        change.append(profit_loss[i+1]-profit_loss[i])
        average_change = average(change)

    '''''
    !!!!!!!!!!!!average change should be -2315.12!!!!!!!!!!!!

    '''''
    
    #find greatest increase in list "change" with min and max
    #use the index function of the greatest increase and decrease then print the gi_increase +1 and gd_increase +1
    #because the change list starts on row index 1 comparatively if the date and PL start on 0
    greatest_decrease = min(change)
    greatest_increase = max(change)
    gd_index = change.index(greatest_decrease)
    gi_index = change.index(greatest_increase)


    # print data summary
    print("Financial Analysis")
    print(f"Total Months: {months}")
    print(f"Total profit: {sum(profit_loss)}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase: {date[gi_index+1]} (${change[gi_index]})")
    print(f"Greatest Decrease: {date[gd_index+1]} (${change[gd_index]})")

    
