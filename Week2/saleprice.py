descInput = input("Please enter the product description: ")
storedDescInput = descInput
quantityInput = input("How many of item " + storedDescInput + " are being purchased? ")
storedQuantityInput = int(quantityInput)
priceInput = input("What is the regular price? ")
storedInputPrice = float(priceInput)

if (storedInputPrice >= 19.99) and (storedInputPrice < 39.99):
    discount = (storedInputPrice * 0.15) 
    savings = discount * storedQuantityInput
    afterDiscount = (storedInputPrice - discount) * storedQuantityInput 
    afterTax = (afterDiscount * 0.0625)
    finalPrice = "${:,.2f}".format(afterTax + afterDiscount)
    print("Your Receipt")
    print("--------------------------------------------------")
    print(storedQuantityInput, storedDescInput, "@", "${:,.2f}".format(storedInputPrice))
    print("***15 percent off***")
    print("Sales Tax:", "${:,.2f}".format(afterTax))
    print("Total amount due:", finalPrice)
    print("Your savings", "${:,.2f}".format(savings), "today!")
elif storedInputPrice >= 39.99:
    discount2 = (storedInputPrice * 0.25)
    savings2 = discount2 * storedQuantityInput
    afterDiscount2 = (storedInputPrice - discount2) * storedQuantityInput
    afterTax2 = (afterDiscount2 * 0.0625)
    finalPrice2 = "${:,.2f}".format(afterTax2 + afterDiscount2)
    print("Your Receipt")
    print("--------------------------------------------------")
    print(storedQuantityInput, storedDescInput, "@", "${:,.2f}".format(storedInputPrice))
    print("***25 percent off***")
    print("Sales Tax:", "${:,.2f}".format(afterTax2))
    print("Total amount due:", finalPrice2)
    print("Your savings", "${:,.2f}".format(savings2), "today!")
else:
    amount = storedInputPrice * storedQuantityInput 
    salesTax = amount * 0.0625
    finalPrice3 = amount + salesTax
    print("Your Receipt")
    print("--------------------------------------------------")
    print(storedQuantityInput, storedDescInput, "@", "${:,.2f}".format(storedInputPrice))
    print("Sales Tax:", "${:,.2f}".format(salesTax))
    print("Total amount due:", "${:,.2f}".format(finalPrice3))
    print("~ Thank you for your purchase! ~")
