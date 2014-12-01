# Write a program which calculates the value of an investment given the initial
# amount PV, the annual interest rate i, and the number of years to invest n.

invested = float(raw_input("What is the amount being invested: "))
annual_rate = float(raw_input("What is the annual interest rate (percentage): ")) * 0.01
years_interest = float(raw_input("How many years will it accrue interest: "))

print "Invested: %d, Annual Rate: %d, Years Interest: %d" % (invested, annual_rate, years_interest)

final_value = invested * (1 + annual_rate) ** years_interest

print "The final value will be $%.2f after %d years." % (final_value, years_interest)
