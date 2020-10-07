import os

# Module for reading CSV files
import csv

csvpath = os.path.join('resources', 'budget_data.csv')



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)