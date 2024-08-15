import tkinter as tk
from tkinter import messagebox

class PartyHire:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Julie's Party Hire")
        self.main_window = MainWindow(self)
        self.hired_items = []  # List to store hired items
        self.receipt_counter = 1  # Counter to generate receipt numbers
        self.root.mainloop()

class MainWindow:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root)
        self.frame.pack()

        tk.Label(self.frame, text="Welcome to the party hire", font=("Helvetica", 16)).pack(pady=10)
        
        self.hire_button = tk.Button(self.frame, text="HIRE", command=self.open_hire_form, width=15)
        self.return_button = tk.Button(self.frame, text="RETURN", command=self.open_return_form, width=15)
        self.quit_button = tk.Button(self.frame, text="QUIT", command=self.confirm_quit, width=15)

        self.hire_button.pack(pady=5)
        self.return_button.pack(pady=5)
        self.quit_button.pack(pady=5)

    def open_hire_form(self):
        self.frame.pack_forget()
        HireForm(self.app)

    def open_return_form(self):
        self.frame.pack_forget()
        ReturnForm(self.app)

    def confirm_quit(self):
        ConfirmationDialog(self.app)

class HireForm:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root)
        self.frame.pack()

        tk.Label(self.frame, text="ITEM INFORMATION", font=("Helvetica", 14)).pack(pady=10)

        self.first_name_label = tk.Label(self.frame, text="First Name:")
        self.first_name_entry = tk.Entry(self.frame)

        self.last_name_label = tk.Label(self.frame, text="Last Name:")
        self.last_name_entry = tk.Entry(self.frame)

        self.items_label = tk.Label(self.frame, text="Items Chosen:")
        self.items_entry = tk.Entry(self.frame)

        self.amount_label = tk.Label(self.frame, text="Amount:")
        self.amount_entry = tk.Entry(self.frame)

        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.items_label.pack()
        self.items_entry.pack()
        self.amount_label.pack()
        self.amount_entry.pack()

        tk.Button(self.frame, text="Submit", command=self.submit_hire).pack(pady=5)
        tk.Button(self.frame, text="Print Receipt", command=self.print_receipt).pack(pady=5)
        tk.Button(self.frame, text="Back", command=self.go_back).pack(pady=5)

    def submit_hire(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        items = self.items_entry.get()
        amount = self.amount_entry.get()

        if first_name and last_name and items and amount.isdigit():
            item_data = {
                "first_name": first_name,
                "last_name": last_name,
                "items": items,
                "amount": int(amount)
            }
            self.app.hired_items.append(item_data)
            messagebox.showinfo("Success", "Item hired successfully!")
            self.go_back()
        else:
            messagebox.showerror("Error", "Please fill all fields correctly.")

    def print_receipt(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        items = self.items_entry.get()
        amount = self.amount_entry.get()

        if first_name and last_name and items and amount.isdigit():
            item_data = {
                "first_name": first_name,
                "last_name": last_name,
                "items": items,
                "amount": int(amount)
            }
            Receipt(self.app, item_data, "Hire")
        else:
            messagebox.showerror("Error", "Please fill all fields correctly.")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_window.frame.pack()

class ReturnForm:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root)
        self.frame.pack()

        tk.Label(self.frame, text="ITEM INFORMATION", font=("Helvetica", 14)).pack(pady=10)

        self.first_name_label = tk.Label(self.frame, text="First Name:")
        self.first_name_entry = tk.Entry(self.frame)

        self.last_name_label = tk.Label(self.frame, text="Last Name:")
        self.last_name_entry = tk.Entry(self.frame)

        self.items_label = tk.Label(self.frame, text="Items Chosen:")
        self.items_entry = tk.Entry(self.frame)

        self.amount_label = tk.Label(self.frame, text="Amount:")
        self.amount_entry = tk.Entry(self.frame)

        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.items_label.pack()
        self.items_entry.pack()
        self.amount_label.pack()
        self.amount_entry.pack()

        tk.Button(self.frame, text="Submit", command=self.submit_return).pack(pady=5)
        tk.Button(self.frame, text="Back", command=self.go_back).pack(pady=5)

    def submit_return(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        items = self.items_entry.get()
        amount = self.amount_entry.get()

        if first_name and last_name and items and amount.isdigit():
            item_data = {
                "first_name": first_name,
                "last_name": last_name,
                "items": items,
                "amount": int(amount)
            }
            # For simplicity, appending to the same list
            self.app.hired_items.append(item_data)
            messagebox.showinfo("Success", "Item returned successfully!")
            self.print_receipt(item_data)
        else:
            messagebox.showerror("Error", "Please fill all fields correctly.")

    def print_receipt(self, data):
        Receipt(self.app, data, "Return")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_window.frame.pack()

class Receipt:
    def __init__(self, app, data, mode):
        self.app = app
        self.data = data
        self.mode = mode
        self.frame = tk.Frame(self.app.root)
        self.frame.pack()

        if self.mode == "Hire":
            tk.Label(self.frame, text="ITEM HIRED", font=("Helvetica", 14)).pack(pady=10)
        else:
            tk.Label(self.frame, text="ITEM RETURNED", font=("Helvetica", 14)).pack(pady=10)

        tk.Label(self.frame, text=f"First Name: {data['first_name']}").pack()
        tk.Label(self.frame, text=f"Last Name: {data['last_name']}").pack()
        tk.Label(self.frame, text=f"Items: {data['items']}").pack()
        tk.Label(self.frame, text=f"Amount: {data['amount']}").pack()
        tk.Label(self.frame, text=f"Receipt Number: {self.app.receipt_counter}").pack()

        tk.Button(self.frame, text="FINISH", command=self.finish).pack(pady=5)
        tk.Button(self.frame, text="BACK", command=self.go_back).pack(pady=5)

        self.app.receipt_counter += 1  # Increment the receipt counter after displaying the receipt

    def finish(self):
        self.frame.pack_forget()
        self.app.main_window.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        if self.mode == "Hire":
            HireForm(self.app)
        elif self.mode == "Return": 
            ReturnForm(self.app)

class ConfirmationDialog:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root)
        self.frame.pack()

        tk.Label(self.frame, text="Are you sure you want to quit?", font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.frame, text="YES", command=self.quit).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame, text="NO", command=self.cancel).pack(side=tk.RIGHT, padx=5)

    def quit(self):
        self.app.root.destroy()

    def cancel(self):
        self.frame.pack_forget()
        self.app.main_window.frame.pack()

# Run the application
if __name__ == "__main__":
    app = PartyHire()
