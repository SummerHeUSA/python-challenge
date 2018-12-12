
import os
import csv


with open ("budget_data.csv",'rU') as f:
    new_row =[]
    reader = csv.reader(f)
    next(reader)
    total_profit= 0
    for row in reader:
         month, profits = row
         new_row.append([month,profits])
         value_of_row = len(list(reader)) 
         total_profit += float(row[1])
      print(new_row)
         
        #  last_month_value = month.startswith('Feb-2017')
        #  last_value = row[1]
        #  first_value_change = float(first_value)
        #  last_value_change = float(last_value)
     
        
       
      # the total is not the final one, i got incremental for each row.... how to fix it ???? 
       

      





  # csvreader = csv.reader(csvfile, delimiter=',')
  #   c=0
  #   next(csvreader)
  #   for line in csvreader:
  #         c=c+1
  #         print(line)
  #   print(f'there are {c} rows')


    
#     month = row[0].split('-')
#     print(month)
  


# print(len(new_row[0]))

# with open ('conversion_paths.csv','rU') as f:
#     new_row = []
#     reader = csv.reader(f)
#     for row in reader:
#         next (reader)
#         channel_path, conversions, value = row
#         new_row.append([channel_path,conversions,value])
#         first_source = row[0].split('>')[0].strip()
#     print (first_source)