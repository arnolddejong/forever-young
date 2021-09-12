number = int(input("Welke tafel wil je graag zien?"))

for i in range(1, 11):
    print(str(i) + " x " + str(number) + " = " + str(i * number))