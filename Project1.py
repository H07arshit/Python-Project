#Project1
c_pin = "1234"
balance = 10000
attempt = 0
history = []

while attempt < 3:
    pin = input("Enter pin: ")
    if pin != c_pin:
        attempt += 1
        if attempt < 3:
            print(f"Wrong PIN. Attempts left: {3 - attempt}")
        else:
            print("Card blocked.")
    else:
        break

if attempt < 3:
    while True:
        print("""
        1. Balance 
        2. Deposit
        3. Withdraw 
        4. Exit""")
        option = int(input("Enter the option: "))
        
        if option == 1:
            print("Balance:", balance)
            
        elif option == 2:
            d_amount = int(input("Enter deposit amount: "))
            if d_amount > 0:
                balance += d_amount
                history.append(f"Deposit {d_amount}")
                print("New balance:", balance)
            else:
                print("Invalid amount")
                
        elif option == 3:
            w_amount = int(input("Enter withdrawal amount: "))
            if w_amount <= balance:
                balance -= w_amount
                history.append(f"Withdraw {w_amount}")
                print("New balance:", balance)
            else:
                print("Insufficient balance")
                
        elif option == 4:
            for item in history:
                print(item)
            print("Thank you!")
            break
            
        else:
            print("Invalid option")
