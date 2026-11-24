# Loggy3 M-PESA Expense Tracker

A working, browser-based M-PESA SMS parser and expense tracker.

## Features

- Paste and parse M-PESA SMS messages
- Automatically detect transaction code, amount, type, party, date, and balance
- Save transactions in browser storage
- View totals and the latest detected balance
- Export all transactions as CSV
- Work entirely offline after loading

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Publish with GitHub Pages

1. Merge this branch into `main`.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select `main` and the `/ (root)` folder.
