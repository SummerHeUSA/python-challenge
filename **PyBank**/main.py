/Users/summerhe/Desktop/python-challenge/**PyBank**
import os
import csv

csvpath = os.path.join('..', 'Rsources', 'budget_data.csv')

with open (csvpath, "rU") as f:
     reader = csv.reader(f)
     for row in reader:
         month, p_l  = row
    print(row 

