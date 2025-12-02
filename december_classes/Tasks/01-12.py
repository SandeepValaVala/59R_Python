import tkinter as tk
from tkinter import messagebox

import mysql.connector

conn = mysql.connector.connect(
    
    user = 'root',
    password = 'S@ndeep9347vs',
    host = 'localhost',
    database = 'tkinter_db',
    autocommit = False
)

print(conn.is_connected())
cursor = conn.cursor()


remaining_chances = 3  # Global variable

def login_record():
    global remaining_chances
    
    db_username = name_entry.get()
    db_password = pass_entry.get()
    
    # MySQL check
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (db_username, db_password)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
        remaining_chances = 3  # Reset after success
    else:
        remaining_chances -= 1
        
        if remaining_chances > 0:
            messagebox.showerror(
                "Error", 
                f"Login Failed!\nRemaining Attempts: {remaining_chances}"
            )
        else:
            messagebox.showerror(
                "Locked", 
                "You have used all 3 attempts!\nPlease try again after 24 hours."
            )
            login_record.config(state="disabled")  # Disable login button



root = tk.Tk()
root.geometry("400x280")


action_frame = tk.Frame(root)
action_frame.pack()

tk.Label(action_frame,text="User_name").grid(row=0,column=0)
name_entry = tk.Entry(action_frame)
name_entry.grid(row=0,column=1,padx=10)

tk.Label(action_frame,text="Password").grid(row=1,column=0)
pass_entry = tk.Entry(action_frame)
pass_entry.grid(row=1,column=1,padx=10)

tk.Button(root,text='Login', command=login_record).pack(pady=10)

root.mainloop()



# def login_record():
#     db_username = name_entry.get()
#     db_password = pass_entry.get()

#     remaining_chances = 3
#     while remaining_chances > 0:
#         # input_username = input("Enter username : ")
#         # input_password = input("Enter password : ")
    
#         if  db_username == input_username and db_password == input_password:
#             print("login Successful")
#             break
#         else:
#             remaining_chances -= 1
#             print("login failed")
#             if remaining_chances == 0:
#                 print("please try after 24hrs")