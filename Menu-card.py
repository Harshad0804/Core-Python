print("========== WELCOME TO HARSHAD CAFÉ ==========")
print("Menu Card:")
print("1. Coffee       - ₹50")
print("2. Tea          - ₹30")
print("3. Sandwich     - ₹70")
print("4. Burger       - ₹120")
print("5. Pizza        - ₹250")
print("6. Exit")

total = 0

while True:
    choice = int(input("\nEnter the item number you want to order (1-6): "))

    if choice == 1:
        total += 50
        print("You added Coffee - ₹50")
    elif choice == 2:
        total += 30
        print("You added Tea - ₹30")
    elif choice == 3:
        total += 70
        print("You added Sandwich - ₹70")
    elif choice == 4:
        total += 120
        print("You added Burger - ₹120")
    elif choice == 5:
        total += 250
        print("You added Pizza - ₹250")
    elif choice == 6:
        print("\nThank you for visiting Harshad Café!")
        print("Your total bill is ₹", total)
        break
    else:
        print("Invalid choice! Please choose from 1 to 6.")
