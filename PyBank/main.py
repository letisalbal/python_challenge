import csv
import os

csvpath = os.path.join("..", "Resources", "Budget_Data.csv")

with open(Budget_Data.csv, newline=‘’) as csvfile:
  csvreader = csv.reader(PyBank_csv, delimiter=‘,’)
  csv_header = next(csvreader)

  profit = []
  date = []
  monthly_changes = []

  count = 0
  total_profit = 0
  total_change = 0
  prev_profit = 0

  for row in csvreader:
      count = count + 1
      date.append(row[0])


      profit.append(row[1])
      total_profit = total_profit + int(row[1])


      final_profit = int(row[1])
      monthly_profit_change = final_profit - prev_profit


      monthly_changes.append(monthly_profit_change)

      total_change = total_change + monthly_profit_change
      prev_profit = final_profit

      avg_change_profit = (total_change/count)



      greatest_increase = max(monthly_changes)
      greatest_decrease = min(monthly_changes)



      increase_date = date[monthly_changes.index(greatest_increase)]
      decrease_date = date[monthly_changes.index(greatest_decrease)]

      print(“Financial Analysis”)
      print(“-------------------------------------------------------“)
      print(“Total Months:” + str(count))
      print(“Total Profits:” + “$” + str(total_profit))
      print(“Average Change:” + “$” + str(int(avg_change_profit)))
      print(“Greatest Increase in Profits:” + str(increase_date) + “($” + str(greatest_increase) + “)”)
      print(“Greatest Decrease in Profits:” + str(decrease_date) + ” ($” + str(greatest_decrease) + “)”)