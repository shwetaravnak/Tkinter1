from tkinter import*
from tkinter import ttk, messagebox
import mysql.connector

def screen2(root):
    root.geometry("450x500")
    root.title("Student Information")

    try:
        myconn = mysql.connector.connect(host="localhost",user="root", passwd="shweta123", database="tkinter1")
        cur = myconn.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        myconn.close()

    except Exception as e:
        messagebox.showerror("Database Error", f"Error fetching data:{e}")
        return 

    cols = ("ID", "Name", "Password")
    tree = ttk.Treeview(root, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    
    for row in rows:
        tree.insert("", "end", values=row)

    scrollbar = Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")  


    tree.pack(expand=True, fill="both")

def disp():
    screen2(Tk())
