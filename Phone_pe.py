while True:
    print("1. Payment Failed")
    print("2. Profile and Privacy")
    print("3. Money Transfer")
    print("4. Recharge and payments")
    print("5. Exit")
    choice = int(input("Enter your choice  "))
    if choice == 1:
        print("Welcome to Payment Failed.")
        print("1.Issues with payment failed.")
        print("2.Issues with pending payments.")
        print("3.Issues successful payments.")
        print("4.Issues with payments made to merchants.")
        print("5.Issues with refunds.")
        print("6. Exit")
        choice1 = int(input("Enter your choice  "))
        if choice1 == 1:
             print("Welcome to Issues with Payment Failed") 
             print("1.Why did my payment fail?")
             print("2.Why is my money deducted for my failed payment?")
             print("3.Why is my money not refunded yet?")
             print("4.Where can i find UTR number?")
             print("5.Exit")
             choice2 = int(input("Enter your choice  "))
             if choice2 == 1:
                print("Why did my payment fail?")
                print("Your UPI payment on PhonePe may have failed due to any one of the below reasons:\n• UPI network issues\n• Technical issues with the banks\n• Wrong UPI PIN\n• Not enough balance in your bank account\n• Reached bank or UPI limits\n• Security reasons\n• Other bank account-related issues\nImportant: You can try making the payment again after checking the reason for failure within the History section of your PhonePe app.")
                break
             if choice2 == 2:
                print("Why is my money deducted for my failed payment?")
                print("\n If money is deducted for a failed payment, there is no need to worry as it is absolutely safe with your bank. The amount will be refunded to your account within 3 to 5 days from the date you made the payment. You can check your relevant bank account statement after 5 days for a refund confirmation.\n \n If your bank fails to refund the amount within 5 days, please contact them with the Unique Transaction Reference (UTR) number for the payment. They will help you with this.\n \nNote: In some error scenarios, your bank may refund your amount immediately. As you may experience a delay in receiving an SMS from your bank about such refunds, we recommend that you check the relevant account statement for confirmation.")
                break
             if choice2 == 3:
                print("Why is my money not refunded yet?")
                print("For failed UPI payments, banks usually refund the money anywhere between 3 to 5 days from the time of payment.\n Please check your bank account statement after 5 days.\n In case you haven’t received the refund even after 5 days, please contact your bank with the Unique Transaction Reference (UTR) number for the payment. \nNote: You may experience a delay in receiving an SMS from your bank about such refunds, we recommend that you check the relevant account statement for a confirmation")
                break
             if choice2 == 4:
                print("Where can i find UTR number?")
                print("\n To find the UTR number for your payment, \n 1 Tap History on your PhonePe app home screen.\n 2 Select the payment for which you would like to view the UTR number.\n 3 You will see the 12-digit UTR number in the Debited from section on the screen")
                break
             if choice2 == 5:
                print("Exit")
                break
             
        if choice1 == 2:
            print("Welcome to pending payments")
        if choice1 == 3:
            print("Welcome to successful payments")  
        if choice1 == 4:
            print("Welcome to payments made to merchants")
        if choice1 == 5:
            print("Welcome to refunds")
        if choice1 == 6:
            print("Exit")
            break 
    if choice == 2:
        print("Welcome to Profile and privacy")
    if choice == 3:
        print("Welcome to Money Transfer")
    if choice == 4:
        print("Welcome to  Recharge and payments")
    if choice == 5:
        print("Exit")
        break