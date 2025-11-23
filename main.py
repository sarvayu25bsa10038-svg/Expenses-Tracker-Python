# Expense Tracker (Python Project)

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        item = input("Enter item: ")
        amount = input("Enter amount: ")

        expenses.append([date, item, amount])
        print("Expense added.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses available.")
        else:
            total = 0
            print("\n--- All Expenses ---")
            for e in expenses:
                print(e[0], "-", e[1], "-", e[2])
                total = total + float(e[2])
            print("Total Expense =", total)

    elif choice == "3":
        import os
        file = open(os.path.join(os.path.dirname(__file__) ,"expenses.txt"),"w")
        for e in expenses:
            file.write(e[0] + "," + e[1] + "," + str(e[2]) + "\n")
        file.close()
        print("Saved in file expenses.txt")
        break

    else:
        print("Invalid choice")