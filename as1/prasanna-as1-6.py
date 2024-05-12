balance = float(input("Enter the balance: "))
if balance > 99999:
    interest = 0.07 * balance
elif balance >= 50000:
    interest = 0.05 * balance
else:
    interest = 0.03 * balance
print("Interest:", interest)