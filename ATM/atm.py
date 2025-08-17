import tkinter as tk
from tkinter import messagebox

# ATM data
password = 5656
bal = 50000
bankacc = 23456789
phone = 9887766554
Otp = 8888

root = tk.Tk()
root.title("ATM Machine")
root.geometry("400x500")
root.config(bg="#739BB1")


def show_menu():
    clear_frame()
    tk.Label(root, text="Welcome to ATM", font=("times new roman",65, "bold"),width=120,fg="white", bg="#4A6575").pack(pady=25)

    # Buttons instead of typing option number
    tk.Button(root, text="Check Balance", font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=check_balance_screen).pack(pady=10)
    tk.Button(root, text="Deposit",font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=deposit_screen).pack(pady=10)
    tk.Button(root, text="Withdraw",font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=withdraw_screen).pack(pady=10)
    tk.Button(root, text="Pin Generate", font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=pin_generate_screen).pack(pady=10)
    tk.Button(root, text="Change Pin",font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=change_pin_screen).pack(pady=10)
    tk.Button(root, text="Quit", font=("times new roman",20, "bold"),width=25,fg="#4A6575",command=quit).pack(pady=10)



def check_balance_screen():
    clear_frame()
    tk.Label(root, text="Balance Enquiry", font=("times new roman",65, "bold"),width=120, fg="white", bg="#4A6575").pack(pady=10)

    tk.Label(root, text="Enter PIN:",font=("times new roman",20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    pin_entry = tk.Entry(root, show="*",width=30)
    pin_entry.pack(pady=5)

    def check():
        if pin_entry.get().isdigit() and int(pin_entry.get()) == password:
            messagebox.showinfo("Balance", f"Your balance is ₹{bal}")
            show_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    tk.Button(root, text="Check",font=("times new roman",17), bg="#3A8E48",command=check).pack(pady=10)
    tk.Button(root, text="Back",font=("times new roman",14),bg="#99A127",command=show_menu).pack()


def deposit_screen():
    clear_frame()
    tk.Label(root, text="Deposit", font=("times new roman",65, "bold"),width=120, fg="white", bg="#4A6575").pack(pady=20)

    tk.Label(root, text="Enter PIN:",font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    pin_entry = tk.Entry(root, show="*",width=30)
    pin_entry.pack(pady=10)

    tk.Label(root, text="Enter Amount:",font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    amt_entry = tk.Entry(root,width=30)
    amt_entry.pack(pady=10)

    def deposit():
        global bal
        if pin_entry.get().isdigit() and int(pin_entry.get()) == password:
            if amt_entry.get().isdigit():
                a = int(amt_entry.get())
                if a % 100 == 0:
                    bal += a
                    messagebox.showinfo("Deposit", f"₹{a} deposited\nNew Balance: ₹{bal}")
                    show_menu()
                else:
                    messagebox.showwarning("Error", "Enter multiples of 100")
            else:
                messagebox.showerror("Error", "Invalid Amount")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    tk.Button(root, text="Deposit", font=("times new roman",17), bg="#3A8E48",command=deposit).pack(pady=10)
    tk.Button(root, text="Back", font=("times new roman",17), bg="#99A127",command=show_menu).pack()


def withdraw_screen():
    clear_frame()
    tk.Label(root, text="Withdraw", font=("times new roman",65, "bold"),width=120, fg="white", bg="#4A6575").pack(pady=20)

    tk.Label(root, text="Enter PIN:",font=("times new roman",20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    pin_entry = tk.Entry(root, show="*",width=30)
    pin_entry.pack(pady=10)

    tk.Label(root, text="Enter Amount:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    amt_entry = tk.Entry(root,width=30)
    amt_entry.pack(pady=10)

    def withdraw():
        global bal
        if pin_entry.get().isdigit() and int(pin_entry.get()) == password:
            if amt_entry.get().isdigit():
                a = int(amt_entry.get())
                if a <= bal and a % 100 == 0:
                    bal -= a
                    messagebox.showinfo("Withdraw", f"₹{a} withdrawn\nRemaining Balance: ₹{bal}")
                    show_menu()
                elif a > bal:
                    messagebox.showwarning("Error", "Insufficient Balance")
                else:
                    messagebox.showwarning("Error", "Enter multiples of 100")
            else:
                messagebox.showerror("Error", "Invalid Amount")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    tk.Button(root, text="Withdraw",font=("times new roman",17), bg="#3A8E48", command=withdraw).pack(pady=10)
    tk.Button(root, text="Back",font=("times new roman",17), bg="#99A127", command=show_menu).pack()


def pin_generate_screen():
    clear_frame()
    tk.Label(root, text="Pin Generate", font=("times new roman",65, "bold"),width=120, fg="white", bg="#4A6575").pack(pady=20)

    tk.Label(root, text="Enter Account No:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    acc_entry = tk.Entry(root,width=30)
    acc_entry.pack(pady=10)

    tk.Label(root, text="Enter Phone No:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    phone_entry = tk.Entry(root,width=30)
    phone_entry.pack(pady=10)

    tk.Label(root, text="Enter OTP:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    otp_entry = tk.Entry(root,width=30)
    otp_entry.pack(pady=10)

    tk.Label(root, text="Enter New PIN:",font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    new_entry = tk.Entry(root, show="*",width=30)
    new_entry.pack(pady=10)

    def generate():
        global password
        if acc_entry.get().isdigit() and int(acc_entry.get()) == bankacc:
            if phone_entry.get().isdigit() and int(phone_entry.get()) == phone:
                if otp_entry.get().isdigit() and int(otp_entry.get()) == Otp:
                    if new_entry.get().isdigit():
                        password = int(new_entry.get())
                        messagebox.showinfo("Success", "PIN generated successfully")
                        show_menu()
                    else:
                        messagebox.showerror("Error", "Invalid New PIN")
                else:
                    messagebox.showerror("Error", "Wrong OTP")
            else:
                messagebox.showerror("Error", "Wrong Phone No")
        else:
            messagebox.showerror("Error", "Wrong Account No")

    tk.Button(root, text="Generate", font=("times new roman",17), bg="#3A8E48",command=generate).pack(pady=10)
    tk.Button(root, text="Back", font=("times new roman",17), bg="#99A127",command=show_menu).pack()


def change_pin_screen():
    clear_frame()
    tk.Label(root, text="Change PIN", font=("times new roman",65, "bold"),width=120, fg="white", bg="#4A6575").pack(pady=20)

    tk.Label(root, text="Enter Old PIN:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    old_entry = tk.Entry(root, show="*",width=30)
    old_entry.pack(pady=10)

    tk.Label(root, text="Enter New PIN:", font=("times new roman", 20,"bold"),fg="#BD1010",bg="#739BB1").pack()
    new_entry = tk.Entry(root, show="*",width=30)
    new_entry.pack(pady=10)

    def change():
        global password
        if old_entry.get().isdigit() and int(old_entry.get()) == password:
            if new_entry.get().isdigit():
                password = int(new_entry.get())
                messagebox.showinfo("Success", "PIN changed successfully")
                show_menu()
            else:
                messagebox.showerror("Error", "Invalid New PIN")
        else:
            messagebox.showerror("Error", "Invalid Old PIN")

    tk.Button(root, text="Change",font=("times new roman",17), bg="#3A8E48",command=change).pack(pady=10)
    tk.Button(root, text="Back",font=("times new roman",17), bg="#99A127",command=show_menu).pack()


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


# Start App
show_menu()
root.mainloop()
