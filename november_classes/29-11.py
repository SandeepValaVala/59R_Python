import tkinter as tk
from tkinter import messagebox


def button_clicked():
    # print('Button Clicked')
    messagebox.showinfo("Info","operation done")
    messagebox.showwarning("Warning", "This is a warning!")
    messagebox.showerror("Error", "Oops! Something went wrong.")
    
    
def check_button_clicked():
    # print(var.get())
    # print('Check Box Clicked')
    if var.get() == 1:
        print("Thanks for accepting T & C")
    else:
        print("Please accept T & C")

root = tk.Tk()

root.title('My Tkinter application')
root.geometry('500x500')

tk.Label(root,text='This is my applicaation',font=('Arial',16)).pack()
tk.Label(root,text='Sandeep',font=('Arial',10)).pack(pady=20)
tk.Button(root,text='Save Button',command=button_clicked).pack()
# Entry
tk.Entry(root).pack()
# tk.Text(root).pack()
tk.Text(root,height=5,width=20).pack()


# check box

var = tk.IntVar()

tk.Checkbutton(root,text='I agree T & C',command=check_button_clicked,variable=var).pack()

# radio butttons

var1 = tk.StringVar()
tk.Radiobutton(root,text='Male',value='m',variable=var1).pack()
tk.Radiobutton(root,text='Female',value='f',variable=var1).pack()
tk.Radiobutton(root,text='Other',value='o',variable=var1).pack()

# message box

  







root.mainloop()