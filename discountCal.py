total = int(input("Enter total amount: "))

if total >= 5000:
    discount = total * 20 / 100
    final = total - discount

    print("20% discount:", discount)
    print("Final amount:", final)

elif total >= 3000:
    discount = total * 10 / 100
    final = total - discount

    print("10% discount:", discount)
    print("Final amount:", final)

else:
    print("No discount")
    print("Final amount:", total)