# rogram using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

remaind_years = 90 - int(age)
days = remaind_years * 365
weeks = remaind_years * 52
months = remaind_years * 12

print(f"You have {days} days, {int(weeks)} weeks, and {months} months left.")
