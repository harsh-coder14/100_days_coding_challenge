print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = (total_bill * tip_percent)/100
pay = total_bill + tip
each_pay = pay/people
each_pay_round = "{:.3f}".format(each_pay)
# each_pay = round (pay/people, 2)
print(f"Each person should pay: ${each_pay_round}")