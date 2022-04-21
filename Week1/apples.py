applePrice = 0.50
currency_format = "${:,.2f}".format(applePrice)
nameInput = input("Please enter your name: ")
storedName = str(nameInput)
print("Hi " + storedName + ". Apples cost", currency_format, "each. ")

quantityInput = input("How many would you like to buy? ")
storedQuantity = int(quantityInput)
print("Thank you", storedName,"for your purchase of", storedQuantity, "apples at a cost of", currency_format, "each.")