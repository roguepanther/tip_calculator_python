# Introduction
print("Welcome to the tip calculator")
# Ask the user for bill total
total_bill = input("What was the total bill? \n")
# Ask the user for tip percentage
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15 \n")
# Ask the user for tip percentage
people_split = input("How many people to split the bill? \n")

bill_per_person = float(total_bill) / int(people_split)
tip_per_bill = bill_per_person * (int(tip_percent) / 100)
full_bill_result = bill_per_person + tip_per_bill
print(round(full_bill_result, 2))
