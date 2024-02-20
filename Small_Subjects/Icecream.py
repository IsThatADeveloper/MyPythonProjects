response = input("Do you like Ice Cream? ").strip().lower()

if response == "yes":
    print("Then do you like Vanilla, Chocolate, or Mint? ")
    flavor = input("Enter your favorite flavor: ").strip().lower()
    
    if flavor == "vanilla":
        print("You like Vanilla!")
    elif flavor == "chocolate":
        print("You like Chocolate!")
    elif flavor == "mint":
        print("You like Mint!")
    else:
        print("Invalid flavor input.")
else:
    print("Okay, maybe next time.")
