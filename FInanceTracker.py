import csv
import matplotlib.pyplot as plt
from datetime import datetime

TRANSACTION_FILE = 'transactions.csv'

def add_transaction(date, amount, category, description):
    with open(TRANSACTION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

def view_transactions():
    try:
        with open(TRANSACTION_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No transactions found. Please add some transactions.")

def generate_report():
    income = 0
    expenses = 0
    categories = {}
    
    try:
        with open(TRANSACTION_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, amount, category, description = row
                amount = float(amount)
                if category.lower() == 'income':
                    income += amount
                elif category.lower() == 'expense':
                    expenses += amount
                    if description in categories:
                        categories[description] += amount
                    else:
                        categories[description] = amount
    except FileNotFoundError:
        print("No transactions found for the report.")

    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Net Savings: ${income - expenses:.2f}")

    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Breakdown by Category")
    plt.show()

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category (income/expense): ")
            description = input("Enter description: ")
            add_transaction(date, amount, category, description)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
