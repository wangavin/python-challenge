# First we'll import the os module. # This will allow us to create file paths across operating systems CORRECT
import os
# Module for reading CSV files CORRECT
import csv
 
Totalmonths = 0
TotalAmount = 0
Totalchange = 0
# ***1. set your variables to hold the values from your calculations CORRECT
ProfitLosseslist = []

# looking CVS file location CORRECT
csvpath = os.path.join('Resources', 'budget_data.csv')

# Improved Reading using CSV module CORRECT
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents CORRECT
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header) CORRECT
    csv_header = next(csvreader)

    # Read each row of data after the header CORRECT
    for row in csvreader:

        Totalmonths += 1
        TotalAmount += int(row[1])
#***2. assign your Previous_number to the first row's profit value   
        curr_number = int(row[1]) # curr_number is showing at the end of Row 87 382539 CORRECT
        ProfitLosseslist.append(curr_number) # this will help skip each loop reduce 1 set number, undtil show the first to stop. CORRECT
        
    Templist = []
# below loop is under the list and using index pickup number location    
    for i in range (0, 85): # this is index
        FirstNum = ProfitLosseslist[i] # i mean is  
        SecondNum = ProfitLosseslist[i+1]
        TempAns = SecondNum -FirstNum # this is 1 position of under 85 number
        Templist.append(TempAns)
    Avg = sum(Templist)/ (Totalmonths-1) #the reason "-1" is I need to get 85 number instead of 86 month. When location1 - location2 there is = 1st answer, so location2 - location3 = 2nd answer....etc

Greatesr_inc = max (Templist)
Greatesr_dec = min (Templist)

output = f"""
Financial Analysis
----------------------------
Total Months: {Totalmonths}
Total: ${TotalAmount}
Average Change: {(round(Avg,2))}
Greatest Increase in Profits: Aug-16 ({Greatesr_inc})
Greatest Decrease in Profits: Feb-14 ({Greatesr_dec})
"""

print (output)  

with open("analysis/budget_output.txt", "w") as outfile:
    outfile.write(output)

