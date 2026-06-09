import csv
from datetime import datetime
import matplotlib.pyplot as plt

def register():
    username = input("Enter new username: ").strip().lower()
    password = input("Enter password: ").strip()

    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("User registered successfully!")

def login():
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login successful!")
                    filename = username + ".csv"
                    return username, filename
    except FileNotFoundError:
        print("No users found. Please register first.")
        return None, None

    print("Invalid credentials!")
    return None, None

def load_expense():
    expense=[]
    try:
         with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    category = row[0]
                    amount = float(row[1])
                    date = "unknown"
                elif len(row) == 3:
                    category = row[0]
                    amount = float(row[1])
                    date = row[2]
                else:                   
                     continue  

                expense.append((category, amount, date))
    except FileNotFoundError:
        print("No existing expense file found. Starting with an empty expense list.")
    return expense

def add_expense():
    with open(filename, "a", newline="") as file:
        category = input("Enter the expense category:").strip().lower()
        try:
            amount = float(input("Enter the expense amount:"))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        today = datetime.now().date()
        expense.append((category, amount, today))
        writer = csv.writer(file)
        writer.writerow([category, amount, today])
    print("Expense added successfully!")

def view_expenses():
    if len(expense) == 0:
        print("No expenses to show.")
        return
    count=0
    for category, amount, date in expense:
        count=count+1
        print(f"{count}. {category}: ${amount:.2f} - {date}")

def show_total_expenses():
    total = 0
    for category, amount, date in expense:
        total = total + amount
    print("Total Expenses:", f"${total:.2f}")

def delete_expense():
    if len(expense) == 0:
        print("No expenses to delete.")
        return
    try:
        choice=int(input("Enter the expense number you want to delete:"))
    except ValueError:
        print("Invalid choice. Please enter a valid number.")
        return
    if 1 <= choice <= len(expense):
        del expense[choice-1]
        with open(filename, "w", newline="") as wfile:
            writer = csv.writer(wfile)
            for category, amount, date in expense:
                writer.writerow([category, amount, date])
        print("Expense deleted successfully!") 
    else:           
         print("Invalid expense number.")

def search_expense():
    if len(expense) == 0:
        print("No expenses to search.")
        return
    search_category = input("Enter the expense category to search:").strip().lower()
    found = False
    for category, amount, date in expense:
        if category.lower() == search_category.lower():
            print(f"{category}: ${amount:.2f} - {date}")
            found = True
    if not found:
        print("No expenses found for the given category.")

def update_expense():
    if len(expense) == 0:
        print("No expenses to update.")
        return
    try:
        choice=int(input("Enter the expense number you want to update:"))
    except ValueError:
        print("Invalid choice. Please enter a valid number.")
        return

    if 1 <= choice <= len(expense):
        category = input("Enter the new expense category:").strip().lower()
        try:
            amount = float(input("Enter the new expense amount:"))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return
        date = expense[choice-1][2]  # Retain the original date
        expense[choice-1] = (category, amount, date)
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for category, amount, date in expense:
                writer.writerow([category, amount, date])
        print("Expense updated successfully!")
    else:           
         print("Invalid expense number.")

def category_wise_total_expenses():
    category_totals = {}
    for category, amount, date in expense:
        #category = category.strip().lower()
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount  
        
    print("Category-wise Total Expenses:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def today_expenses():
    if len(expense) == 0:
        print("No expenses to show.")
        return
    today = str(datetime.now().date())
    total = 0
    count = 0
    highest_amount = 0
    highest_category = ""
    highest_date = ""

    found = False

    for category, amount, date in expense:
        if date == today:
            if not found:
                highest_amount = amount
                highest_category = category
                highest_date = date
                found = True

            print(f"{category}: ${amount:.2f} - {date}")

            total += amount
            count += 1

            if amount > highest_amount:
                highest_amount = amount
                highest_category = category
                highest_date = date

    if count == 0:
        print("No expenses found for today.")
        return

    print("\n--- Today's Summary ---")
    print(f"Total: ${total:.2f}")
    print(f"Count: {count}")
    print(f"Highest: {highest_category} - ${highest_amount:.2f} - {highest_date}")

def highest_expense():
    if len(expense) == 0:
        print("No expenses to analyze.")
        return
    highest_category, highest_amount, highest_date = expense[0]
    for category, amount, date in expense[1:]:
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category
            highest_date = date
    print(f"Highest Expense: {highest_category} - ${highest_amount:.2f} - {highest_date}")

def lowest_expense():
    if len(expense) == 0:
        print("No expenses to analyze.")
        return
    lowest_category, lowest_amount, lowest_date = expense[0]
    for category, amount, date in expense[1:]:
        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = category
            lowest_date = date
    print(f"Lowest Expense: {lowest_category} - ${lowest_amount:.2f} - {lowest_date}")

def view_expenses_by_date():
    if len(expense) == 0:
        print("No expenses to show.")
        return
    search_date = input("Enter the date to view expenses (YYYY-MM-DD):").strip()
    found = False
    for category, amount, date in expense:
        if date == search_date:
            print(f"{category}: ${amount:.2f} - {date}")
            found = True
    if not found:
        print("No expenses found for the given date.")

def monthly_expenses():
    if len(expense) == 0:
        print("No expenses to show.")
        return
    search_month = input("Enter the month to view expenses (YYYY-MM):").strip()
    monthly_total = 0
    count = 0
    highest_amount = 0
    highest_category = ""
    highest_date = ""
    for category, amount, date in expense:
        if date[:7] == search_month:  # Compare the month part of the date
                print(f"{category}: ${amount:.2f} - {date}")
                monthly_total = monthly_total + amount
                count = count + 1
                if amount > highest_amount:
                    highest_amount = amount
                    highest_category = category
                    highest_date = date
    if count == 0:
        print("No expenses found for the given month.")

    print("\n--- Monthly Summary ---")
    print(f"Total: ${monthly_total:.2f}")
    print(f"Count: {count}")
    print(f"Highest: {highest_category} - ${highest_amount:.2f} - {highest_date}")
    print(f"Total expenses for {search_month}: ${monthly_total:.2f}")

def export_monthly_report():
    search_month = input("Enter month (YYYY-MM): ").strip()

    filename = f"monthly_report_{search_month}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Category", "Amount", "Date"])

        for category, amount, date in expense:
            if date[:7] == search_month:
                writer.writerow([category, amount, date])

    print(f"Monthly report exported successfully to {filename}")

def category_monthly_report():
    search_month = input("Enter month (YYYY-MM): ").strip()

    category_totals = {}
    total = 0

    for category, amount, date in expense:
        if date[:7] == search_month:

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

            total += amount

    print("\n--- Category Wise Report ---")

    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")

    print(f"\nTotal: ${total:.2f}")

def category_chart():
    category_totals = {}

    for category, amount, date in expense:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Category-wise Expenses")
    plt.show()

def monthly_trend_chart():
    month_totals = {}

    for category, amount, date in expense:
        month = date[:7]

        if month in month_totals:
            month_totals[month] += amount
        else:
            month_totals[month] = amount

    months = sorted(month_totals.keys())
    values = [month_totals[m] for m in months]

    plt.figure(figsize=(8,5))
    plt.plot(months, values, marker='o')
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.grid(True)
    plt.show()

print("Welcome to the Expense Tracker!")
print("Please choose an option:")
print("1. New Register")
print("2. Login")

auth_choice = input("Enter choice: ")

if auth_choice == "1":
    register()

username, filename = login()

if username is None:
    exit()

expense = load_expense()

while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")
    print("5. Delete Expense")
    print("6. Search Expense")
    print("7. Update Expense")
    print("8. Category-wise Total Expenses")
    print("9. Category-wise Monthly Report")
    print("10. Today's Expenses")
    print("11. Highest Expense")   
    print("12. Lowest Expense") 
    print("13. View Expenses by Date")
    print("14. Monthly Expenses")   
    print("15. Export Monthly Report")
    print("16. Category-wise Expense Chart")
    print("17. Monthly Expense Trend Chart")
    
    choice = input("Enter your choice: ") 

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_total_expenses()
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        break
    elif choice == '5':
        delete_expense()
    elif choice == '6':
        search_expense()
    elif choice == '7':
        update_expense()    
    elif choice == '8':
        category_wise_total_expenses()
    elif choice == '9':
        category_monthly_report()
    elif choice == '10':
        today_expenses()
    elif choice == '11':
        highest_expense()
    elif choice == '12':
        lowest_expense()
    elif choice == '13':
        view_expenses_by_date()
    elif choice == '14':
        monthly_expenses()
    elif choice == '15':
        export_monthly_report()
    elif choice == '16':
        category_chart()
    elif choice == '17':
        monthly_trend_chart()
    else:
        print("Invalid choice. Please try again.")