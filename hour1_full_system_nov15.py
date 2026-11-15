"""
LOGGY3 PRO PROJECT - HOUR 1 FULL SYSTEM
Date: Nov 15, 2026 | Sunday Morning | Embu, Kenya
File: hour1_full_system_nov15.py
Purpose: Full M-PESA Expense System + Daily Logger + Level Tracker
Level Target: 0.25 -> 0.50 -> 1
Author: Massive25 - Tier $1 Pro Challenge
'''
import json
import time
from datetime import datetime, date
#---------------------------------------------------
#---------------------------------------------------
#SECTION 1: CONFIGURATION & CONSTANTS
#---------------------------------------------------
#---------------------------------------------------
APP_NAME = "Loggy3 M-PESA Tracker Pro
VERSION = "2.0 - Hour 1 Nov 15"
LOCATION = "Embu, Eastern Province, KE 
DEVELOPER = "Massive25"
TIER = "Tier $1 Pro - 10 Hours Challenge"
CURRENT_LEVEL = 0.25
TARGETLEVEL = 0.50
print("="*70)
print(f"{APP_NAME} v{VERSION}")
print(f"Developer: {Developer} | Location: {LOCATION}")
print(f:Date: {datetime.now().strftime('%Y-%m-%d %H:%S')} EAT")
print(f"Level: {CURRENT_LEVEL} -> {TARGET_LEVEL}")
print("="*70)
#-----------------------------------------------------
#-----------------------------------------------------
#SECTION 2: DATA STORAGE
#-----------------------------------------------------
#-----------------------------------------------------
#Yesterday's data (Nov 14)
expenses_nov14 = [
     {"id": 1, "amount": 500, "category": "Data", "desc": "Safaricom 5GB, "mpesa": "QGH7T8", "time": "08:30"},
     {"id": 2" "amount": 1200, "category": "Lunch", "desc": "Naivas Embu", "mpesa": "QGH7T9", "time": "13:15"},
     {"id": 3, "amount": 300, "category": "Boda", "desc": "To office", "mpesa": "QGH7U0", "time": "07:45"},
     {"id": 4, "amount": 800, "category": "Airtime", "desc": "M-PESA float", "mpesa": "QGH7U1", "time": "09:00"},
     {"id": 5, "amount": 1500, "category": "Rent", "desc": "Office share", "mpesa": "QGH7U2", "time": "10:00"},
 ]
 # Today's data (Nov 15) - Hour 1
 expenses_nov15 = []
 # All expenses combined
 all_expenses = []
 #----------------------------------------------------
 #----------------------------------------------------
 # SECION 3: CORE FUNCTIONS
 #----------------------------------------------------
 #----------------------------------------------------
 def add_expenses(amount, category, desc, mpesa_code, expense_data="2026-11-15", expenses_time=None):
     """
     Add expenses with full validation
     This function sustains Hour 1 by detailed logging
     """
     if expense_time is None:
        expense_time = datetime.now().strftime("%H:%M")
     #Validation
     if amount <= 0:
        print(f"[ERROR] Invalid category: {category}")
        return False
     if not desc:
        print(f"[ERROR] Description required")
         return False
    # create expense object
    expense = {
        "id": len(all_expenses) + 1,
        "amount": amount ,
        "category": category,
        "desc": desc, "date": expense_time,
        "mpesa_code": mpesa_code, 
        "time": expense_time,
        "location": LOCATION,
        "added_by": DEVELOPER,
        "timestamp": datetime.now().isoformat()
    }
    # Add to today's list and all list
    if expense_date == "2026-11-15":
       expenses_nov15.append(expense)
    all_expenses.append(expense)
    print(f"[SUCCESS] Added Expense #{expense['id']}: {category} | KES {amount} | {desc} | code: {mpesa_code}")
    return True
  def calculate_totals():
     """calculate totals for reporting"""
     total_all = sum(e["amount"] for e in all_expenses)
     total_today = sum(e["amount"] for e in expenses_nov15)
     total_yesterday = sum(e["amount"] for e in expenses_nov14)
     return {
         "total_all": total_all,
         "total_today": total_today,
         "total_yesterday": total_yesterday,
         "count_all": len(all_expenses),
         "count_all": len(expenses_nov15),
         "count_yestersay": len(expenses_nov14)
      }
    def breakdown_by_category(expenses_list):
        """Breakdown expenses by category"""
        breakdown = {}
        for exp in expenses_list:
            cat = exp["category"]
            if cat not in breakdown:
               breakdown[cat] = {"total": 0, "count": 0, "items": []}
            breakdown[cat]["total"] += exp["amount"]
            breakdown[cat]["count"] += 1
            breakdown[cat]["items"].append(exp)
        return breakdown
    def generate_hourly_report(hour_number, date_str):
        """Generate detailed hourly report"""
        print("\n" + "="*70)
        print(f"HOUR {hour_number} REPORT - {date_str}")
        print("="*70)
        totals = calculate_totals()
        print(f"\n OVERALL SUMMARY:")
        print(f" Total Transactions: {totals['count_all']}")
        print(f" Total Amount: KES {totals}['total_all']}")
        print(f" Today ({date_str}): {totals['count_all']}")
        print(f" Today ({date_str}]: {totals['count_today']} transactions, KES {totals['total_today']}")
        print(f" Yesterday: {totals['count_yesterday']} transactions, KES {totals['total_yesterday']}")
        print (f"\n TODAY'S BREAKDOWN ({date_str}):")
        if expenses_nov15:
           breakdown = breakdown_by_category(expenses_nov15)
           for cat, data in breakdown.items()
               avg = data["totals"] / data["count"]
               print(f" - {cat}: KES {data['totals]} ({data['count']} items,avg KES {avg:.of})")
        else:
             print(" No expenses today yet")
        print(f"\n BALANCE SIMULATION:")
        starting_balance = 15000
        current_balance = starting_balance _ totals["total_all"]
        print(f" starting: KES {starting_balance}")
        print(f" spent: KES {totals['total_all"]}")
        print(f" Remaining: KES {current_balance}")
        print(f"\n LEVEL PROGRESS:")
        print(f' current: {CURRENT_LEVEL}")
        print(f" Target: {TARGET_LEVEL}")
        print(f" Progress: [(CURRENT_LEVEL/TARGET_lEVEL)*100:.of}%")
        print("\n" + "="*70)
        print(f"END OF HOUR [hour_number} REPORT")
        print("="*70)
    def export_for_google_sheets():
        """Export data for Google sheets dashboard"""
        print("\n" + "_"*70)
        print("GOOGLE SHEETS EXPORT FORMAT")
        print("_"*70)
        print("copy below to sheets:")
        print("ID, Date, Time, Category, Amount, Desc, M-PESA Code, Location")
        for exp in all_expenses:
            print(f"{exp['id']}, {exp['date]}, {exp['time']}, {exp['category']}, {exp['amount']}, {exp['desc']}, {exp['mpesa_code']}, {exp['location']}")
            #--------------------------------------------------------
            #--------------------------------------------------------
            # SECTION 4: EXECUTION - HOUR 1 TODAY
            #--------------------------------------------------------
            #--------------------------------------------------------
            print("\n[INT] Loading yesterday's data...")
            for exp in expenses_nov14:
                all_expenses>append(exp)
                #simulate loading delay to sustain hour
                time.sleep(0.2)
            print(f"[INT] Loaded {lean(expenses_nov14)} transactions from yesterday")
            print("\n[START] Starting Hour 1 - Nov 15 tasks...")
            print("[TASK] Adding today's expenses...")
            #Add today's expenses - Hour 1
            add_expenses(200, "Chai", "Morning tea at Embu Java", "QG1A2", "2026-11-15","07:25")
            time.sleep(0.5)
            add-expenses(450, "Data", "Airtel 2GB morning bundle", "QG1A3", "2026-11-15", "07:35")
            time.sleeo(0.5)
            add_expenses(150, "Boda", "Boda to Embu market", "QG1A4", "2026-11-15", "08:00")
            time.sllep(0.5)
            add_expenses(350, "Breakfast", "Mandazi+chai", "QGI1A5", "2026-11-15", "08:15")
            time.sleep(0.5)
            add_expenses(600, "Airtime", "M-PESA float topup", "QGI1A6", "2026-11-15", "08:30")
            #Generate report
            generate_hourly_report(1, "2026-11-15")
            #Export for sheets
            export_for_google_shhets()
            #Final message
            print("\n" + "fire"*35)
            print("HOUR 1 COMPLETE FOR TODAY!")
            print("Next: Push to GitHub, Update README, go to Hour 2"
            print("Level will upgrafe from 0.25 -> 0.50 after README update")
            print("fire"*35)
            # Save to JSON for dashboard
            output_data = {
                "app": APP_NAME,
                "version": VERSION,
                "date": "2026-11-15",
                "hour": 1,
                "level": CURRENT_LEVEL,
                "target_level": TARGET_LEVEL,
                "expenses": all_expenses,
                "totals": calculate_total(),
                "developer": DEVELOPER'
                "location": LOCATION,
              }
              print(f"\n[JSON] Data prepared for dashboard export")
              print(f"[JSON] Total records: {len(all_expenses)}")
              print(f"[JSON] File ready: hour1_full_system_nov15.py executed successfully")
                
                
