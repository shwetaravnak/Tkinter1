from tkinter import*
from tkinter import messagebox
import mysql.connector
from exp92 import disp

def insert(top):
    name = name1.get()
    password = pass1.get()
    print(name, password)
    messagebox.showinfo("Hello",f"Submitted Successfully {name}, {password}")
    
    try:
        myconn = mysql.connector.connect(host="localhost",user="root", passwd="shweta123", database="tkinter1")
        cur = myconn.cursor()
        sql = "INSERT INTO student(name, password) VALUES (%s, %s)"
        val = (name, password)


        cur.execute(sql, val)
        myconn.commit()

    except Exception as e:
        print("Error:", e)
        myconn.rollback()

    finally:
        print(cur.rowcount, "record inserted!")
        myconn.close()

    top.destroy()
    disp()

def create_gui():
    top = Tk()
    top.geometry("300x250")
    top.title("Insert Student Data")
    global name1, pass1
    name = Label(top, text="Name:", bd=4, cursor="arrow", font=("Times New Roman", 14), fg="Black")
    name.grid(row=1, column=1)
    name1 = Entry(top)
    name1.grid(row=1, column=2)
    
    password = Label(top, text="Password:", bd=4, cursor="arrow", font=("Times New Roman", 14), fg="Black")
    password.grid(row=4, column=1)
    pass1 = Entry(top, show="*")  
    pass1.grid(row=4, column=2)
    
    submit_button = Button(top, text="Submit", font=("Times New Roman", 14), fg="Red", bg="Aqua", activebackground="pink", command=lambda: insert(top))
    submit_button.grid(row=6, column=2)
    
    top.mainloop()

create_gui()   