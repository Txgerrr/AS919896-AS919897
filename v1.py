import tkinter as tk
from tkinter import ttk, messagebox
import random

class PartyHireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Julie's Party Hire")

        self.receipts = {}  # Dictionary to store receipt details

        self.main_window()

    def main_window(self):
        self.clear_window()
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)

        hire_button = tk.Button(main_frame, text="HIRE", command=self.hire_form)
        hire_button.pack(pady=5)

        return_button = tk.Button(main_frame, text="RETURN", command=self.return_form)
        return_button.pack(pady=5)

        stored_receipts_button = tk.Button(main_frame, text="STORED RECEIPTS", command=self.view_stored_receipts)
        stored_receipts_button.pack(pady=5)

        quit_button = tk.Button(main_frame, text="QUIT", command=self.confirm_quit)
        quit_button.pack(pady=5)

    def hire_form(self):
        self.clear_window()
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(form_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(form_frame)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Items Chosen:").grid(row=2, column=0, padx=5, pady=5)
        self.items_chosen = ttk.Combobox(form_frame, values=["Item1", "Item2", "Item3"])
        self.items_chosen.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Amount:").grid(row=3, column=0, padx=5, pady=5)
        self.amount_entry = tk.Spinbox(form_frame, from_=1, to=100)          
        self.amount_entry.grid(row=3, column=1, padx=5, pady=5)

        submit_button = tk.Button(form_frame, text="Submit", command=self.submit_hire)
        submit_button.grid(row=4, column=0, padx=50, pady=10)

        back_button = tk.Button(form_frame, text="Back", command=self.main_window)
        back_button.grid(row=4, column=1, padx=50, pady=10)

    def return_form(self):
        self.clear_window()
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(form_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(form_frame)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Items Chosen:").grid(row=2, column=0, padx=5, pady=5)
        self.items_chosen = ttk.Combobox(form_frame, values=["Item1", "Item2", "Item3"])
        self.items_chosen.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Amount:").grid(row=3, column=0, padx=5, pady=5)
        self.amount_entry = tk.Spinbox(form_frame, from_=1, to=100)
        self.amount_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Receipt Number:").grid(row=4, column=0, padx=5, pady=5)
        self.receipt_entry = tk.Entry(form_frame)
        self.receipt_entry.grid(row=4, column=1, padx=5, pady=5)

        submit_button = tk.Button(form_frame, text="Submit", command=self.submit_return)
        submit_button.grid(row=5, column=0, padx=5, pady=5)

        back_button = tk.Button(form_frame, text="Back", command=self.main_window)
        back_button.grid(row=5, column=1, padx=5, pady=5)

    def print_receipt_hire(self):
        if self.validate_hire_form():
            receipt_number = self.generate_receipt_number()
            receipt_details = {
                "First Name": self.first_name_entry.get(),
                "Last Name": self.last_name_entry.get(),
                "Items Chosen": self.items_chosen.get(),
                "Amount": self.amount_entry.get(),
                "Receipt Number": receipt_number
            }
            self.receipts[receipt_number] = receipt_details

            receipt_window = tk.Toplevel(self.root)
            receipt_window.title("Receipt")

            receipt_frame = tk.Frame(receipt_window)
            receipt_frame.pack(pady=20)

            tk.Label(receipt_frame, text="First Name: " + self.first_name_entry.get()).grid(row=0, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Last Name: " + self.last_name_entry.get()).grid(row=1, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Items Chosen: " + self.items_chosen.get()).grid(row=2, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Amount: " + self.amount_entry.get()).grid(row=3, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Receipt Number: " + str(receipt_number)).grid(row=4, column=0, padx=5, pady=5)

            finish_button = tk.Button(receipt_frame, text="FINISH", command=lambda: [receipt_window.destroy(), self.main_window()])
            finish_button.grid(row=5, column=0, padx=5, pady=5)

    def print_receipt_return(self):
        if self.validate_return_form():
            receipt_window = tk.Toplevel(self.root)
            receipt_window.title("Receipt")

            receipt_frame = tk.Frame(receipt_window)
            receipt_frame.pack(pady=20)

            tk.Label(receipt_frame, text="First Name: " + self.first_name_entry.get()).grid(row=0, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Last Name: " + self.last_name_entry.get()).grid(row=1, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Items Chosen: " + self.items_chosen.get()).grid(row=2, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Amount: " + self.amount_entry.get()).grid(row=3, column=0, padx=5, pady=5)
            tk.Label(receipt_frame, text="Receipt Number: " + self.receipt_entry.get()).grid(row=4, column=0, padx=5, pady=5)

            finish_button = tk.Button(receipt_frame, text="FINISH", command=lambda: [receipt_window.destroy(), self.main_window()])
            finish_button.grid(row=5, column=0, padx=5, pady=5)

    def submit_hire(self):
        if self.validate_hire_form():
            messagebox.showinfo("Success", "Hire information submitted successfully.")
            self.print_receipt_hire()

    def submit_return(self):
        if self.validate_return_form():
            messagebox.showinfo("Success", "Return information submitted successfully.")
            self.print_receipt_return()

    def validate_hire_form(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        items_chosen = self.items_chosen.get()
        amount = self.amount_entry.get()

        if not first_name or not last_name or not items_chosen or not amount:
            messagebox.showerror("Error", "All fields are required.")
            return False

        if not first_name.isalpha():
            messagebox.showerror("Error", "First name must contain only letters.")
            return False

        if not last_name.isalpha():
            messagebox.showerror("Error", "Last name must contain only letters.")
            return False

        if not amount.isdigit():
            messagebox.showerror("Error", "Amount must be a positive integer.")
            return False

        if int(amount) <= 0:
            messagebox.showerror("Error", "Amount must be greater than zero.")
            return False

        return True

    def validate_return_form(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        items_chosen = self.items_chosen.get()
        amount = self.amount_entry.get()
        receipt_number = self.receipt_entry.get()

        if not first_name or not last_name or not items_chosen or not amount or not receipt_number:
            messagebox.showerror("Error", "All fields are required.")
            return False

        if not first_name.isalpha():
            messagebox.showerror("Error", "First name must contain only letters.")
            return False

        if not last_name.isalpha():
            messagebox.showerror("Error", "Last name must contain only letters.")
            return False

        if not amount.isdigit():
            messagebox.showerror("Error", "Amount must be a positive integer.")
            return False

        if int(amount) <= 0:
            messagebox.showerror("Error", "Amount must be greater than zero.")
            return False

        if not receipt_number.isdigit():
            messagebox.showerror("Error", "Receipt number must be a positive integer.")
            return False

        if int(receipt_number) <= 0:
            messagebox.showerror("Error", "Receipt number must be greater than zero.")
            return False

        return True

    def generate_receipt_number(self):
        while True:
            receipt_number = random.randint(10000, 99999)
            if receipt_number not in self.receipts:
                return receipt_number

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def view_stored_receipts(self):
        self.clear_window()
        receipts_frame = tk.Frame(self.root)
        receipts_frame.pack(pady=20)

        if not self.receipts:
            tk.Label(receipts_frame, text="No receipts stored.").pack()
        else:
            for receipt_number, details in self.receipts.items():
                tk.Label(receipts_frame, text="Receipt Number: " + str(receipt_number)).pack()
                for key, value in details.items():
                    tk.Label(receipts_frame, text=key + ": " + str(value)).pack()
                tk.Label(receipts_frame, text="---------------------").pack()

        back_button = tk.Button(receipts_frame, text="Back", command=self.main_window)
        back_button.pack(pady=5)

    def confirm_quit(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PartyHireApp(root)
    root.mainloop()
