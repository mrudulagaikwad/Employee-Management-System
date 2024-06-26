from sqlite3 import Connection
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcombo=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()




        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #LOGO
        img_logo=Image.open('emp_img/logo2.jpg')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)


        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=260,y=0,width=50,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)


        #first image
        img1=Image.open('emp_img/emp2.jpg')
        img1=img1.resize((540,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=510,height=160)
        #second image
        img2=Image.open('emp_img/emp3.jpg')
        img2=img2.resize((540,160))
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=510,y=0,width=510,height=160)

        #third image
        img_3=Image.open('emp_img/emp4.jpg')
        img_3=img_3.resize((540,160))
        self.photo3=ImageTk.PhotoImage(img_3)


        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=530,height=160)

        #MainFrame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=7,y=220,width=1345,height=470)

        #upperFrame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee information ',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=6,width=1320,height=230)

        #labels and entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=18,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial',11,'bold'),width=22)
        txt_Name.grid(row=0,column=3,padx=2,pady=7)

        #lbl_designation
        lbl_designition=Label(upper_frame,font=('arial',12,'bold'),text='Designition1:',bg='white')
        lbl_designition.grid(row=1,column=0,padx=2,sticky=W,pady=7)
        txt_designition=ttk.Entry(upper_frame,textvariable=self.var_designition,font=('arial',11,'bold'),width=22)
        txt_designition.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Email
        lbl_email=Label(upper_frame,font=('arial',12,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,padx=2,sticky=W,pady=7)
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,font=('arial',11,'bold'),width=22)
        txt_email.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #Address
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,padx=2,sticky=W,pady=7)
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,font=('arial',11,'bold'),width=22)
        txt_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #Married
        lbl_married_status=Label(upper_frame,font=('arial',12,'bold'),text='Married Status:',bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,sticky=W,pady=7)
        com_txt_married=ttk.Combobox(upper_frame,state='readonly',textvariable=self.var_married,font=('arial',11,'bold'),width=20)
        com_txt_married['value']=('Married','Unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #dateofbirth
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,sticky=W,pady=7)
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,font=('arial',11,'bold'),width=22)
        txt_dob.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #Doj
        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,sticky=W,pady=7)
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,font=('arial',11,'bold'),width=22)
        txt_doj.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        #Idproof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcombo,font=('arial',12,'bold'),state='readonly',width=14)
        com_txt_proof['value']=("select ID proof","PAN CARD","ADHAR CARD","DRIVING LICENE")
        com_txt_proof.current(0)

        com_txt_proof.grid(row=4,column=0,padx=2,sticky=W,pady=7)
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,font=('arial',11,'bold'),width=22)
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text="Gender:",bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,sticky=W,pady=7)
        com_txt_gender=ttk.Combobox(upper_frame,state='readonly',textvariable=self.var_gender,font=('arial',12,'bold'),width=18)
        com_txt_gender['value']=("Male","Female","other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #Phone
        lbl_phone=Label(upper_frame,font=('arial',12,'bold'),text="Phone No:",bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_phone=ttk.Entry(upper_frame,width=22,textvariable=self.var_phone,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)
        
        #country
        lbl_country=Label(upper_frame,font=('arial',12,'bold'),text="Country:",bg='white')
        lbl_country.grid(row=1,column=4,padx=2,sticky=W,pady=7)
   
        txt_country=ttk.Entry(upper_frame,width=22,textvariable=self.var_country,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)
        
        #Salary
        lbl_ctc=Label(upper_frame,font=('arial',12,'bold'),text="Salary(ctc):",bg='white')
        lbl_ctc.grid(row=2,column=4,padx=2,sticky=W,pady=7)

        txt_ctc=ttk.Entry(upper_frame,width=22,textvariable=self.var_salary,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #image
        img_4=Image.open('emp_img/spemp.jpg')
        img_4=img_4.resize((200,200))
        self.photo4=ImageTk.PhotoImage(img_4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=950,y=0,width=200,height=200)

        #button Frame
        btn_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=1160,y=6,width=148,height=195)

        btn_save=Button(btn_frame,text="SAVE",command=self.add_data,font=('arial',15,'bold'),width=11,fg="darkblue",bg="cyan")
        btn_save.grid(row=0,column=0,padx=1,pady=3)

        btn_update=Button(btn_frame,text="UPDATE",command=self.update_data,font=('arial',15,'bold'),width=11,fg="darkblue",bg="cyan")
        btn_update.grid(row=1,column=0,padx=1,pady=3)

        btn_delete=Button(btn_frame,text="DELETE",command=self.delete_data,font=('arial',15,'bold'),width=11,fg="darkblue",bg="cyan")
        btn_delete.grid(row=2,column=0,padx=1,pady=3)

        btn_clear=Button(btn_frame,text="CLEAR",command=self.reset_data,font=('arial',15,'bold'),width=11,fg="darkblue",bg="cyan")
        btn_clear.grid(row=3,column=0,padx=1,pady=3)

        #downframe
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=238,width=1320,height=220)

        #searchframe
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white', text='Search Employee information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=3,y=0,width=1310,height=55)

        search_by=Label(search_frame,font=('arial',11,'bold'),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,state="readonly",textvariable=self.var_com_search,font=('arial',12,'bold'),width=18)
        com_txt_search['value']=("Select Option","Phone")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,width=22,textvariable=self.var_search,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",command=self.search_data,font=('arial',11,'bold'),width=14,fg="darkblue",bg="cyan")
        btn_search.grid(row=0,column=3,padx=4)

        btn_showAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('arial',11,'bold'),width=14,fg="darkblue",bg="cyan")
        btn_showAll.grid(row=0,column=4,padx=4)

        behappy=Label(search_frame,bg='white', text='BE HAPPY !!!',font=('times new roman',30,'bold'),fg='red')
        behappy.place(x=800,y=0,width=550,height=30)

        img_5=Image.open('emp_img/smile2.jpg')
        img_5=img_5.resize((50,70))
        self.photo5=ImageTk.PhotoImage(img_5)

        self.img_5=Label(search_frame,image=self.photo5)
        self.img_5.place(x=880,y=0,width=50,height=40)

        #----------------------------------------------------Employeee table----------------------------------------------------------------


        #table frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1313,height=140)
        

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcombo","idproof","gender","phone","country","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designition1')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married_status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcombo',text='ID_Proof_type')
        self.employee_table.heading('idproof',text='ID_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        

        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcombo',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #**************************************8****************FUNCTION DECLARATIONS************************************************
          
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields Are Required...')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='System@2024',database='mydata')
                my_cursor=conn.cursor()
                
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  (        
                                        self.var_dep.get(),
                                        self.var_name.get(),
                                        self.var_designition.get(),
                                        self.var_email.get(),
                                        self.var_address.get(),
                                        self.var_married.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_idproofcombo.get(),
                                        self.var_idproof.get(),
                                        self.var_gender.get(),
                                        self.var_phone.get(),
                                        self.var_country.get(),
                                        self.var_salary.get()
                                         
                                         
                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess','Employee has Been Added..!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


    #fetch data
    def fetch_data(self):
       conn=mysql.connector.connect(host='localhost',username='root',password='System@2024',database='mydata')
       my_cursor=conn.cursor()
       my_cursor.execute('select * from employee1')
       data=my_cursor.fetchall()
       if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
               self.employee_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #Get Cursor
            
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcombo.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
    
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            
            messagebox.showerror('Error','All Fields Are Required...')
        else:
            try:
                update=messagebox.askyesno('update','are you sure update this employee data')
                if update>0:
                     conn=mysql.connector.connect(host='localhost',username='root',password='System@2024',database='mydata')
                     my_cursor=conn.cursor()
                     my_cursor.execute('update employee1 set Department=%s,Name=%s,Designition1=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,ID_Proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where ID_Proof=%s',(
                                        self.var_dep.get(),
                                        self.var_name.get(),
                                        self.var_designition.get(),
                                        self.var_email.get(),
                                        self.var_address.get(),
                                        self.var_married.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_idproofcombo.get(),
                                        self.var_gender.get(),
                                        self.var_phone.get(),
                                        self.var_country.get(),
                                        self.var_salary.get(),
                                        self.var_idproof.get()

                     ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Updated SuccessFully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required....')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure Delete these employee....!',parent=self.root) 
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='System@2024',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where ID_Proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Deleted SuccessFully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #clear
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcombo.set("Select Id Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")



    #search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','PLEASE select option....')    
        else:
            try:
                 conn=mysql.connector.connect(host='localhost',username='root',password='System@2024',database='mydata')
                 my_cursor=conn.cursor()
                 my_cursor.execute('Select * from employee1 where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                     self.employee_table.delete(*self.employee_table.get_children())
                     for i in rows:
                         self.employee_table.insert("",END,values=i)
                 conn.commit()
                 conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    #

                    
                
    



      

        






    








if __name__=="__main__": 
     root=Tk()
     obj=Employee(root)
     root.mainloop()

