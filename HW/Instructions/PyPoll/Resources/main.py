
import os
import csv
new_row = []
with open ("election_data.csv",'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        i_d, country, candidates = row
        # print ",".join(row)
 
        new_row.append([i_d,country,candidates])
        #  value = len(list(reader)) 
       print (new_row)
  
  
  
  
    value = sum(c.values())
    print (value)
