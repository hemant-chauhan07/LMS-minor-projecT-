from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
import tkinter
import mysql.connector as a
import importlib 
newbookwindow = importlib.import_module("add_book")
detailswindow = importlib.import_module("book_details")


class LibraryManagementSystem:
    def __init__(self, root):
        # main frame
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM:")
        self.root.geometry("1500x800")   
        self.root.resizable(False, False)


    
        #variables




        
        self.member_var = StringVar()
        self.prn_no_var = StringVar()
        self.id_no_var = StringVar()
        self.name_var = StringVar()
        self.address_var = StringVar()
        self.post_code_var = StringVar()
        self.contact_no_var = StringVar()
        self.book_id_var = StringVar()
        self.book_name_var = StringVar()
        self.issue_date_var = StringVar()
        self.late_fine_var = StringVar()
        

        
        

        # top frame 
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM",
                         bg="powder blue", fg="green", bd=10, relief=RIDGE, font="arial 30 bold",
                         padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=8, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=100, width=1500, height=400)

        # declaration of left frame 
        left_frame = LabelFrame(frame, text="Library Member Information", 
                               bg="powder blue", fg="green", bd=10, relief=RIDGE, 
                               font="arial 12 bold")
        left_frame.place(x=0, y=5, width=730, height=350)
        

        # declaration of of member Label
        lblmember = Label(left_frame, bg="powder blue", text="Member Type :", font="arial 12 bold", padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W) 
        # declaration of memeber Combobox
        member_combo_box = ttk.Combobox(left_frame, font="times 11 bold", textvariable=self.member_var, width=27, state="readonly")
        member_combo_box["value"]= ("Student", "Faculty", "Staff") 
        member_combo_box.grid(row=0, column=1)


        # declaration of prn number Label
        lbl_PRN_no = Label(left_frame, bg= "powder blue", text= "PRN No :", font="arial 12 bold", padx=2, pady=6 )
        lbl_PRN_no.grid(row=1, column=0, sticky=W)
        # declaration of prn number entrybox
        txt_PRN_NO = Entry(left_frame, font="times 11", textvariable=self.prn_no_var, width=33)
        txt_PRN_NO.grid(row=1, column=1)


        # declaration of id no Label
        lbl_id_no = Label(left_frame, bg= "powder blue", text= "ID No :", font="arial 12 bold", padx=2, pady=6 )
        lbl_id_no.grid(row=2, column=0, sticky=W)
        # declaration of id no entrybox
        txt_id_NO = Entry(left_frame, font="times 11", textvariable=self.id_no_var, width=33)
        txt_id_NO.grid(row=2, column=1)


        # declaration of name Label
        lbl_firstname = Label(left_frame, bg= "powder blue", text= "Name :", font="arial 12 bold", padx=2, pady=6 )
        lbl_firstname.grid(row=3, column=0, sticky=W)
        # declaration of first name entrybox
        txt_firstname = Entry(left_frame, font="times 11",textvariable=self.name_var, width=33)
        txt_firstname.grid(row=3, column=1)


        # declaration of address Label
        lbl_address = Label(left_frame, bg= "powder blue", text= "Address :", font="arial 12 bold", padx=2, pady=6 )
        lbl_address.grid(row=4, column=0, sticky=W)
        # declaration of address entrybox
        txt_adress = Entry(left_frame, font="times 11", textvariable=self.address_var, width=33)
        txt_adress.grid(row=4, column=1)


        # declaration of post code Label
        lbl_postcode = Label(left_frame, bg= "powder blue", text= "Post Code :", font="arial 12 bold", padx=2, pady=6 )
        lbl_postcode.grid(row=5, column=0, sticky=W)
        # declaration of post code entrybox
        txt_postcode = Entry(left_frame, font="times 11", textvariable=self.post_code_var, width=33)
        txt_postcode.grid(row=5, column=1)


        # declaration of contact no Label
        lbl_contact_no = Label(left_frame, bg= "powder blue", text= "Contact No :", font="arial 12 bold", padx=2, pady=6 )
        lbl_contact_no.grid(row=6, column=0, sticky=W)
        # declaration of contact no entrybox
        txt_contact_no = Entry(left_frame, font="times 11", textvariable=self.contact_no_var, width=33)
        txt_contact_no.grid(row=6, column=1)


        # declaration of book name Label
        lbl_book_name = Label(left_frame, bg= "powder blue", text= "Book Name :", font="arial 12 bold", padx=2, pady=6 )
        lbl_book_name.grid(row=0, column=4, sticky=W)
        # declaration of book name combobox
        book_name_combobox = ttk.Combobox(left_frame, font="times 11 bold", textvariable=self.book_name_var, width=27, state="readonly")
        #code to fetch data from database to combobox
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        books = cur.execute("select * from books")
        books = cur.fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]))
        book_name_combobox["value"] = book_list
        book_name_combobox.grid(row=0,column=5)
        

       
        
        # declaration of book id Label
        lbl_book_id = Label(left_frame, bg= "powder blue", text= "Book ID :", font="arial 12 bold", padx=2, pady=6 )
        lbl_book_id.grid(row=1, column=4, sticky=W)
        # declaration of book id entrybox
        txt_book_id = Entry(left_frame, font="times 11", textvariable=self.book_id_var, width=33)
        txt_book_id.grid(row=1, column=5)



        # declaration of date borrowed Label
        lbl_issue_date = Label(left_frame, bg= "powder blue", text= "Issue Date :", font="arial 12 bold", padx=2, pady=6 )
        lbl_issue_date.grid(row=2, column=4, sticky=W)
        # declaration of date borrowed entrybox
        txt_issue_date = Entry(left_frame, font="times 11", textvariable=self.issue_date_var, width=33)
        txt_issue_date.grid(row=2, column=5)


        # declaration of late fine Label
        lbl_latefee = Label(left_frame, bg= "powder blue", text= "Late Fee :", font="arial 12 bold", padx=2, pady=6 )
        lbl_latefee.grid(row=3, column=4, sticky=W)
        # declaration of late fine entrybox
        txt_latefee = Entry(left_frame, font="times 11", textvariable=self.late_fine_var, width=33)
        txt_latefee.grid(row=3, column=5)


       



        # declaration of right frame 
        right_frame = LabelFrame(frame, text="Book Details", 
                               bg="powder blue", fg="green", bd=10, relief=RIDGE, 
                               font="arial 12 bold")
        right_frame.place(x=780, y=5, width=650, height=350)

        # declaration of text box
        self.txt_box = Text(right_frame, font="arial 12 bold", width=32, height=16)
        self.txt_box.grid(row=0, column=2, padx=45, pady=6)
        #declaration of scroll bar
        listScrollbar = Scrollbar(right_frame)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        #declaration of listbox for book list
        self.listBox = Listbox(right_frame, font="arial 10 bold", width=30, height=16)
        self.listBox.grid(row=0, column=0, padx=10)
        listScrollbar.config(command=self.listBox.yview)
        #code to fetch data from database to listbox
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        books = cur.execute("select b_name from books")
        books = cur.fetchall()

        for items in books:
            self.listBox.insert(END, items)
        



        #  frame for buttons
        btn_frame = Frame(self.root, bd=8, relief=RIDGE, padx=20, bg="powder blue")
        btn_frame.place(x=0, y=500, width=1500, height=70)

        book_details_btn = Button(btn_frame, text="Book Details", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.book_details)
        book_details_btn.grid(row=0, column=0, pady=8)

         #declaration of all the buttons

        #add book button
        add_book_btn = Button(btn_frame, text="ADD Book", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.new_book)
        add_book_btn.grid(row=0, column=1, pady=8)
        
        #add data button
        add_data_btn = Button(btn_frame, text="ADD Data", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.add_data)
        add_data_btn.grid(row=0, column=2, pady=8)
        
        #show data button
        showdata_btn = Button(btn_frame, text="Show Data", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.show_data)
        showdata_btn.grid(row=0, column=3, pady=8)
       
        #update data button
        update_btn = Button(btn_frame, text="Update", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.update)
        update_btn.grid(row=0, column=4, pady=8)
        
        #delete button
        delete_btn = Button(btn_frame, text="Delete", font="arial 10 bold", width=20, bg="grey", fg="white", command=self.delete_data)
        delete_btn.grid(row=0, column=5, pady=8)
        
        #reset button
        reset_btn = Button(btn_frame, text="Reset", font="arial 10 bold", width=25, bg="grey", fg="white", command=self.reset)
        reset_btn.grid(row=0, column=6, pady=8)
        
        #exit button
        exit_btn = Button(btn_frame, text="Exit", font="arial 10 bold", width=25, bg="grey", fg="white", command=self.exit)
        exit_btn.grid(row=0, column=7, pady=8)
       
        
        #  frame  for database information
        info_frame = Frame(self.root, bd=8, relief=RIDGE, padx=20, bg="powder blue")
        info_frame.place(x=0, y=570, width=1500, height=195)

        xscroll = ttk.Scrollbar(info_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(info_frame, orient=VERTICAL)

        # #declaration of table to  store data from the database
        self.data_table = ttk.Treeview(info_frame, columns=("member type", "prn number", "id number", "name",
                                      "address", "post code", "contact number", "book id", "book name", "issue date", "late fee" ),
                                       xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        #vertical scroll bar for the data table  
        xscroll.pack(side=BOTTOM, fill=X)
        xscroll.config(command=self.data_table.xview)
        
        #horizontal scroll bar for the data table
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.data_table.yview)


        

        #declaration the columns for the data table
        self.data_table.heading("member type", text="Member Type")
        self.data_table.heading("prn number", text="PRN Number")
        self.data_table.heading("id number", text="ID Number")
        self.data_table.heading("name", text="Name")
        self.data_table.heading("address", text="Adress")
        self.data_table.heading("post code", text="Post Code")
        self.data_table.heading("contact number", text="Contact Number")
        self.data_table.heading("book id", text="Book ID")
        self.data_table.heading("book name", text="Book Name")
        self.data_table.heading("issue date", text="Issue Date")
        self.data_table.heading("late fee", text="Panulty Fee")
        
        self.data_table["show"] = "headings"
        self.data_table.pack(fill=BOTH, expand=1)
        

        #declaration of the widht of the columns of the data table
        self.data_table.column("member type", width=100)
        self.data_table.column("prn number", width=100)
        self.data_table.column("id number", width=100)
        self.data_table.column("name", width=100)
        self.data_table.column("address", width=100)
        self.data_table.column("post code", width=100)
        self.data_table.column("contact number", width=100)
        self.data_table.column("book id", width=100)
        self.data_table.column("book name", width=100)
        self.data_table.column("issue date", width=100)
        self.data_table.column("late fee", width=100)

        self.fetch_data()
        self.data_table.bind("<ButtonRelease-1>", self.get_cursor)
    
    #function called for add book button stored in newbook window imported from the add_book file
    def new_book(self):
        add = newbookwindow.StoreBook()
    
    #function called for book details stored in details window imported from book_details file
    def book_details(self):
        add = detailswindow.StoreDetails()


    #function for add data button
    def add_data(self):
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        member =  self.member_var.get()
        prn = self.prn_no_var.get()
        id = self.id_no_var.get()
        name = self.name_var.get()
        addr =  self.address_var.get()
        pc = self.post_code_var.get()
        cn = self.contact_no_var.get()
        b_id = self.book_id_var.get()
        b_name = self.book_name_var.get()
        date =  self.issue_date_var.get()
        lf = self.late_fine_var.get()

        tup1 = (member, prn, id, name, addr, pc, cn, b_id, b_name, date, lf)


        if(prn != ""):
            try:
                query = "insert into project_lms.data(member, prn_number, id_number, name, address, post_code, contact_number, book_id, book_name, issue_date, late_fine) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(query, tup1)
                con.commit()
                messagebox.showinfo("Library Management System","Data Entered Successfully!", icon="info")
            
            except:
                messagebox.showerror("Library Management System","Something Went Wrong!!", icon="error")

        
        else:
            messagebox.showwarning("Library Management System","All Fields Are Mandatory", icon="warning")
        
        self.fetch_data()
        con.close()
        

    #function for update data button
    def update(self):
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        cur.execute("update data set member = %s, id_number = %s, name = %s, address = %s, post_code = %s, contact_number = %s, book_id = %s, book_name = %s, issue_date = %s, late_fine = %s where prn_number = %s",
                                                                    (self.member_var.get(), 
                                                                    self.id_no_var.get(), 
                                                                    self.name_var.get(), 
                                                                    self.address_var.get(), 
                                                                    self.post_code_var.get(),
                                                                    self.contact_no_var.get(), 
                                                                    self.book_id_var.get(), 
                                                                    self.book_name_var.get(), 
                                                                    self.issue_date_var.get(), 
                                                                    self.late_fine_var.get(),
                                                                    self.prn_no_var.get()
                                                                    ))
        con.commit()
        self.fetch_data()
        self.reset()
        con.close()

        messagebox.showinfo("Library Management Systerm","Data Has Been Updated", icon= "info")

                                        
        


    #function for fetching data on real time
    def fetch_data(self):
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        query = "select * from data"
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows)!= 0:
            self.data_table.delete(*self.data_table.get_children())
            for i in rows:
                self.data_table.insert("", END, values=i)
            con.commit()
        con.close()

    #cursor for showing data in the data table
    def get_cursor(self, event=""):
        cur_row = self.data_table.focus()
        content = self.data_table.item(cur_row)
        row = content['values']


        self.member_var.set(row[0])
        self.prn_no_var.set(row[1])
        self.id_no_var.set(row[2])
        self.name_var.set(row[3])
        self.address_var.set(row[4])
        self.post_code_var.set(row[5])
        self.contact_no_var.set(row[6])
        self.book_id_var.set(row[7])
        self.book_name_var.set(row[8])
        self.issue_date_var.set(row[9])
        self.late_fine_var.set(row[10])
    
    #function for show data button
    def show_data(self):
        self.txt_box.insert(END, "Member Type:\t" + self.member_var.get() + "\n")
        self.txt_box.insert(END, "PRN NO:\t" + self.prn_no_var.get() + "\n")
        self.txt_box.insert(END, "ID No:\t" + self.id_no_var.get() + "\n")
        self.txt_box.insert(END, "Name:\t" + self.name_var.get() + "\n")
        self.txt_box.insert(END, "Address:\t" + self.address_var.get() + "\n")
        self.txt_box.insert(END, "Post Code:\t" + self.post_code_var.get() + "\n")
        self.txt_box.insert(END, "Contact No:\t" + self.contact_no_var.get() + "\n")
        self.txt_box.insert(END, "Book ID:\t" + self.book_id_var.get() + "\n")
        self.txt_box.insert(END, "Book Name:\t" + self.book_name_var.get() + "\n")
        self.txt_box.insert(END, "Issue Date:\t" + self.issue_date_var.get() + "\n")
        self.txt_box.insert(END, "Late Fine:\t" + self.late_fine_var.get() + "\n")

    #function of reset button
    def reset(self):
        self.member_var.set("")
        self.prn_no_var.set("")
        self.id_no_var.set("")
        self.name_var.set("")
        self.address_var.set("")
        self.post_code_var.set("")
        self.contact_no_var.set("")
        self.book_id_var.set("")
        self.book_name_var.set("")
        self.issue_date_var.set("")
        self.late_fine_var.set("")
        self.txt_box.delete("1.0", END)

    #functon for exit button
    def exit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System","Do You Want To Exit")
        if iExit>0:
            self.root.destroy()
            return
    
    #function for delete data button
    def delete_data(self):
        if self.prn_no_var.get()=="" or self.id_no_var.get()=="":
            messagebox.showerror("Error", "First Select Some Data To Delete", icon="error")

        else:
            con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
            cur = con.cursor()
            query = "delete from data where prn_number = %s"
            value = (self.prn_no_var.get(),)
            cur.execute(query, value)

            con.commit()
            self.fetch_data()
            self.reset()
            con.close()

            messagebox.showinfo("Library Management System", "Data Has Been Deleted Successfully!", icon= "info")



if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
