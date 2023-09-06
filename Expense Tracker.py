#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        total_expenses = 0
        result = "\nExpense Tracker\n----------------\n"
        for category, amount in self.expenses.items():
            result += f"{category}: ${amount}\n"
            total_expenses += amount
        result += "----------------\n"
        result += f"Total Expenses: ${total_expenses}"
        return result

def add_expense():
    category = category_entry.get()
    amount = float(amount_entry.get())
    tracker.add_expense(category, amount)
    result_label.config(text=f"Expense of ${amount} added to {category} category.")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def view_expenses():
    result = tracker.view_expenses()
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

tracker = ExpenseTracker()

root = tk.Tk()
root.title("Expense Tracker")

category_label = tk.Label(root, text="Enter the expense category:")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()

amount_label = tk.Label(root, text="Enter the expense amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

result_text = tk.Text(root, height=10, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()

