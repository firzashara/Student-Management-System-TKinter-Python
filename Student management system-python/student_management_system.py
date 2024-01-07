from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Student:
    def __init__(self,main):
        self.main=main
        
        self.T_Frame=Frame(self.main,height=50,width=1200,background="grey",bd=2,relief=GROOVE)
        self.T_Frame.pack()
        self.title=Label(self.T_Frame,text="Student Management System",font="cambria 20 bold",width=1200,bg="mediumvioletred",fg="white")
        self.title.pack()
        
        self.Frame_1=Frame(self.main,height=580,width=400,bd=2,relief=GROOVE,bg="lightgrey")
        self.Frame_1.pack(side="left")
        self.Frame_1.pack_propagate(0)
        
        Label(self.Frame_1,text="Student Details:",background="lightgrey",font="arial 12 bold underline").place(x=20,y=20)
        
        self.roll_num=Label(self.Frame_1,text="Roll Number",background="lightgrey",font="arial 11 bold")
        self.roll_num.place(x=40,y=60)
        self.roll_entry=Entry(self.Frame_1,width=40)
        self.roll_entry.place(x=140,y=60)
        
        self.name=Label(self.Frame_1,text="Name",background="lightgrey",font="arial 11 bold")
        self.name.place(x=40,y=100)
        self.name_entry=Entry(self.Frame_1,width=40)
        self.name_entry.place(x=140,y=100)
        
        self.grade=Label(self.Frame_1,text="Grade",background="lightgrey",font="arial 11 bold")
        self.grade.place(x=40,y=140)
        self.grade_entry=Entry(self.Frame_1,width=40)
        self.grade_entry.place(x=140,y=140)
        
        self.gender=Label(self.Frame_1,text="Gender",background="lightgrey",font="arial 11 bold")
        self.gender.place(x=40,y=180)
        self.gender_entry=Entry(self.Frame_1,width=40)
        self.gender_entry.place(x=140,y=180)
        
        self.DOB=Label(self.Frame_1,text="DOB",background="lightgrey",font="arial 11 bold")
        self.DOB.place(x=40,y=220)
        self.DOB_entry=Entry(self.Frame_1,width=40)
        self.DOB_entry.place(x=140,y=220)
        
        self.GPA=Label(self.Frame_1,text="GPA",background="lightgrey",font="arial 11 bold")
        self.GPA.place(x=40,y=260)
        self.GPA_entry=Entry(self.Frame_1,width=40)
        self.GPA_entry.place(x=140,y=260)
        
        self.Button_Frame=Frame(self.Frame_1,height=250,width=250,relief=GROOVE,bd=2,background="grey")
        self.Button_Frame.place(x=80,y=300)
        
        self.Add=Button(self.Button_Frame,text="ADD",width=25,font="arial 11 bold",command=self.Add)
        self.Add.pack()
        
        self.Update=Button(self.Button_Frame,text="UPDATE",width=25,font="arial 11 bold",command=self.Update )
        self.Update.pack()
        
        self.Delete=Button(self.Button_Frame,text="DELETE",width=25,font="arial 11 bold",command=self.Delete)
        self.Delete.pack()
        
        self.Clear=Button(self.Button_Frame,text="CLEAR",width=25,font="arial 11 bold",command=self.Clear)
        self.Clear.pack()
        
        
        
        
        self.Frame_2=Frame(self.main,height=580,width=800,bd=2,relief=GROOVE,bg="white")
        self.Frame_2.pack(side="right")
        
        self.tree=ttk.Treeview(self.Frame_2,columns=("c1","c2","c3","c4","c5","c6"),show='headings',height=25)
        
        self.tree.column("#1",anchor=CENTER,width=90)
        self.tree.heading("#1",text="Roll Number")
        
        self.tree.column("#2",anchor=CENTER,width=100)
        self.tree.heading("#2",text="Name")
        
        self.tree.column("#3",anchor=CENTER,width=120)
        self.tree.heading("#3",text="Grade")
        
        self.tree.column("#4",anchor=CENTER,width=140)
        self.tree.heading("#4",text="Gender")
        
        self.tree.column("#5",anchor=CENTER,width=160)
        self.tree.heading("#5",text="DOB")
        
        self.tree.column("#6",anchor=CENTER,width=180)
        self.tree.heading("#6",text="GPA")
        
        
        
        
        
        self.tree.insert("",index=0,values=(101,"Edward","A","Male","12-01-1998",3.7899))
        self.tree.insert("",index=0,values=(202,"Jane","C","Female","09-05-2000",2.0989))
        self.tree.insert("",index=0,values=(303,"Leeza","A","Female","23-01-2001",3.5678))
        self.tree.insert("",index=0,values=(404,"Tessa","B","Female","02-01-1998",3.0045))
        self.tree.insert("",index=0,values=(505,"Hardin","B","Male","31-01-1999",2.9890))
        
        self.tree.pack()
        
    def Add(self):
        messagebox.showinfo("Success","Data added successfully")
        roll_n=self.roll_entry.get()
        name=self.name_entry.get()
        grade=self.grade_entry.get()
        gender=self.gender_entry.get()
        dob=self.DOB_entry.get()
        gpa=self.GPA_entry.get()
        self.tree.insert("",index=0,values=(roll_n,name,grade,gender,dob,gpa))
        
    def Delete(self):
        messagebox.showinfo("Success","Data deleted successfully")
        item=self.tree.selection()[0]
        self.tree.delete(item)
        
    def Update(self):
        messagebox.showinfo("Success","Data updated successfully")
        roll_n=self.roll_entry.get()
        name=self.name_entry.get()
        grade=self.grade_entry.get()
        gender=self.gender_entry.get()
        dob=self.DOB_entry.get()
        gpa=self.GPA_entry.get()
        item=self.tree.selection()[0]
        self.tree.item(item,values=(roll_n,name,grade,gender,dob,gpa))
        
    def Clear(self):
        messagebox.showinfo("Success","Data cleared successfully")
        self.roll_entry.delete(0,END)
        self.name_entry.delete(0,END)
        self.grade_entry.delete(0,END)
        self.gender_entry.delete(0,END)
        self.DOB_entry.delete(0,END)
        self.GPA_entry.delete(0,END)
        
 

main=Tk()
main.title("Student Management System")
main.resizable(False,False)
main.geometry("1200x600")

Student(main)
main.mainloop()


