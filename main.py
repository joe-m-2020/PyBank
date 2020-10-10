import os

# Module for reading CSV files
import csv

budget_csv= os.path.join('resources', 'budget_data.csv')

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
    
    # since each index is a new month, the total number of lines after the header are the total months 
    # months = 0
    # for line in python_csvfile:
    #     months = months + 1

    # print("Total months: ", months)


    months = 0
    profit_loss = []
    change = []
    first_num = 0
    
    
    for row in python_csvfile:
        profit_loss.append(int(row[9:-1]))
        months = months + 1

    for i in range(len(profit_loss)-1):
        change.append(profit_loss[i+1]-profit_loss[i])
        average_chage = average(change)


    print("Total Months: ", months)
    print("Total profit: ", sum(profit_loss))
    print("Average Change: ", average_chage)
 

    
