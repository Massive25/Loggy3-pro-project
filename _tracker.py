#Loggy3 pro -M-Pesa Tracker
expenses=[]
def add_expense(amount, category,desc):
  if amount <=0:
    print("Invalid amount")
    return none
    expenses.append({"amount": amount, "amount, "category": category, "desc": desc})
    print(f"Added {category}: KES {amount}")
    return True
def total():
    return sum(e["amount"] for e in expenses)
def report():
    print("\n---Loggy3 Report---")
    for e in expenses:
        Print(f"{e{'category']}: KES {e['amount']} - {e['desc']}"
    Print(f"Total: KES {total()}")
#Demo
add_expenses(500, "Data", "Safaricom 5GB")
add_expenses(1200, "Lunch", "Embu Town")
add_expenses(300, "Boda", "To office")
report()
