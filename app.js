const STORAGE_KEY = "loggy3-mpesa-transactions";

const smsInput = document.querySelector("#smsInput");
const addBtn = document.querySelector("#addBtn");
const exportBtn = document.querySelector("#exportBtn");
const clearBtn = document.querySelector("#clearBtn");
const message = document.querySelector("#message");

let transactions = loadTransactions();

function loadTransactions() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    return [];
  }
}

function saveTransactions() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(transactions));
}

function parseMpesaSms(text) {
  const sms = text.trim();
  if (!sms) throw new Error("Paste an M-PESA SMS first.");

  const codeMatch = sms.match(/\b([A-Z0-9]{10})\b/i);
  const amountMatch = sms.match(/Kshs?\.?\s*([\d,]+(?:\.\d{1,2})?)/i);
  if (!amountMatch) throw new Error("No valid KES amount found in the message.");

  const amount = Number(amountMatch[1].replace(/,/g, ""));
  if (!Number.isFinite(amount) || amount <= 0) throw new Error("The amount is invalid.");

  let type = "other";
  let party = "";

  if (/sent to/i.test(sms)) {
    type = "sent";
    party = sms.match(/sent to\s+(.+?)\s+on\b/i)?.[1]?.trim() || "";
  } else if (/paid to/i.test(sms)) {
    type = "purchase";
    party = sms.match(/paid to\s+(.+?)\s+on\b/i)?.[1]?.trim() || "";
  } else if (/you have received/i.test(sms)) {
    type = "received";
    party = sms.match(/from\s+(.+?)\.?\s*(?:on|\.\s*New)/i)?.[1]?.trim() || "";
  } else if (/withdrawn/i.test(sms)) {
    type = "withdrawal";
  }

  const dateMatch = sms.match(/\bon\s+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b/i);
  const balanceMatch = sms.match(/(?:balance(?: is)?|balance of)\s*(?:is\s*)?Kshs?\.?\s*([\d,]+(?:\.\d{1,2})?)/i);

  return {
    id: `${Date.now()}-${Math.random().toString(16).slice(2)}`,
    code: codeMatch?.[1]?.toUpperCase() || "—",
    amount,
    type,
    party,
    date: dateMatch?.[1] || new Date().toISOString().slice(0, 10),
    balance: balanceMatch ? Number(balanceMatch[1].replace(/,/g, "")) : null,
    raw: sms,
    createdAt: new Date().toISOString()
  };
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function render() {
  const rows = [...transactions].reverse();
  document.querySelector("#transactions").innerHTML = rows.map(tx => `
    <tr>
      <td>${escapeHtml(tx.date)}</td>
      <td>${escapeHtml(tx.code)}</td>
      <td>${escapeHtml(tx.type)}</td>
      <td>${escapeHtml(tx.party || "—")}</td>
      <td>KES ${tx.amount.toFixed(2)}</td>
    </tr>
  `).join("") || '<tr><td colspan="5">No transactions yet</td></tr>';

  const spent = transactions
    .filter(tx => tx.type !== "received")
    .reduce((sum, tx) => sum + tx.amount, 0);

  const latestBalance = [...transactions].reverse().find(tx => tx.balance !== null)?.balance;
  document.querySelector("#count").textContent = transactions.length;
  document.querySelector("#total").textContent = `KES ${spent.toFixed(2)}`;
  document.querySelector("#balance").textContent = latestBalance == null ? "Not found" : `KES ${latestBalance.toFixed(2)}`;
}

function showMessage(text, error = false) {
  message.textContent = text;
  message.className = `message ${error ? "error" : "success"}`;
}

addBtn.addEventListener("click", () => {
  try {
    const transaction = parseMpesaSms(smsInput.value);
    transactions.push(transaction);
    saveTransactions();
    render();
    smsInput.value = "";
    showMessage("Transaction added successfully.");
  } catch (error) {
    showMessage(error.message, true);
  }
});

exportBtn.addEventListener("click", () => {
  if (!transactions.length) {
    showMessage("Nothing to export yet.", true);
    return;
  }

  const headers = ["Date", "Code", "Type", "Party", "Amount", "Balance", "Raw SMS"];
  const rows = transactions.map(tx => [
    tx.date, tx.code, tx.type, tx.party, tx.amount,
    tx.balance ?? "", tx.raw
  ]);
  const csv = [headers, ...rows]
    .map(row => row.map(value => `"${String(value).replaceAll('"', '""')}"`).join(","))
    .join("\n");

  const url = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = "loggy3-mpesa-transactions.csv";
  link.click();
  URL.revokeObjectURL(url);
  showMessage("CSV export downloaded.");
});

clearBtn.addEventListener("click", () => {
  if (!transactions.length || confirm("Delete every saved transaction?")) {
    transactions = [];
    saveTransactions();
    render();
    showMessage("All transactions cleared.");
  }
});

render();
