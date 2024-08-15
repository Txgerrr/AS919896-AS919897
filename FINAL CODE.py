import tkinter as tk
from tkinter import ttk, messagebox
import random
import tkinter.font as font
from tkinter import *



# Constants
CUSTOM_FONT = ("Century", "14")
NORMAL_FONT = ("Courier New", "12")
TITLE_FONT = ("Forte", "20")
LABEL_WIDTH = 15
OTHER_WIDTH = 12
VALID_ITEMS = ["Chair", "Balloon", "Candles"]

def generate_unique_receipt_number():
    # Generate a unique receipt number
    return random.randint(1000, 9999)

def validate_name(name):
    # Check if the name contains only alphabetic characters
    return name.isalpha()

def validate_number(number):
    # Check if the number is a valid integer
    return number.isdigit()


def hire_window():
    # Create and display the hire window
    def submit_hire():
        # Handle the submission of the hire form
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        item_chosen = item_combobox.get()
        amount = amount_spinbox.get()

          # Check if any fields are empty
        if not first_name or not last_name or item_chosen == "Select Item" or not amount:
            messagebox.showerror("Input Error", "Fields cannot be left blank.")
            return

        if not validate_name(first_name) or not validate_name(last_name):
            messagebox.showerror("Input Error", "Names can only contain letters. And no spaces")
            return
        try:
            amount = int (amount)
            if amount < 1 or amount > 500:
                raise ValueError
        except ValueError:
            messagebox. showwarning ("Warning!", "Please enter a valid input: amount must be less than 500")
            return
        if item_chosen not in VALID_ITEMS:
            messagebox.showerror("Input Error", "Please choose a valid item.")
            return

        receipt_number = generate_unique_receipt_number()

        receipt_window = tk.Toplevel(window)
        receipt_window.title("Receipt")
        receipt_window.configure(bg="#ccf2cc")

        tk.Label(receipt_window, text=f"Customer Name: {first_name} {last_name}", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).pack()
        tk.Label(receipt_window, text=f"Item Chosen: {item_chosen}", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).pack()
        tk.Label(receipt_window, text=f"Amount: {amount}", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).pack()
        tk.Label(receipt_window, text=f"Receipt Number: {receipt_number}", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).pack()

        tk.Button(receipt_window, text="Close", command=receipt_window.destroy, bg="#f0f0f0").pack(pady=10)

        with open("Items.txt", "a") as file:
            file.write(f"{first_name},{last_name},{item_chosen},{amount},{receipt_number}\n")

    window = tk.Toplevel()
    window.title("Juile's Party Hire")
    window.configure(bg="#ccf2cc")

    frame = tk.Frame(window, bg="#ccf2cc")
    frame.pack(padx=50, pady=50)

    user_info_frame = tk.LabelFrame(frame, text="User Information", bg="#ccf2cc", fg="black", font=TITLE_FONT)
    user_info_frame.pack(padx=20, pady=20)

    tk.Label(user_info_frame, text="First Name", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=0, column=0, pady=10,padx=20)
    tk.Label(user_info_frame, text="Last Name", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=1, column=0, pady=10, padx=20)

    first_name_entry = tk.Entry(user_info_frame)
    last_name_entry = tk.Entry(user_info_frame)
    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)

    tk.Label(user_info_frame, text="Item", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=2, column=0, pady=10)
    item_combobox = ttk.Combobox(user_info_frame, values=VALID_ITEMS, width=18)
    item_combobox.grid(row=2, column=1)
    item_combobox.set("Select Item")  # Set a default placeholder

    tk.Label(user_info_frame, text="Amount", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=3, column=0, pady=10)
    amount_spinbox = tk.Spinbox(user_info_frame, from_=1, to=10, width=18)
    amount_spinbox.grid(row=3, column=1)

    tk.Button(user_info_frame, text="Submit", width=LABEL_WIDTH, command=submit_hire, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=4, column=1, pady=10, padx=30)
    tk.Button(user_info_frame, text="Home", width=LABEL_WIDTH, command=window.destroy, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=4, column=0, pady=10, padx=30)

def return_window():
    # Create and display the return window
    def submit_return():
        # Handle the submission of the return form
        first_name = first_return_name_entry.get()
        last_name = last_return_name_entry.get()
        item_chosen = return_item_combobox.get()
        amount = return_amount_spinbox.get()
        receipt_number = return_receipt_number_entry.get()

        if not validate_name(first_name) or not validate_name(last_name):
            messagebox.showerror("Input Error", "Names can only contain letters.")
            return
        if not validate_number(amount) or not validate_number(receipt_number):
            messagebox.showerror("Input Error", "Amount and Receipt Number must be numbers.")
            return
        if item_chosen not in VALID_ITEMS:
            messagebox.showerror("Input Error", "Please choose a valid item.")
            return

        try:
            with open("Items.txt", "r") as file:
                lines = file.readlines()
            with open("Items.txt", "w") as file:
                found = False
                for line in lines:
                    if receipt_number in line:
                        found = True
                    else:
                        file.write(line)
            if found:
                messagebox.showinfo("Success", "Return processed successfully!")
            else:
                messagebox.showerror("Error", "Receipt Number not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found.")

    return1 = tk.Toplevel()
    return1.title("Juile's Party Hire")
    return1.configure(bg="#ccf2cc")

    frame = tk.Frame(return1, bg="#ccf2cc")
    frame.pack(padx=20, pady=20)

    user_return_frame = tk.LabelFrame(frame, text="User Information", bg="#ccf2cc", fg="black", font=TITLE_FONT)
    user_return_frame.pack(padx=20, pady=20)

    tk.Label(user_return_frame, text="First Name", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=0, column=0, pady=10, padx=30)
    tk.Label(user_return_frame, text="Last Name", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=1, column=0, pady=10, padx=30)

    first_return_name_entry = tk.Entry(user_return_frame)
    last_return_name_entry = tk.Entry(user_return_frame)
    first_return_name_entry.grid(row=0, column=1)
    last_return_name_entry.grid(row=1, column=1)

    tk.Label(user_return_frame, text="Item", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=2, column=0, pady=10, padx=30)
    return_item_combobox = ttk.Combobox(user_return_frame, values=VALID_ITEMS)
    return_item_combobox.grid(row=2, column=1)
    return_item_combobox.set("Select Item")

    tk.Label(user_return_frame, text="Amount", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=3, column=0, pady=10, padx=30)
    return_amount_spinbox = tk.Spinbox(user_return_frame, from_=1, to=500)
    return_amount_spinbox.grid(row=3, column=1)

    tk.Label(user_return_frame, text="Receipt Number", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=4, column=0, pady=10, padx=30)
    return_receipt_number_entry = tk.Entry(user_return_frame)
    return_receipt_number_entry.grid(row=4, column=1)

    tk.Button(user_return_frame, text="Submit", width=LABEL_WIDTH, command=submit_return, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=5, column=0, pady=10, padx=30)
    tk.Button(user_return_frame, text="Home", width=LABEL_WIDTH, command=return1.destroy, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=5, column=1, pady=10, padx=30)

def stored_info():
    # Create and display the stored information window
    store_receipt = tk.Toplevel()
    store_receipt.title("Stored Receipts")
    store_receipt.configure(bg="#ccf2cc")

    receipt_frame = tk.Frame(store_receipt, bg="#ccf2cc")
    receipt_frame.pack(padx=20, pady=20)
   
    receipt_frame = tk.LabelFrame(receipt_frame, text="User Information", bg="#ccf2cc", fg="black", font=TITLE_FONT)
    receipt_frame.grid(row=0, column=0, padx=20, pady=20)

    tk.Label(receipt_frame, text="Customer Name", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).grid(row=0, column=0)
    tk.Label(receipt_frame, text="Item", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).grid(row=0, column=1)
    tk.Label(receipt_frame, text="Amount", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).grid(row=0, column=2)
    tk.Label(receipt_frame, text="Receipt Number", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).grid(row=0, column=3)

    row = 1
    try:
        with open("Items.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                tk.Label(receipt_frame, text=f"{data[0]} {data[1]}", bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=row, column=0)
                tk.Label(receipt_frame, text=data[2], bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=row, column=1)
                tk.Label(receipt_frame, text=data[3], bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=row, column=2)
                tk.Label(receipt_frame, text=data[4], bg="#ccf2cc", fg="black", font=NORMAL_FONT).grid(row=row, column=3)
                row += 1
    except FileNotFoundError:
        tk.Label(receipt_frame, text="No records found", bg="#ccf2cc", fg="black", font=CUSTOM_FONT).grid(row=1, column=0, columnspan=4)

    tk.Button(receipt_frame, text="Close", command=store_receipt.destroy, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=row, column=0, columnspan=4, pady=10)

def quit_program():
    # Confirm and quit the main window
    question_box = messagebox.askquestion("Exit", "Are you sure you would like to quit the program?", icon="warning")
    if question_box == "yes":
        window_main.destroy()

# Main Window
window_main = tk.Tk()
window_main.title("Party Hire")
window_main.configure(bg="#ccf2cc")

frame_main = tk.Frame(window_main, bg="#ccf2cc")
frame_main.pack(padx=20, pady=20)

Label(frame_main, text="Juile's Party Hire", font=TITLE_FONT, bg="#ccf2cc", fg="black").grid(row=0, column=0)
Button(frame_main, text="Hire", command=hire_window, width=OTHER_WIDTH, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=1, column=0, padx=60, pady=10)
tk.Button(frame_main, text="Return", command=return_window, width=OTHER_WIDTH, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=2, column=0, padx=60, pady=10)
tk.Button(frame_main, text="View Receipts", command=stored_info, width=OTHER_WIDTH, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=3, column=0, padx=60, pady=10)
tk.Button(frame_main, text="Quit", command=quit_program, width=OTHER_WIDTH, bg="#f0f0f0", fg="black", font=CUSTOM_FONT).grid(row=4, column=0, padx=60, pady=10)

window_main.mainloop()
