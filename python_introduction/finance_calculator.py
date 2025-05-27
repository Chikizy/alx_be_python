month_inc = int(input("Enter your monthly income: "))
month_exp = int(input("Enter your total monthly expenses: "))
monthly_savings = month_inc - month_exp

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

