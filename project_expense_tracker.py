import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        amount REAL,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(category, amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nID | Category | Amount | Date")
    print("-" * 40)
    for expense in expenses:
        print(f"{expense[0]} | {expense[1]} | ₹{expense[2]} | {expense[3]}")
    print("-" * 40)

def total_by_category():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    totals = cursor.fetchall()
    conn.close()
    
    if not totals:
        print("No expenses recorded.")
        return
    
    print("\nCategory-wise Expense Summary")
    print("-" * 30)
    for total in totals:
        print(f"{total[0]}: ₹{total[1]}")
    print("-" * 30)

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print("Expense deleted successfully!")

def ask_continue():
    while True:
        choice = input("Do you want to make any changes? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thank you! Have a great day!")
            return False
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

def main():
    create_table()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses by Category")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            category = input("Enter category (e.g., Food, Travel, Rent, other): ")
            amount = float(input("Enter amount: ₹"))
            add_expense(category, amount)
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            total_by_category()
        
        elif choice == "4":
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
        
        elif choice == "5":
            print("Exiting... Have a great day!")
            break
        
        else:
            print("Invalid choice! Please try again.")
        
        if not ask_continue():
            break

if __name__ == "__main__":
    main()
