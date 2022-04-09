import os
import csv




#variables
month_count = 0
total_profit = 0
total_profit_change = 0



    # set up path
budget_data = '/Users/anthonygarcia/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

    


    # Open CSV
with open(budget_data) as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)
        
    
        # Variables 
        row = next(csvReader,None)
        incr_month = row[0]
        decr_month = row[0]
        profit = float(row[1])
        decr_profit = profit
        incr_profit = profit
        prev_profit = profit
        month_count = 1
        total_profit = float(row[1])
        total_profit_change = 0

        
        for row in csvReader:

            # Increase counter for months
            month_count = month_count + 1

            profit = float(row[1])

            # Add to the sum of profit
            total_profit = total_profit + profit

            # Find change in profit between current and previous month
            profit_change = profit - prev_profit

            
            total_profit_change = total_profit_change + profit_change

            # Determine the increase/decrease  from change in profit
            if profit_change > incr_profit:
                incr_month = row[0]
                incr_profit = profit_change

            if profit_change < decr_profit:
                decr_month = row[0]
                decr_profit = profit_change

            # reset  
            prev_profit = profit

        # find average/average change in profit
        avg_profit = total_profit/month_count
        avg_profit_change = total_profit_change/(month_count-1)

        # Round the totals
        total_profit = int(total_profit)
        avg_profit_change = round(avg_profit_change,2)
        incr_profit = round(incr_profit)
        decr_profit = round(decr_profit)
        
        # Print analysis
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {month_count}")
        print(f"Total Revenue: ${total_profit} ")
        print(f"Average Revenue Change: ${avg_profit_change} ")
        print(f"Greatest Increase in Revenue: {incr_month}  ${incr_profit} ")
        print(f"Greatest Decrease in Revenue: {decr_month}  ${decr_profit} ")
        
        # The output path
        output_path = '/Users/anthonygarcia/Desktop/python-challenge/PyBank/analysis/PyBank_Analysis.txt'
        
        # Write summary to text 
        with open('/Users/anthonygarcia/Desktop/python-challenge/PyBank/analysis/PyBank_Analysis.txt', 'w') as text:
            text.write(f"Financial Analysis:\n")
            text.write("-------------------------------------------------------\n")
            text.write(f"Total Months: {month_count}\n")
            text.write(f"Total Revenue: ${total_profit}\n")
            text.write(f"Average Revenue Change: ${avg_profit_change}\n")
            text.write(f"Greatest Increase in Revenue: {incr_month}  ${incr_profit}\n")
            text.write(f"Greatest Decrease in Revenue: {decr_month}  ${decr_profit}\n")
            text.close
            
        