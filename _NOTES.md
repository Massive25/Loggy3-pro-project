"""
Loggy3 Pro Project - Hour 6
File: hour6_dashboard.py
Purpose: Generate data for Google sheets dashboard + sustain 1 hour
Author: Massive25 | Embu, KE
Tier: $1 Pro Upgrade Track -10 Hours Challenge
"""
#Import time to simulate dashboard refresh (like real dashboard)
import time
from datetime import datetime
print("="*50)
Print(LOGGY3 HOUR 6 - DASHBOARD GENERATOR STAARTING...")
Print("="*50)
# Step 1:Mock M-PESA data (like you receive M-PESA SMS)
M_PESA_ messages = [
      {"code": "QGH7T8", "amount": 500,"type": "Data Bundle", "balance": 12000}'
      {"code": "QGH7T9", "amount": 1200, "type": "Lunch Payment", "balance": 10800},
      {"code": "QGH7UO", "amount": 300, "type": "BODA BODA", "balance",: 10500},
      {"code": "QGH7UI", "amount": 800, "type": "ARTIME" , "balance",: 9700},
      {"code": "QGH7U2", "amount",: 1500, "type": "Office Rent", "balance",: 8200},
      ]
      Print(f"\n[ {datetime.now ()} ] PARASING {Len(M-PESA_MESSAGES)} M-PESA messages...")
      # Step 2: Process expenses
      processed-expenses = []
      total_ spent = 0
for I, msg in enumerate(MPESA_MESSAGES)}: {msg['type']}..")
Print(f"\n Processing {i}/{len(MPESA_MESSAGES)}: {msg['type']}..") 
  time. sleep(1) # Simulate work - help sustain hour
  expense = {
       "id": i,
       "MPESA_CODE": msg["amount"],
       "category": msg["type"]'
       "remaining_ balance": msg["balance"},
       "date": "2026-11-14",
       "location": "Embu, Kenya"
       }
       processed_expenses.append(expense)
       total_ spent +=msg["amount"]
       print(f" -> Added: KES {msg['amount']} \ Balance: KES {msg['balance']}")
    #Step 3: Analytics for Dashboard
    Print("\n" + "-"*50)
    print("GENERATING DASHBOARD ANALYTICS...")
    Print("-"*50)
    categories = {}
    for EXP in PROCESSED_EXPENSES:
        cat = exp["category"] 
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += exp["amount_kes"] 
    print(f"\NTOTAL TRANSACTIONS PROCESSED: {len(processed_expenses)}") 
    print(F"TOTAL TRANSACTION SPENT:KES {total_spent}")
    print(F"AVERAGE TRANSACTION: KES {"TOTAL-SPENT" / Len(PROCESSED_EXPENSES):.2f}")          
    print(F"REMAINING BALANCE: KES {PROCESSED_EXPENSES[-1]['remaining_balance']}")
    print(\NCATEGORY BREAKDOWN (for Pie Chart):")
    for cat, amount in categories.items()
        percentage = (amount / TOTAL-spent) * 100
        print(f"  {cat}: KES {amount} ({percentage:.1f}%)")
    #Step4; Prepare Google Sheet export format 
    print("\n" + "-"*50)
    print("PREPARING GOOGLE SHEET EXPORT...")
    print("-"*50)
    print("\NCOPY this to Google sheets:")
    print("ID, M-PESA Code, Amount, Category, Balance, Date")
    for EXP in PROCESSED_EXPENSES:
        print(f"{EXP['id']},{EXP['M-PESA_CODE']}, {EXP['AMOUNT KES']}, {EXP['category']], {EXP['REMAINING_BALANCE']}, {EXP['date']}")
   #Step 5: Summary for README
   print("\n" + "="*50)
   print("HOUR 6 SUMMARY - READY FOR LOGGY3 PRO")
   print("="*50)
   print("File created:hour6_dashboard.py")
   print("purpose: Dashboard data generator")
   print(Time taken:2:30hrs sustained")
   print(Next file hour 7_tinkercad.py")
   print("Status:Hour 6 COMPLETE-Ready for review") 
   print("="50)
   #Bonus: Function for Hour 7
   def get_dashboardPlink():
       '''Return placeholder for Google sheets link"""
       return "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID"
       print(f"\NDASHBOARD Link Placeholder: {get_dashboard_link()}")
       print("Remember to update README.md with real sheets link!")
