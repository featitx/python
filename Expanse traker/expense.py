import datetime

class SimpleExpenseTracker:
    def __init__(self):
        self.expense_records = {}

    def add_spending(self, amount, category):
        date = datetime.date.today()
        if date not in self.expense_records:
            self.expense_records[date] = []
        self.expense_records[date].append({"amount": amount, "category": category})
        print("Spending recorded successfully.")

    def display_expenses(self):
        if not self.expense_records:
            print("No spending recorded.")
            return

        print("\nSimple Expense Tracker:")
        for date, items in self.expense_records.items():
            print(f"\nDate: {date}")
            for item in items:
                print(f"Amount: ${item['amount']}, Category: {item['category']}")

    def display_spending_pattern(self):
        if not self.expense_records:
            print("No spending recorded.")
            return

        total_spending = 0
        category_spending = {}

        for items in self.expense_records.values():
            for item in items:
                total_spending += item['amount']
                category = item['category']
                category_spending[category] = category_spending.get(category, 0) + item['amount']

        print("\nSpending Pattern:")
        print(f"Total Spending: ${total_spending}")
        for category, amount in category_spending.items():
            print(f"{category}: ${amount}")

def start_expense_tracker():
    expense_tracker = SimpleExpenseTracker()

    while True:
        print("\nExpense Tracking Menu:")
        print("1. Add Spending")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the spending amount: $"))
            category = input("Enter the spending category: ")
            expense_tracker.add_spending(amount, category)
        elif choice == '2':
            expense_tracker.display_expenses()
        elif choice == '3':
            expense_tracker.display_spending_pattern()
        elif choice == '4':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    start_expense_tracker()
