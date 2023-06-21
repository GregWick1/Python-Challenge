import os
import csv
# Import os and csv and create a variable to store your csv file
csv_path = os.path.join('Resources','budget_data.csv')
# Create 3 lists 
total_months = []
total_profit = []
profit_change_list = []



# Read the csv file into python as budget reader
with open(csv_path, 'r') as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=',')
    
    header = next(budget_reader)
    #Use a for loop for each row in the budget reader
    for row in budget_reader:
        #Store the date row in the total months list
        total_months.append(row[0])
        #Store the profit/losses row as integers in the total profit list
        total_profit.append(int(row[1]))
    #Use a for loop to loop the range of the total profit 
    #Subtracting one from the range because the last value would be subtracted from a row that doesnt exist 
    #Which would give an incorrect mean    
    for i in range(len(total_profit) -1):
        #Store the profit/losses change every month in the profit_change_list using i+1 to get the next months profit/losses
        profit_change_list.append(total_profit[i+1]-total_profit[i])
       
    sum_total_profit = sum(total_profit)
    len_total_months = len(total_months)
    #Find the greatest and least profit/loss changes
    max_total_profit = max(profit_change_list)
    min_total_profit = min(profit_change_list)
    #To find the corresponding month use the index function to find the integer value of max/min profit change and add 1 to it 
    #Because we subtracted 1 in the range function 
    max_month = profit_change_list.index(max(profit_change_list)) + 1
    min_month = profit_change_list.index(min(profit_change_list)) + 1
    #Used to find the average change of the profit/losses column
    average_change = round(sum(profit_change_list)/len(profit_change_list),2)
    
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {len_total_months}')
    print(f'Total: ${sum_total_profit}')
    print(f'Average Change: ${average_change}')
    #To match the months we put the max month into the total months list to give us the correct string for the month
    print(f'Greatest Increase: {total_months[max_month]} ${max_total_profit}')
    print(f'Greatest Decrease: {total_months[min_month]} ${min_total_profit}')
    
    analysis_file = os.path.join("Analysis", "Financial_Analysis.txt")
    # Use the write application to write our findings into the txt file we created
    #The \n are used to move down a row after each row has been written
    with open(analysis_file, "w") as writing_file:
        
        writing_file.write("Financial Analysis")
        writing_file.write("\n")
        writing_file.write("--------------------------------")
        writing_file.write("\n")
        writing_file.write(f'Total Months: {len_total_months}')
        writing_file.write("\n")
        writing_file.write(f'Total: ${sum_total_profit}')
        writing_file.write("\n")
        writing_file.write(f'Average Change: ${average_change}')
        writing_file.write("\n")
        writing_file.write(f'Greatest Increase: {total_months[max_month]} ${max_total_profit}')
        writing_file.write("\n")
        writing_file.write(f'Greatest Decrease: {total_months[min_month]} ${min_total_profit}')
        