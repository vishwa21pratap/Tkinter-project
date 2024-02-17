from tkinter import*
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
import tkinter.messagebox

class atm:
    def __init__(self , root):
        self.root = root
        titlespace=" "
        self.root.title( "EMPLOYEE SYSTEM" )
        self.root.geometry("900x900+400+0")
        self.root.resizable(width =True,height=False)

        MainFrame = Frame(self.root, bd=40,width=1200, height=1200, relief= RIDGE, bg='orange')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame ,bd=7, width=770 ,height=100 ,relief=RIDGE,bg="red")
        TitleFrame.grid(row = 0,column =0)
        TopFrame3 = Frame(MainFrame ,bd=5 ,width=770 ,height=500 ,relief=RIDGE,bg="light green")
        TopFrame3.grid(row = 1,column = 0)

        LeftFrame = Frame(TopFrame3 , bd=5,width=770,height=400 ,padx=2,bg="orange",relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame , bd=5,width=600,height=180 ,padx=12,pady=9,relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3 , bd=5,width=100,height=400 ,padx=2,bg="orange",relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1 , bd=5,width=90,height=300 ,padx=2,pady=2,relief=RIDGE,bg="light blue")
        RightFrame1a.pack(side=TOP)
        #=======================================================================================
        Empid =StringVar()
        Accnumber =StringVar()
        Cusname =StringVar()
        Balance =StringVar()
        Gender =StringVar()
        Open_date =StringVar()
        #=======================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("MYSQL conntion","Confirm If You Want To Exit")
            if iExit > 0:
                root.destroy()
                return
        def Reset():
            self.entEmpid.delete(0,END)
            self.entAccnumber.delete(0,END)
            self.entCusname.delete(0,END)
            self.entBalance.delete(0,END)
            Gender.set("")
            self.entOpen_date.delete(0,END)

        def addData():
            if Empid.get() == ""  or Accnumber.get()== "" or Cusname.get() == "":
                tkinter.messagebox.showerror("Atm Details","Enter correct Details")
            else:
                try:
                    pin=0
                    pin= int(Empid.get())
                    if pin < 1000 :
                        tkinter.messagebox.showerror("Atm Details","Enter correct Details")
                    mysqlCon = mysql.connector.connect(host ="localhost",user="root",password="",database="emp_rec")
                    cursor = mysqlCon.cursor()
                    cursor.execute("insert into emp_rec Values(%s,%s,%s,%s,%s,%s)",(

                    Empid.get(),
                    Accnumber.get(),
                    Cusname.get(),
                    Balance.get(),
                    Gender.get(),
                    Open_date.get()
                    ))
         
                        
                            
                    
                      
                       
                    mysqlCon.commit()
                #   DisplayData()
                    cursor.execute("select *from  emp_rec where Empid='"+str(Empid.get())+"'")
                    result=cursor.fetchall()
                    if len (result)!=0:
                        self.atm_records.delete(* self.atm_records.get_children())
                        for row in result:
                            self.atm_records.insert('',END,values=row)
                            mysqlCon.commit()
                    mysqlCon.close()
                    tkinter.messagebox.showinfo("ATM RECORD","Entered Succesfully")
                except :
                    tkinter.messagebox.showerror("ATM RECORD","Entered Record Already Exist")
                
                
        def DisplayData():
            
                mysqlCon = mysql.connector.connect(host ="localhost",user="root",password="",database="emp_rec")
                cursor =mysqlCon.cursor()
                cursor.execute("select *from  emp_rec")
                result=cursor.fetchall()
                if len (result)!=0:
                    self.atm_records.delete(* self.atm_records.get_children())
                    for row in result:
                        self.atm_records.insert('',END,values=row)
                        mysqlCon.commit()
                mysqlCon.close()
                
             
        def emp_recInfo(ev):
            viewInfo = self.atm_records.focus()
            learnerData = self.atm_records.item(viewInfo)
            row=learnerData['values']
            Empid.set(row[0])
            Accnumber.set(row[1])
            Cusname.set(row[2])
            Balance.set(row[3])
            Gender.set(row[4])
            Open_date.set(row[5])

        def update():
            mysqlCon = mysql.connector.connect(host ="localhost",user="root",password="",database="emp_rec")
            cursor =mysqlCon.cursor()
            cursor.execute("update  emp_rec set Accnumber=%s,Cusname=%s,Balance=%s,Gender=%s,Open_date=%s where Empid=%s",(

            Empid.get(),
            Accnumber.get(),
            Cusname.get(),
            Balance.get(),
            Gender.get(),
            Open_date.get(),
            
            ))
            mysqlCon.commit()
            mysqlCon.close()
            tkinter.messagebox.showinfo("Data entry from","Record updated succesfully")
            
                
        def deleteDB():
            mysqlCon = mysql.connector.connect(host ="localhost",user="root",password="",database="emp_rec")
            cursor =mysqlCon.cursor()
            cursor.execute("delete from emp_rec where Empid='"+Empid.get()+"'")

            mysqlCon.commit()
            DisplayData()
            mysqlCon.close()

            tkinter.messagebox.showinfo("Data entry from","Record succesfully Deleted ")
            Reset()

        
               
            

        def searchDB():
        
            mysqlCon = mysql.connector.connect(host ="localhost",user="root",password="",database="emp_rec")
            cursor =mysqlCon.cursor()
            cursor.execute("select * from emp_rec where Empid='"+Empid.get()+"'")
            row=cursor.fetchone()
            if row!=None:
                Empid.set(row[0])
                Accnumber.set(row[1])
                Cusname.set(row[2])
                Balance.set(row[3])
                Gender.set(row[4])
                Open_date.set(row[5])

            mysqlCon.commit()
            
            if row==None:
                tkinter.messagebox.showinfo("Data entry from","No Such ReCord found")
                Reset()
            mysqlCon.close()
        self.c=0
         
        def setpin():
            if self.c%2==0:
                self.lbl.configure(image=self.image)
                self.entEmpid.configure(show='')
                
            else :
                self.lbl.configure(text='hogya')
                self.entEmpid.configure(show='*')
            self.c+=1
        
        self.image=ImageTk.PhotoImage(file="C:/Users/VISHWA/Pictures/Screenshot 2022-11-29 210714.png") 
        #
        self.lbl=Button(MainFrame,image=self.image,command=setpin,width=160,height=85)
        self.lbl.place(x=0,y=0)

        
        self.iimage=ImageTk.PhotoImage(file="C:/Users/VISHWA/Downloads/image.jpg")
        self.lbl=Button(MainFrame,image=self.iimage,command=setpin,width=195,height=85)
        self.lbl.place(x=650,y=0)
            
            
        #=======================================================================================
        
        self.lbltitle=Label(TitleFrame, font=('arial',40, 'bold'),text="ATM MODULE",bd=7,bg="light blue")
        self.lbltitle.grid(row=0,column=0, padx=132)
        #========================================================================================

        self.lblEmpid=Label(LeftFrame1, font=('arial',12, 'bold'),text="Emp id",bd=7,bg="light blue")
        self.lblEmpid.grid(row=0,column=0, sticky=W, padx=5)
        
        self.entEmpid=Entry(LeftFrame1, font=('arial',12, 'bold'),bd=5,fg="red",bg="light blue",width=44, justify='left',show="*",
                             textvariable=Empid)
        self.entEmpid.grid(row=0,column=1, sticky=W, padx=5)

        self.lblAccnumber=Label(LeftFrame1, font=('arial',12, 'bold'),text="Accnumber",bd=7,bg="light blue")
        self.lblAccnumber.grid(row=1,column=0, sticky=W, padx=5)
        self.entAccnumber=Entry(LeftFrame1, font=('arial',12, 'bold'),bd=5,fg="red",bg="light blue",width=44, justify='left',
                            textvariable=Accnumber)
        self.entAccnumber.grid(row=1,column=1, sticky=W, padx=5)


        self.lblCusname=Label(LeftFrame1, font=('arial',12, 'bold'),text="Cusname",bd=7,bg="light blue")
        self.lblCusname.grid(row=2,column=0, sticky=W, padx=5)
        self.entCusname=Entry(LeftFrame1, font=('arial',12, 'bold'),bd=5,fg="red",bg="light blue",width=44, justify='left',
                              textvariable=Cusname)
        self.entCusname.grid(row=2,column=1, sticky=W, padx=5)

        self.lblBalance=Label(LeftFrame1, font=('arial',12, 'bold'),text="Balance",bd=7,bg="light blue")
        self.lblBalance.grid(row=3,column=0, sticky=W, padx=5)
        self.entBalance=Entry(LeftFrame1, font=('arial',12, 'bold'),bd=5,fg="red",bg="light blue",width=44, justify='left',
                              textvariable=Balance)
        self.entBalance.grid(row=3,column=1)

        self.lblGender=Label(LeftFrame1, font=('arial',12, 'bold'),text="Gender",bd=5,bg="light blue")
        self.lblGender.grid(row=4,column=0, sticky=W, padx=5)
        self.cboGender=ttk.Combobox(LeftFrame1, font=('arial',12, 'bold'),width=44, state='readonly',
                                    textvariable=Gender)
        self.cboGender['values']= (' ', 'FEMALE', 'MALE')
        self.cboGender.current(0)
        self.cboGender.grid(row=4,column=1)


        self.lblOpen_date=Label(LeftFrame1, font=('arial',12, 'bold'),text="Open_date",bd=5,bg="light blue")
        self.lblOpen_date.grid(row=5,column=0, sticky=W, padx=5)
        self.entOpen_date=Entry(LeftFrame1, font=('yellow',12, 'bold'),bd=5,fg="red",bg="light blue",width=44,
                           textvariable=Open_date)
        self.entOpen_date.grid(row=5,column=1, sticky=W, padx=5)
        #=======================================TABLE TREEVIEW==============================================
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

        self.atm_records=ttk.Treeview(LeftFrame, height =12, columns=("Empid","Accnumber","cusname","balance","gender",
        "Open_date"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side= RIGHT , fill=Y)
        scroll_y.config(command=self.atm_records.yview)

        self.atm_records.heading("Empid",text="Empid")
        self.atm_records.heading("Accnumber",text="Accnumber")
        self.atm_records.heading("cusname",text="Cusname")
        self.atm_records.heading("balance",text="Balance")
        self.atm_records.heading("gender",text="Gender")
        self.atm_records.heading("Open_date",text="Open_date")

        self.atm_records['show']='headings'

        self.atm_records.column("Empid", width =100)
        self.atm_records.column("Accnumber",width =100)
        self.atm_records.column("cusname",width =100)
        self.atm_records.column("balance",width =100)
        self.atm_records.column("gender",width =100)
        self.atm_records.column("Open_date",width =100)

        self.atm_records.pack(fill=BOTH, expand=1)
        self.atm_records.bind("<ButtonRelease-1>",emp_recInfo)
        


        #=====================================================================================
        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Add New",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2,command=addData).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text="Display",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2,command=DisplayData).grid(row=1,column=0,padx=1)
        
        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2, command = update).grid(row=2,column=0,padx=1)
        
        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2,command = deleteDB).grid(row=3,column=0,padx=1)
        
        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2,command=searchDB).grid(row=4,column=0,padx=1)
        
        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2, command=Reset).grid(row=5,column=0,padx=1)
        
        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,bg="light blue",
                              width =8,height=2, command=iExit).grid(row=6,column=0,padx=1)

        


        #=====================================================================================
 



        
        
        
          



if __name__ =='__main__':
    root=Tk()
    application = atm(root)
    root.mainloop()

