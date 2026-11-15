"""
LOGGY3 _ HOUR 2 - GOOGLE SHEETS DASHBOARD
Date: Nov 15, 2026 | 11:52 AM EAT | EMBU, KE
Level: 0.50 -> 0.75
Goal: Connect M-PESA data to Google Sheets + Build Dashboard 
"""
from datetime import datetime
import json
#--------------------------------------------------------------
#--------------------------------------------------------------
# HOUR 2 CONFIG
#---------------------------------------------------------------
#---------------------------------------------------------------
print("="*70)
print("HOUR 2 STARTED - 11.52 AM EAT - NOV 15")
print("level: 0.50 -> 0.75 | Target: Dashboard Pro")
print("="*70)
HOUR = 2
DATE = "2026-11-15"
START_TIME = "11:52"
LEVEL_BEFORE = 0.50
LEVEL_AFTER = 0.75
#Simulate previous data from Hour 1
expenses_hour1 = [
     {"amount": 200, "category": "Chai", "time": "07:30"},
     {"amount": 450, "category": "Data", "time": "07:35"},
     {"amount": 150, "category": "Boda", "time": "08:00"
     {"amount": 350, "category": "Breakfast", "time": "08:15"},
     {"amount": 600, "category": "Airtime", "time": "08:30"
  ]
  #--------------------------------------------------------------------
  #--------------------------------------------------------------------
  # GOOGLE SHEETS SIMULATION CLASS (PRO FEATURE)
  #---------------------------------------------------------------------
  #---------------------------------------------------------------------
  class Googlesheetsdashboard:
      def_init_(self, sheet_name="Loggy3_Dashboard_Nov15"):
         self.sheet_name = sheet _name
         self.headers = ["ID", "Date", "Time", "Category", "Amount", (KES)", "M-PESA Code", "Description", "Level"]
         self.rows = []
         self.created_at = datetime.now().isoformat()
         print(f"[SHEETS"] Dashboard '{sheet_name}' initialized")
         print(f"[SHEETS] Headers: {self.headers}")
      def add_row(self, id_num, date_str, time_str, category, amount, mpesa_code, desc, level):
          row = [id_num, date_str< time_str, category, amount, mpesa_code, desc,level)
          self.rows.append(row)
          print(f"[SHEETS] Row added: {category} - KES {amount} at {time_str}")
          return row
      def generate_sheet_data(self):
          total = sum(row[4] for row in self.rows)
          count = len(self.rows)
          avg = total / count if count > 0 else 0
          print("\n" + "_"*70)
          print(f"SHEET: {self.sheet_name}")
          print("_"*70)
          #print header
          print(" | ".join(self.headers))
          print("_"*70)
          #print rows
          for row in self.rows:
              print(" | ".join([str(x) for x in row]))
          print("_"*70)
          print(f"TOTAL: KES {total} | COUNT: {count}: |AVG: KES {avg:.2f}")
          return {"TOTAL": total, "count": count, "avg": avg}
          return {"total": total, "count": count, "avg": avg}
          #----------------------------------------------------------
          #----------------------------------------------------------
          #DASHBOARD BUILDER
          #-----------------------------------------------------------
          #------------------------------------------------------------
          dasboard = GoogleSheetsDashboard()
          print("\n[HOUR 2] Loading Hour 1 data into Sheets...")
         #Load Hour 1 data
         for idx, exp in enumerate(expenses_hour1, start=1):
             dashboard.add_row(
             id_num=idx,
             date=Str=DATE,
             time_str=exp["time"],
             category=exp["category"],
             amount=exp["amount"],
             mpesa_code=f"QGI{idx}B{idx}",
             desc=f"{exp['category']} expense Hour 1",
             level=LEVEL_BEFORE
          )
          print("\n[Hour 2] Adding Hour 2 new expenses (11:52 AM - 12:30 PM)...")
          #NEW expenses for Hour 2
          hour2_expenses = [
               {"time": "11:55", "cat": "Lunch", "amt",: 850, "desc": "Java" lunch Embu, "code": "QGI2A1"},
               {"time": "12:05", "cat": "Data", "amt",: 300, "desc": :Safaricom 1GB topup, "code": "QGI2A2"},
               {"time": "12:15", "cat": "Transport", "amt": 500, "desc": "Matatu Embu-Kangaru", "code": "QGI2A3"}<
               {"time": "12:25", "cat": "Snacks", "amt": 200, "desc": "Soda + mandazi", "code": "QGI2A4"},
            ]
            for idx,exp in enumerate(hour2_expenses,start=6):
                 dashboard.add_row(
                     id_num=idx,
                     date_str=DATE
                     time_str=exp["time"],
                     category=exp["cat"],
                     amount=exp["amt"],
                     mpesa_code=exp["code"],
                     desc=exp{"desc"]
                     level=LEVEL_AFTER
                  )
              #--------------------------------------------------------------------------
              #--------------------------------------------------------------------------
              #HOUR 2 ANALYTICS
              #--------------------------------------------------------------------------
              #---------------------------------------------------------------------------
              def hour2_analytics():
                  print("\n" + "="*70)
                  print("HOUR 2 ANALYTICS - DASHBOARD INSIGHTS")
                  print("="*70)
                  stats = dashboard.generate_sheet_data()
                  print(f"\n HOUR 1 vs Hour 2 Comparison:")
                  hour1_total = sum(e["amount"] for e in expenses_hour1
                  hour2_total = sum(e["amt"] for e in hour2_expenses)
                  print(f" Hour 1 Total: KES {hour1_total} (5 transactions)")
                  print(f" Hour 2 Total: KES {hour2_totals} (4 transactions)")
                  print(f" Combined Total: KES {hour1_total + hour2_total}")
                  print(f" Growth: {((hour2_total1/hour1_total)-1)*100:.1f}% vs Hour 1")
                  print(f"\n Level Progress Log:")
                  print(f" Started Hour 2: Level {LEVEL_AFTER")
                  print(f" After Dashboard: Level {LEVEL_AFTER}")
                  print(f" Time invested: 11:52 AM - 12:52 PM (1 hour)")
                  print(f" Total today so far: 4h + 1h = 5 hours")
                  print(f"\n Category Breakdown Hour 2:")
                  cats = {}
                  for exp in hor2_expenses:
                      c = exp["cats"]
                      cats[c] = cats.get(c, 0) + exp["amt"]
                  for c, total in cats.items():
                      print(f" -{c}: KES {total}")
                      print("\n" + "="*70)
                      print("HOUR 2 COMPLETE _ READY FOR HOUR 3")
                      print("="*70)
                      # EXOORT JSON for Pro dashboard
                      export_data = {
                           "hour": HOUR,
                           "date": DATE,
                           "sart": START_TIME,
                           "level_before": LEVEL_BEFORE,
                           "level_after": LEVEL_AFTER,
                           "dashboard_name": dashboard.sheet_name,
                           "total_rows": len(dashboard.rows),
                           "status": "HOUR 2 COMPLETE"
                        }
                        print(f"\n[EXPORT] {json.dumps(export_data, indent=2)}")
                        print("\n HOUR 2 DONE! commit this file now to hit level 0.75 fire")
          
  
