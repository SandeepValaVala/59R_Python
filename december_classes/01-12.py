import tkinter as tk
import csv 
from tkinter import messagebox
from tkinter import filedialog

# use for mysql database to python connect
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

# use for upload file into myfiles for button operation
def file_open():
    file = filedialog.askopenfilename(filetypes=[('CSV FILES Desc','*.csv')])


    with open(file,'r') as f:
        reader = csv.reader(f)
        print(next(reader))
        
        for row in reader:
            # print(row)
            
            cursor.execute(
                '''INSERT INTO STUDENTS(NAME,CLASS,GRADE) 
                VALUES (%s,%s,%s)
                ''',row
            )
        conn.commit()
        messagebox.showinfo('Info','Dta saved to db')

# data can be stored in DB we can bring back to text(area to show visible ) def function
def fill_text_box():
    text_box.configure(state='normal')
    text_box.delete('1.0',tk.END)
    cursor.execute('SELECT * FROM STUDENTS')
    for row in cursor.fetchall():
        print(row)
        text_box.insert(tk.END,f"Id :{row[0]}, Name : {row[1]}, Class :{row[2]}, Grade : {row[3]}\n")
    text_box.configure(state='disabled')

# create records for add,update,delete

def add_record():
    name = name_entry.get()
    class_ = class_entry.get()
    grade = grade_entry.get()
    
    cursor.execute(''' INSERT INTO STUDENTS (NAME,CLASS,GRADE)
                   VALUES (%s,%s,%s)
                   ''',(name,class_,grade))
    conn.commit()
    messagebox.showinfo('Info','Record added')
    fill_text_box()
    
def update_record():
    id = id_entry.get()
    name = name_entry.get()
    class_ = class_entry.get()
    grade = grade_entry.get()
    
    cursor.execute(''' UPDATE STUDENTS SET NAME = %s,CLASS = %s,GRADE = %s WHERE ID = %s''',(name,class_,grade,id))
    
    conn.commit()
    messagebox.showinfo('Info','updated record_added')
    fill_text_box()

def delete_record():
    pass
    # id = id_entry
    
    # cursor.execute(''' DELETE FROM STUDENTS WHERE ID = %s''',(id,))

    # conn.commit()
    # messagebox.showinfo("Success", "Record deleted successfully!")
    # fill_text_box()

root = tk.Tk()
root.geometry('500x500')


tk.Button(root,text='UPLOAD CSV', command=file_open).pack(pady=10)

text_box = tk.Text(root,height=10,width=50)
text_box.pack(pady=20)

# create one frame

action_frame = tk.Frame(root)
action_frame.pack()

tk.Label(action_frame,text='ID').grid(row=0,column=0)
id_entry = tk.Entry(action_frame,width=4)
id_entry.grid(row=0,column=1,)

tk.Label(action_frame,text='NAME').grid(row=0,column=2)
name_entry = tk.Entry(action_frame)
name_entry.grid(row=0,column=3)

tk.Label(action_frame,text='CLASS').grid(row=0,column=4)
class_entry = tk.Entry(action_frame,width=2)
class_entry.grid(row=0,column=5)

tk.Label(action_frame,text='GRADE').grid(row=0,column=6)
grade_entry = tk.Entry(action_frame,width=2)
grade_entry.grid(row=0,column=7)

tk.Button(action_frame,text='Add', command= add_record).grid(row = 1,column=0,padx=20)
tk.Button(action_frame,text='Update', command=update_record).grid(row = 1,column=1,padx=10)
tk.Button(action_frame,text='Delete', command=delete_record).grid(row = 1,column=2,padx=10)

fill_text_box() #call the text_ box function

root.mainloop()



# db_username = "sai"
# db_password = "12345"

# remaining_chances = 3
# while remaining_chances > 0:
#     input_username = input("Enter username : ")
#     input_password = input("Enter password : ")
    
#     if  db_username == input_username and db_password == input_password:
#         print("login Successful")
#         break
#     else:
#         remaining_chances -= 1
#         print("login failed")
#         if remaining_chances == 0:
#             print("please try after 24hrs")
