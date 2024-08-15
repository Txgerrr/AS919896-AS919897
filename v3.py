import tkinter
from tkinter import ttk
from tkinter import messagebox  # Import messagebox


label_width = 20
other_width = 10


def hire_window():
    def submit_hire():
        messagebox.showinfo("Submission Successful", "Your hire information has been submitted successfully!")

    window = tkinter.Tk()
    window.title("Juile's Party Hire")

    frame = tkinter.Frame(window)
    frame.pack()
    # Saving user info
    user_info_frame = tkinter.LabelFrame(frame, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=20)

    first_name_label = tkinter.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tkinter.Label(user_info_frame, text="Last Name")
    last_name_label.grid(row=1, column=0)

    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)

    item = tkinter.Label(user_info_frame, text="Title")
    item_combobox = ttk.Combobox(user_info_frame, value=["Chair", "Balloon", "Candles"])
    item.grid(row=3, column=0)
    item_combobox.grid(row=3, column=1)

    amount_label = tkinter.Label(user_info_frame, text="Amount")
    amount_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=10)
    amount_label.grid(row=4, column=0)
    amount_spinbox.grid(row=4, column=1)

    home_button = tkinter.Button(user_info_frame, text="Home", width=label_width, command=window.destroy)
    home_button.grid(row=5, column=1)

    submit_button = tkinter.Button(user_info_frame, text="Submit", width=label_width, command=submit_hire)
    submit_button.grid(row=5, column=0)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


def return_window():
    return1 = tkinter.Tk()
    return1.title("Juile's Party Hire")

    return_frame = tkinter.Frame(return1)
    return_frame.pack()
    # Saving user info
    user_return_frame = tkinter.LabelFrame(return_frame, text="User Information")
    user_return_frame.grid(row=0, column=0, padx=20, pady=20)

    first_name_return_label = tkinter.Label(user_return_frame, text="First Name")
    first_name_return_label.grid(row=0, column=0)
    last_return_name_label = tkinter.Label(user_return_frame, text="Last Name")
    last_return_name_label.grid(row=1, column=0)

    first_return_name_entry = tkinter.Entry(user_return_frame)
    last_return_name_entry = tkinter.Entry(user_return_frame)
    first_return_name_entry.grid(row=0, column=1)
    last_return_name_entry.grid(row=1, column=1)

    return_item = tkinter.Label(user_return_frame, text="Title")
    return_item_combobox = ttk.Combobox(user_return_frame, value=["Chair", "Balloon", "Candles"])
    return_item.grid(row=3, column=0)
    return_item_combobox.grid(row=3, column=1)

    return_amount_label = tkinter.Label(user_return_frame, text="Amount")
    return_amount_spinbox = tkinter.Spinbox(user_return_frame, from_=1, to=10)
    return_amount_label.grid(row=4, column=0)
    return_amount_spinbox.grid(row=4, column=1)

    return_receipt_number = tkinter.Label(user_return_frame, text="Receipt Number")
    return_receipt_number.grid(row=5, column=0)
    return_receipt_number_entry = tkinter.Entry(user_return_frame)
    return_receipt_number_entry.grid(row=5, column=1)

    return_home_button = tkinter.Button(user_return_frame, text="Home", command=return1.destroy, width=label_width)
    return_home_button.grid(row=6, column=1)

    return_submit_button = tkinter.Button(user_return_frame, text="Submit", width=label_width)
    return_submit_button.grid(row=6, column=0)

    for widget in user_return_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


def quit_window():
    quit_main = tkinter.Tk()
    quit_main.title("Quit Menu")

    quit_frame = tkinter.Frame(quit_main)
    quit_frame.pack()

    quit_option = tkinter.LabelFrame(quit_frame, text="Would You Like To Quit")
    quit_option.grid(row=0, column=0, padx=20, pady=20)

    yes = tkinter.Button(quit_option, text="Yes", width=other_width)
    yes.grid(row=1, column=0, padx=10, pady=10)

    no = tkinter.Button(quit_option, text="No", command=quit_main.destroy, width=other_width)
    no.grid(row=2, column=0, padx=10, pady=10)


# Main window

window_main = tkinter.Tk()
window_main.title("Juile's Party Hire")

frame_main = tkinter.Frame(window_main)
frame_main.pack()
# Saving user info
hire_info_frame = tkinter.LabelFrame(frame_main, text="Welcome To The Party Hire")
hire_info_frame.grid(row=0, column=0, padx=20, pady=10)

button_main = tkinter.Button(hire_info_frame, text="Hire", command=hire_window)
button_main.grid(row=1, column=0, padx=60, pady=10)

button_return = tkinter.Button(hire_info_frame, text="Return", command=return_window)
button_return.grid(row=2, column=0, padx=10, pady=10)

button_quit = tkinter.Button(hire_info_frame, text="Quit", command=quit_window)
button_quit.grid(row=3, column=0, padx=10, pady=10)

window_main.mainloop()
