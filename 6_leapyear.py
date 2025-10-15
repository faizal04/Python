# Check if a year is leap or not
year = int(input("Enter the year you want to check: "))
if year % 100 == 0 and year % 400 == 0:
    print(f"The entered year {year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"The entered year {year} is a leap year")
else:
    print(f"The entered year {year} is NOT a leap year")
