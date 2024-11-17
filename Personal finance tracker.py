import json
import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try: # Error handling
        with open("transactions.json", "r") as file:
            global transactions
            transactions = json.load(file)
    except FileNotFoundError:
        print("Transaction file not found. Starting with an empty Transaction")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty Transaction list...")

def save_transactions():
     with open("transactions.json", "w") as file: # Opening the json file in writable format
        file.write('[\n')
        for transaction in transactions:
            file.write('\t')
            json.dump(transaction, file)
            file.write(',\n')
        file.write('\b\b]')

# Feature implementations
def add_transaction():
    while True:
        try: # Error handling
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid input. Try again!")
    category = input("Enter the category: ")
    while True:
        transaction_type = input("Enter the transaction type (Income/Expense): ").capitalize()
        if transaction_type == "Income" or transaction_type == "Expense":
            break
        else:
            print("Invalid transaction. Try again!")
    while True:
        try: # Error handling
            date = input("Enter the date (YYYY-MM-DD): ")
            datetime.datetime.strptime(date , "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use 'YYYY-MM-DD' format.")
    transactions.append([amount, category, transaction_type, date])
    save_transactions()
    print("Transaction added successfully!")

def view_transactions():
    print("\n----Transactions----")
    if not transactions:
        print("No transactions available!")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")

def update_transaction():
    view_transactions()
    while True:
        index = int(input("Enter the index of the transaction to update: ")) - 1
        if 0 <= index < len(transactions):
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            type = input("Enter new type (Income/Expense): ").capitalize()
            date = input("Enter new date (YYYY-MM-DD): ")
            transactions[index] = [amount, category, type, date]
            save_transactions()
            print("Transaction updated successfully!")
            break
        else:
            print("Invalid index. Try again!")

def delete_transaction():
    view_transactions()
    index = int(input("Enter the index of the transaction to delete: ")) - 1
    if 0 <= index < len(transactions):
        del transactions[index]
        save_transactions()
        print("Transaction deleted successfully!")
    else:
        print("Invalid index.")

def display_summary():
    total_income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")
    total_expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")
    net_balance = total_income - total_expense
    print("\n----Summary----")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Net Balance: {net_balance}")

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program...\n")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
