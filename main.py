import os

# Module for reading CSV files
import csv

budget_csv= os.path.join('resources', 'budget_data.csv')


# def budget_info(budget_list):
#     Date = str(budget_list[0])
#     PL = int(budget_list[1])
 
# budget_info(Date)
with open(budget_csv, 'r') as python_csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(python_csvfile, delimiter=',')

    header = next(csvreader)
     

    for line in python_csvfile:
        print(line)

