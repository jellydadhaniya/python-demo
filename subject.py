print("Welcome to Telecom Calling System")
print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")

choice = int(input("Enter your language choice: "))

match choice:
    case 1:
        print("You selected English")
        print("Press 1 for Balance Check")
        print("Press 2 for Recharge")
        sub = int(input("Enter your choice: "))

        match sub:
            case 1:
                print("Your balance is ₹50")
            case 2:
                print("Recharge successful")
            case _:
                print("Invalid option")

    case 2:
        print("Aapne Hindi chuni hai")
        print("1 dabaye Balance Check ke liye")
        print("2 dabaye Recharge ke liye")
        sub = int(input("Apna option dale: "))

        match sub:
            case 1:
                print("Aapka balance ₹50 hai")
            case 2:
                print("Recharge safal hua")
            case _:
                print("Galat option")

    case 3:
        print("Tame Gujarati pasand kari chhe")
        print("1 dabavo Balance Check mate")
        print("2 dabavo Recharge mate")
        sub = int(input("Tamaro option mukho: "))

        match sub:
            case 1:
                print("Tamaro balance ₹50 chhe")
            case 2:
                print("Recharge safal thayu")
            case _:
                print("Khoto option")

    case _:
        print("Invalid language selection")