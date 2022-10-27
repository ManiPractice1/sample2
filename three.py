def Trans():
    pin = 1234
    bal = 6000
    rpin = int(input("Enter your pin :"))
    if rpin == pin:
        print("Authentication Success")
        amt = int(input("Enter amount to Withdraw :"))

        if amt <= bal:
            print("transaction Success")
            print("Collect Your cash")
            print("Drawn Amount : ", amt)
            bal = bal-amt
            print("Remaining Balance :", bal)
        else:
           print("Transaction Failed, insuficient balance")
    else:
        print("Authentication failed")



Trans()
