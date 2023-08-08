# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
# Example Input
# Welcome to the tip calculator!
# What was the total bill?
# How much tip would you like to give? 10, 12, or 15?
# How many people to split the bill?

print(40 * "*" + " Welcome to the Tip Calculator " + 40 * "*")

org_bill = float(input("What was the total bill?\n$"))

org_tip = float(input("How much tip would you like to give? 10, 12, or 15?\n%"))

total_people = int(input("How many people to split the bill?\n"))

total_bill = ((org_tip / 100) * org_bill) + org_bill

total_per_person = total_bill / total_people

print(f"The total per person is... ${total_per_person:.2f}")