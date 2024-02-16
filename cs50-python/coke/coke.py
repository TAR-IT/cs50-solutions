def coke_machine():
    accepted_coins = {1, 5, 10, 25}  # Denominations of accepted coins (in cents)
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        coin = int(input("Insert a coin (1, 5, 10, or 25 cents): "))
        if coin in accepted_coins:
            total_inserted += coin
            amount_remaining = amount_due - total_inserted

            if amount_remaining <= 0:  # Changed the condition to include the case of exact change
                change_owed = total_inserted - amount_due
                print(f"Change Owed: {change_owed}")
                return

            print(f"Amount Due: {amount_remaining}")
        else:
            print("Invalid coin. Please insert a valid coin.")
            print(f"Amount Due: {amount_due - total_inserted}")

    change_owed = total_inserted - amount_due
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    coke_machine()