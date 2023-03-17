#!/usr/bin/env python
# coding: utf-8

# # Project-1
# # Employee Management System
# 

# # #Establish a database connection

# ### we dont use django, flask here 

# In[16]:


# create a database and a table


# In[ ]:


import mysql.connector
conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost') # connection object
qur='create database myproject'                                                    # created a database
mycur=conn.cursor()                                                                # cursor method 
mycur.execute(qur)                                                                 # execute method 
mycur.close()                                                                      # close method - cur 
conn.close()                                                                       # close method - conn

'''
import mysql.connector
conn=mysql.connector.connect(user='root',password='Python@123',host='localhost')
qur='create database myproject'
mycur=conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()'''


# In[ ]:


import mysql.connector
conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
qur='create table emp1(name varchar(20),mobno Varchar(20),dept varchar(20),salary varchar(20))'         # create table query
mycur=conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()


# # # interface

# ### tkinter
This is a standard Python library used for creating GUI (Graphical User Interface) applications. 
It provides a set of widgets (buttons, labels, textboxes, etc.) that can be used to build interactive desktop applications.
# ### messagebox
This module provides functions for displaying message boxes in Tkinter applications. 
It allows you to show simple messages, warning messages, error messages, and ask for confirmation from the user.
# ### ttk
This module provides an improved set of widgets over the standard Tkinter widgets.
It includes widgets such as Combobox, Progressbar, Notebook, etc.
Just like CSS is used to style an HTML element, we use tkinter.ttk to style tkinter widgets. 
# ### PIL 
Python Imaging Library
This module provides classes for working with images in Python.
It allows you to open, manipulate, and save images in various formats.

# ### ImageTk
it is a submodule of PIL that provides a way to display images in Tkinter applications.
# In[27]:


import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

win=Tk()
win.title('EMPLOYEE MANAGEMENT SYSTEM')
win.minsize(width=800,height=600)
win.configure(bg='mint cream')


# All funtions are defined here 

# function 1 - show() 

def show():
    conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
    qur='select * from emp1'
    mycur=conn.cursor()
    mycur.execute(qur)
    list1=mycur.fetchall()  # fetchallmethod is used to fetch all the rows in the result set returned by the query
    for i in list1:
        treev.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    mycur.close()
    conn.close()
    
# function 2 - add()

def add():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if name=='' or mobno=='' or dept=='' or salary=='':
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
        qur='INSERT INTO emp1(name,mobno,dept,salary) VALUES ("%s","%s","%s","%s")'%(name,mobno,dept,salary)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','data is added Successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
        
# function 3 - salary()

def salary():
    win.destroy()
    root=Tk()
    root.title('EMPLOYEE MANAGEMENT SYSTEM')
    root.minsize(width=800,height=600)
    root.configure(bg='lavender blush')
# define the function in salary
    def disp():
        name=var3.get()
        conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
        qur='select salary from emp1 where name="%s"'%(name)
        mycur=conn.cursor()
        mycur.execute(qur)
        result=mycur.fetchone()
        l12.configure(text=result[0]+' Rs')
        mycur.close()
        conn.close()
    
# label for salary 
    l11=Label(root,text='Name of Employee',width=20,
              bd=5,relief='ridge',font=('times new roman',14,'bold'))
    l11.place(x=100,y=40)
    
    l12=Label(root,text='Salary is here',width=20,height=4,
              bd=5,relief='ridge',font=('times new roman',14,'bold'))
    l12.place(x=100,y=160)
# entry for salary
    var3=StringVar()
    e11=Entry(root,width=40,textvariable=var3,
              bd=5,relief='ridge',font=('times new roman',14,'bold'))
    e11.place(x=350,y=40)
    
# button for salary 
    b11=Button(root,text='SHOW SALARY',width=20,command=disp)
    b11.place(x=350,y=80)
    
    
    root.mainloop()

def delete():
    name=var1.get() 
    if name=='':
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
        qur='DELETE FROM emp1 WHERE name="%s"'%(name)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is Deleted Successfully')
        var1.set('')

def select():
    name=var1.get() 
    if name=='':
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
        qur='select * from emp1 where name="%s"'%(name)
        mycur=conn.cursor()
        mycur.execute(qur)
        result=mycur.fetchone()
        e1.insert(0,result[0])
        e2.insert(0,result[1])
        e3.insert(0,result[2])
        e4.insert(0,result[3])
        mycur.close()
        conn.close()
        


def update():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if name=='' or mobno=='' or dept=='' or salary=='':
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Iamvibhor12!',host='localhost',database='myproject')
        qur='UPDATE emp1 SET mobno="%s",dept="%s",salary="%s" WHERE name="%s"'%(mobno,dept,salary,name)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is updated Successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')

def clear():
    treev.delete(*treev.get_children())

# main label

l0=Label(win,text='EMPLOYEE MANAGEMENT SYSTEM',bd=5,relief='ridge',bg='white',
        fg='black',width=35,font=('times new roman',16,'bold'))
l0.place(x=268,y=40)

# name label and entry 

# -label1
l1=Label(win,text='name',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l1.place(x=190,y=100)
# -entry1
n1=StringVar()
e1=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=n1,font=('times new roman',12,'bold'))
e1.place(x=385,y=100)




# -mob no label and entry

# -label2
l2=Label(win,text='mobno',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l2.place(x=190,y=140)
# -entry2
m1=StringVar()
e2=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=m1,font=('times new roman',12,'bold'))
e2.place(x=385,y=140)

# -dept label name and entry

# -label3
l3=Label(win,text='dept',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l3.place(x=190,y=180)
# -entry2
d1=StringVar()
e3=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=d1,font=('times new roman',12,'bold'))
e3.place(x=385,y=180)

# -salary label name and entry

# -label4
l4=Label(win,text='salary',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l4.place(x=190,y=220)
# -entry4
s1=StringVar()
e4=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=s1,font=('times new roman',12,'bold'))
e4.place(x=385,y=220)


# add show exit salary buttons
b1=Button(win,text='SHOW',command=show,width=20)
b1.place(x=200,y=320)

b2=Button(win,text='ADD',command=add,width=20)
b2.place(x=500,y=320)

b3=Button(win,text='exit',command=win.destroy,width=20)
b3.place(x=200,y=360)

b4=Button(win,text='salary',command=salary,width=20)
b4.place(x=500,y=360)

# "delete" label entry button

# - label5
l5=Label(win,text='Delete By Name >>',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l5.place(x=190,y=400)
# -entry5
var1=StringVar()
e5=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=var1,font=('times new roman',12,'bold'))
e5.place(x=385,y=400)
# -button
b5=Button(win,text='DELETE',command=delete,width=20)
b5.place(x=200,y=440)

# "update" label,entry,select and update button

# - label6
l6=Label(win,text='Update By Name >>',bd=5,relief='ridge',bg='white',
        fg='black',width=20,font=('times new roman',12,'bold'))
l6.place(x=190,y=480)
# -entry6
var2=StringVar()
e6=Entry(win,bd=5,relief='ridge',bg='white',fg='black',width=40,
        textvariable=var2,font=('times new roman',12,'bold'))
e6.place(x=385,y=480)
# -button
b6=Button(win,text='SELECT',command=delete,width=20)
b6.place(x=200,y=520)
b7=Button(win,text='UPDATE',command=update,width=20)
b7.place(x=350,y=520)

# creating the triview

treev=ttk.Treeview(win,height=20)
treev.place(x=800,y=100,width=550)

# creating columns in treeview

treev["columns"] = ("1","2","3","4")
treev['show'] = 'headings'

# width for the columns  

treev.column("1",width= 90, anchor ='c')
treev.column("2",width= 90, anchor ='se')
treev.column("3",width= 90, anchor ='se')
treev.column("4",width= 90, anchor ='se')

# heading for treeview

treev.heading("1", text = "Name")
treev.heading("2", text = "mobile no")
treev.heading("3", text = "dept")
treev.heading("4", text = "salary")

# clear button
clearbtn=Button(win,text='Clear',width=20,command=clear)
clearbtn.place(x=1000,y=560)



win.mainloop()


# In[ ]:




