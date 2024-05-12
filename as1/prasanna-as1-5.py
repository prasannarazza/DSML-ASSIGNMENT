purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount >= 5000:
    discount = 0.10 * purchase_amount
elif purchase_amount >= 4000:
    discount = 0.07 * purchase_amount
elif purchase_amount >= 3000:
    discount = 0.05 * purchase_amount
elif purchase_amount >= 2000:
    discount = 0.03 * purchase_amount
else:
    discount = 0.02 * purchase_amount
print("Discount:", discount)