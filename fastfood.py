print("----- Fast Food Menu -----")
print("1. Sandwich")
print("2. Pizza")
print("3. Burger")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Sandwich")
        print("1. Veg Sandwich")
        print("2. Cheese Sandwich")
        print("3. Grilled Sandwich")

        sub = int(input("Select Sandwich type: "))

        match sub:
            case 1:
                print("You ordered Veg Sandwich")
            case 2:
                print("You ordered Cheese Sandwich")
            case 3:
                print("You ordered Grilled Sandwich")
            case _:
                print("Invalid Sandwich choice")

    case 2:
        print("You selected Pizza")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")

        sub = int(input("Select Pizza type: "))

        match sub:
            case 1:
                print("You ordered Thin Crust Pizza")
            case 2:
                print("You ordered Cheese Burst Pizza")
            case 3:
                print("You ordered Fresh Dough Pizza")
            case _:
                print("Invalid Pizza choice")

    case 3:
        print("You selected Burger")
        print("1. Veg Burger")
        print("2. Cheese Burger")
        print("3. Double Patty Burger")

        sub = int(input("Select Burger type: "))

        match sub:
            case 1:
                print("You ordered Veg Burger")
            case 2:
                print("You ordered Cheese Burger")
            case 3:
                print("You ordered Double Patty Burger")
            case _:
                print("Invalid Burger choice")

    case _:
        print("Invalid Menu Choice")