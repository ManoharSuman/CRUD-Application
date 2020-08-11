from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, N, S, E, W, END
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

# Insert Function

def insert():
    title_label = title_entry.get()
    title_label1 = title_entry1.get()
    title_label2 = title_entry2.get()
    title_label3 = title_entry3.get()
    if title_label == None or title_label1 == None or title_label2 == None or title_label2 == None:
        messagebox.showinfo("Data is not Provided")
    else:
        con = mysql.connect(host="localhost", user="root", password="54321", database="book_data")
        cursor = con.cursor()
        cursor.execute("insert into Books values(' "+title_label+" ',' "+title_label1+" ',' "+title_label2+" ',' "+title_label3+" ')")
        cursor.execute("commit");
        title_entry.delete(0, 'end')
        title_entry1.delete(0, 'end')
        title_entry2.delete(0, 'end')
        title_entry3.delete(0, 'end')
        messagebox.showinfo("inserted successfully")
        con.close()

# DELETE Function

def delete():
    if title_entry.get() == None:
        messagebox.showinfo("Book ID Required")
    else:
        con = mysql.connect(host="localhost", user="root", password="54321", database="book_data")
        cursor = con.cursor()
        cursor.execute("delete from books where ID =' "+ title_entry.get() +" '")
        cursor.execute("commit");
        title_entry.delete(0, 'end')
        title_entry1.delete(0, 'end')
        title_entry2.delete(0, 'end')
        title_entry3.delete(0, 'end')
        messagebox.showinfo("Deleted successfully")
        con.close()

# UPDATE Function

def update():
    title_label = title_entry.get()
    title_label1 = title_entry1.get()
    title_label2 = title_entry2.get()
    title_label3 = title_entry3.get()
    if title_label == None or title_label1 == None or title_label2 == None or title_label3 == None:
        messagebox.showinfo("Data is not Provided")
    else:
        con = mysql.connect(host="localhost", user="root", password="54321", database="book_data")
        cursor = con.cursor()
        cursor.execute("UPDATE books SET Book_Name = '"+title_label1+"', Author = '"+title_label2+"', ISBN = '"+title_label3+"' WHERE ID = '"+title_label+"' ")
        cursor.execute("commit");
        title_entry.delete(0, 'end')
        title_entry1.delete(0, 'end')
        title_entry2.delete(0, 'end')
        title_entry3.delete(0, 'end')
        messagebox.showinfo("Updated successfully")
        con.close()

# ViewList Function

def view():
    con = mysql.connect(host="localhost", user="root", password="54321", database="book_data")
    cursor = con.cursor()
    cursor.execute("select * from books")
    rows = cursor.fetchall()

    for ele in rows:
        add_listbox.insert('end', ele)

    con.close()

# Clear List Function
def clear():
    add_listbox.delete(0, END)

# Exit Window Function
def exit():
    root.quit()

# ----GUI Using Tkinter----

root = Tk()
root.title("My Book DataBase")
root.configure(background="light green")
root.geometry("1050x500")
root.resizable(width=False, height=False)
# For ID
title_label = ttk.Label(root, text="ID", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row="0", column="0", sticky=W)
title_text = int
title_entry = ttk.Entry(root, width="24", textvariable="title_text")
title_entry.grid(row="0", column="1", sticky=W)
# For Title
title_label1 = ttk.Label(root, text="Title", background="light green", font=("TkDefaultFont", 16))
title_label1.grid(row="0", column="2", sticky=W)
title_text1 = StringVar
title_entry1 = ttk.Entry(root, width="24", textvariable="title_text1")
title_entry1.grid(row="0", column="3", sticky=W)
# For Author
title_label2 = ttk.Label(root, text="Author", background="light green", font=("TkDefaultFont", 16))
title_label2.grid(row="0", column="4", sticky=W)
title_text2 = StringVar
title_entry2 = ttk.Entry(root, width="24", textvariable="title_text2")
title_entry2.grid(row="0", column="5", sticky=W)
# For ISBN
title_label3 = ttk.Label(root, text="ISBN", background="light green", font=("TkDefaultFont", 16))
title_label3.grid(row="0", column="6", sticky=W)
title_text3 = StringVar
title_entry3 = ttk.Entry(root, width="24", textvariable="title_text3")
title_entry3.grid(row="0", column="7", sticky=W)

# INSERT Button
add_btn = Button(root, text="Add Book", bg="blue", fg="white", font="helvetica 10 bold", command=insert)
add_btn.grid(row="0", column="8", sticky=W)

# ListBOX
add_listbox = Listbox(root, height=16, width=40, bg="light blue", font="helvetica 13")
add_listbox.grid(row="3", column="1", columnspan="14", sticky=W+E, pady=40, padx=15)
# Add Scrollbar
add_scrollbar = Scrollbar(root)
add_scrollbar.grid(row="1", column="9", rowspan="14", sticky=W)
# Enable Verticle Scrolling
add_listbox.configure(yscrollcommand=add_scrollbar.set)
add_scrollbar.configure(command=add_listbox.yview)

# View Button
view_btn = Button(root, text="View Record", bg="blue", fg="white", font="helvetica 10 bold", command=view)
view_btn.grid(row="15", column="1")

# Modify Button
modify_btn = Button(root, text="Modify Record", bg="black", fg="white", font="helvetica 10 bold", command=update)
modify_btn.grid(row="15", column="2")

# Delete Button
delete_btn = Button(root, text="Delete Record", bg="red", fg="white", font="helvetica 10 bold", command=delete)
delete_btn.grid(row="15", column="3")

# Clear Button
clear_btn = Button(root, text="Clear Record", bg="purple", fg="white", font="helvetica 10 bold", command=clear)
clear_btn.grid(row="15", column="4")

# Exit Button
exit_btn = Button(root, text="Exit", bg="blue", fg="maroon", font="helvetica 10 bold", command=exit)
exit_btn.grid(row="15", column="5")

root.mainloop()

# ------------------------------------------------------------------------------------------------------------------ #