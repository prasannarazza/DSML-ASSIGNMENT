purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount >= 1000:
    discount = 0.05 * purchase_amount
    print("Discount:", discount)