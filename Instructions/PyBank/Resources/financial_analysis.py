import os
import csv 

budget_data = os.path.join("budget_data.csv")
with open(budget_data, 'r') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ',')
    total_months = sum(1 for row in csvreader)
    print(total_months)

def financials(budget_data):
    monthtotal = 0
    net_revenue = 0
    total_revenue = 0
    average_change = 0
    max_rev = 0
    min_rev = 0 
    change = []
    lastmonth = None 
    for row in budget_data:
            current_month = row[0]
            current_profit = int(row[1])
            total_revenue += current_profit
            monthtotal += 1 
            if lastmonth is not None: 
                current_change = current_profit-lastmonth
                change.append(current_change)
                if current_change > max_rev:
                    max_rev = current_change
                    maxmonth = current_month
                if current_change < min_rev:
                    min_rev = current_change
                    minmonth = current_month
            lastmonth = current_profit
    average_change = sum(change)/len(change)
    return[monthtotal, total_revenue, max_rev, min_rev, average_change, maxmonth, minmonth]


with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvfile)
    analysis = financials(csvreader)
output_summary = print(f"""Financial Summary\n
----------------------\n
Total months:{analysis[0]}\n
Total Revenue:${analysis[1]}\n
Average Change: ${analysis[4]}\n
Greatest increase:{analysis[5]}, ${analysis[2]}\n
Greatest decrease: {analysis[6]}, ${analysis[3]}\n
""")

output_file = os.path.join("output.txt")

with open(output_file, "w") as file:
    data  = csv.writer(datafile)

    writer.writerow(["Title", "Price", "subCount", "numRev", "courseLength"])

    writer.writerows(udemyData)
help(writer.writerows)






        








# def financials(budget_data):
#     net_revenue = 0
#     for row in budget_data: 
#         net_revenue += int(row[1])
# print(financials(budget_data))



# def financials(budget_data):
#     total_months = sum(1 for row in )
#         print("Hi")
# print(financials(budget_data))

    # net_revenue = int(budget_data[1])
    # average_change = 0 
    # greatest_inc = 0
    # greatest_dec = 0 
