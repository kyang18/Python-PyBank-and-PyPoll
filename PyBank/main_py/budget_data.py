#Create file paths across operating systems and read the csv file
import os
import csv 

# Module for reading the csv file 
csvFile = os.path.join('..','resources','budget_data.csv')

# Set variables
csvDataset = []
csvDataset_Month = []
csvDataset_Amount = []

# Open the Csv
with open(csvFile,'r') as bankFile:
        csvRead = csv.reader(bankFile,delimiter=',')
        
        #print(csvRead)                                 
        csv_header = next(csvRead)                      
       
        #print(f"CSV Header: {csv_header}")
        for row in csvRead:

            csvDataset.append(row)                      
            csvDataset_Month.append(row[0])             
            csvDataset_Amount.append(int(row[1]))       


# The total number of months included in the dataset
total_months = len(csvDataset_Month)

# The net total amount of "Profit/Losses" over the entire period
net_total = 0                                           
for month, amount in csvDataset:                       
    net_total += int(amount)                          

# The average change in "Profit/Losses" over the entire period
changeAmount = 0                                              
monthChange = []            
for amount in range(1,len(csvDataset_Amount)):     
    monthChange.append(csvDataset_Amount[amount] - csvDataset_Amount[amount-1])

changeAmount= round(sum(monthChange) / len(monthChange),2)   

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses(date and amount) over the entire period
for amount in range(1,len(csvDataset_Amount)):        
    maxIncr = max(monthChange)                            
    maxIncrIndex = monthChange.index(maxIncr)             
    maxDecr = min(monthChange)                             
    maxDecrIndex = monthChange.index(maxDecr)             

monthMaxIncr = csvDataset_Month[maxIncrIndex + 1]       
monthMaxDecr = csvDataset_Month[maxDecrIndex + 1]      

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------") 
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${changeAmount}")
print(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})")
print(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})")

#  Export a text file with the results
output = open("PyBank.txt", 'w')
output.write("Financial Analysis\n") 
output.write("----------------------------\n")   
output.write(f"Total Months: {total_months}\n")
output.write(f"Total: ${net_total}\n")
output.write(f"Average Change: ${changeAmount}\n")
output.write(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})\n")
output.write(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})\n")
