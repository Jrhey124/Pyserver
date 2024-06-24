# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:14:57 2024

@author: Admin
"""

from tkinter import *
import random


import mysql.connector
mydb = mysql.connector.connect(
    host="bjtwsgkom4qxz55lr2tr-mysql.services.clever-cloud.com",
    user="uqnextu4zjufudjj",
    password="fxpqZmAg4Jkx6aCXGlHw",
    database="bjtwsgkom4qxz55lr2tr"
)


mycursor = mydb.cursor()
def insert():
    if entry2.get()== "" or entry3.get()=="" or entry4.get() =="":
        messagebox.showwarning("error", "Fill up the requirements")
        entry1.focus_set()
    else:
        if entry1.get() == "":
            entry1.insert(0, "NULL")
        sql = "INSERT INTO tblstudents VALUES (" + entry1.get() + ",'" + entry2.get() + "','" + entry3.get() + "'," + entry4.get() + ",'" + Yearlevel.get() + "')"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        
        messagebox.showinfo("showinfo", "Records Inserted")
        ClearEntries()
        #btn1["state"]="disable"


#
def search(): # Create new Widget to show the Table students
    table = Tk()
    table.title("Table Students")
    table.geometry("450x550")
    
    if entry1.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "":
        messagebox.showwarning("error", "Please Provide Values")
        entry1.focus_set() ## ?????
    else: 
        sql = "SELECT * FROM tblstudents WHERE "
    
        if entry1.get() != "":
            sql += "StudentID = " + entry1.get() + " AND "
        if entry2.get() != "":
            sql += "FirstName = '" + entry2.get() + "' AND "
        if entry3.get() != "":
            sql += "LastName = '" + entry3.get() + "' AND "
        if entry4.get() != "":
            sql += "Age = " + entry4.get() + " AND "
        sql += "1"
        
    print(sql)
    mycursor.execute(sql)
    
    values = mycursor.fetchall()
    w, x, y, z = "(StudentID)\n", "(Firstname)\n", "(Lastname)\n", "(Age)\n"
    
    for i in values:
        w += str(i[0])+'\n'
        x += str(i[1])+'\n'
        y += str(i[2])+'\n'
        z += str(i[3])+'\n'
     
    lbl1=Label(table,text=w,font="Arial 8 bold", fg="light green")
    lbl2=Label(table,text=x,font="Arial 8 bold", fg="light blue")
    lbl3=Label(table,text=y,font="Arial 8 bold", fg="light green")
    lbl4=Label(table,text=z,font="Arial 8 bold", fg="light blue")
        
        
    lbl1.place(x=25,y=10)
    lbl2.place(x=125,y=10)
    lbl3.place(x=225,y=10)
    lbl4.place(x=325,y=10)

def ClearEntries():
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry1.focus_set()

root=Tk()
root.title("Place sample")
root.geometry("500x400")
root.resizable(width=False,height=False)

lbl1=Label(root,text="StudentID:",font="Arial 20 bold")
lbl2=Label(root,text="First Name:",font="Arial 20 bold")
lbl3=Label(root,text="Last Name:",font="Arial 20 bold")
lbl4=Label(root,text="Age:",font="Arial 20 bold")
lbl5=Label(root,text="YearLevel:",font="Arial 20 bold")

entry1=Entry(root,font="Arial 20 bold", fg='grey')
entry2=Entry(root,font="Arial 20 bold")
entry3=Entry(root,font="Arial 20 bold")
entry4=Entry(root,font="Arial 20 bold")

choices = ["Freshmen", "Sophomore", "Junior", "Senior"]
Yearlevel = StringVar(root, value="Freshmen")
choice_box = OptionMenu(root, Yearlevel, *choices)

btn1=Button(root,text="Insert",font="Arial 20 bold", fg='brown',command=insert)
btn2=Button(root,text="Search",font="Arial 20 bold", fg='brown',command=search)

showvalue=StringVar()

lbl1.place(x=22,y=25)
lbl2.place(x=22,y=65)
lbl3.place(x=22,y=105)
lbl4.place(x=22,y=185)
lbl5.place(x=22,y=145)

entry1.place(x=190,y=25,width=150)
entry2.place(x=190,y=65,width=150)
entry3.place(x=190,y=105,width=150)
entry4.place(x=100,y=185, width=70)


choice_box.config(font=("Arial", 15))
choice_box.pack(anchor=W , padx=170, pady=145)

btn1.place(x=22,y=230,width=150)
btn2.place(x=22,y=290,width=150)

root.mainloop()

