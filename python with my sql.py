from tkinter import*
import tkinter.messagebox as messagebox
import mysql.connector as mysql
root=Tk()

root.geometry("250x200")
def save():
    name=Text1.get()
    address=Text2.get()
    phone=text3.get()
    if name=='' or address=='' or phone=='':
        messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='akshara')
        cursor=conn.cursor()
        cursor.execute("insert into student values('%s','%s','%s')"%(name,address,phone))
        conn.commit()
        Text1.delete(0,END)
        Text2.delete(0,END)
        text3.delete(0,END)
        messagebox.showinfo("Insert Status","Inserted Successfully")
        cursor.close()
        conn.close()
def show():
    name=Text1.get()
    if name=='':
        messagebox.showinfo("insert status","please enter name")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='akshara')
        cursor=conn.cursor()
        cursor.execute("select * from student where name='%s'"%name)
        rows=cursor.fetchall()

        for row in rows:
            Text2.insert(0,row[1])
            text3.insert(0,row[2])
        cursor.close()
        conn.close()
def delete():
    name=Text1.get()
    if name=='':
        messagebox.showinfo("insert ststus","please enter name")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='akshara')
        cursor=conn.cursor()
        cursor.execute("delete from student where name='%s'"%name)
        conn.commit()
        Text1.delete(0,END)
        Text2.delete(0,END)
        text3.delete(0,END)
        messagebox.showinfo("Delete Status","Deleted Successfully")
        cursor.close()
        conn.close()
def clear():
        Text1.delete(0,END)
        Text2.delete(0,END)
        text3.delete(0,END)
def update():
    name=Text1.get()
    address=Text2.get()
    phone=text3.get()
    if name=='' or address=='' or phone=='':
        messagebox.showinfo("Update Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='akshara')
        cursor=conn.cursor()
        cursor.execute("update student set phone='%s',address='%s' where name='%s'"%(phone,address,name))
        conn.commit()
        Text1.delete(0,END)
        Text2.delete(0,END)
        text3.delete(0,END)
        messagebox.showinfo("Update Status","Updated Successfully")
        cursor.close()
        conn.close()

labl=Label(root,text=" name         :")
labl2=Label(root,text="address      :")
labl3=Label(root,text="phone number :")
Text1=Entry()
Text2=Entry()
text3=Entry()
Btn=Button(root,text="save",command=save)
btn2=Button(root,text="show",command=show)
btn3=Button(root,text="delete",command=delete)
btn4=Button(root,text="clear",command=clear)
btn5=Button(root,text="update",command=update)
labl.place(x=0,y=10)
labl2.place(x=0,y=50)
labl3.place(x=0,y=90)
Text1.place(x=100,y=10)
Text2.place(x=100,y=50)
text3.place(x=100,y=90)
Btn.place(x=25,y=150)
btn2.place(x=60,y=150)
btn3.place(x=100,y=150)
btn4.place(x=145,y=150)
btn5.place(x=185,y=150)
root.mainloop()