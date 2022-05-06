number = input("Please input a positive number: ")

def showEvenNumber(num):
    for i in range(0, num, 2):
        print(i)

while True:
    if (number.isdigit()) and (int(number) % 2 == 0):
        showEvenNumber(int(number))
    else:
        number = input("Invalid entry. Please input a positive number: ")
        continue
    break