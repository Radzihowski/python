# 6.5 - Challenge: Track Your Investments
# Solution to challenge

# Calculate interest to track the growth of an investment

def invest(amount, rate, years):
    for i in range (1, years + 1):
        amount = amount * ( rate + 1 )
        print(f"year {i}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an annual rate of return: "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)