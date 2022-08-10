from tkinter import*
from tkinter import ttk
import mysql.connector as a
from tkinter import messagebox


class StoreDetails(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        #main fram
        self.geometry("800x800")
        self.title("Book Details")
        self.resizable(False, False)



        #variables
        self.b_name_var = StringVar()
        self.author_var = StringVar()
        self.b_subject_var = StringVar()
        self.search_var = StringVar()
          
        #top frame with title  
        self.top_frame = Frame(self, height=150, bg="powder blue")
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text="BOOK DETAILS", font="arial 18 bold", bg="powder blue", fg="black")
        heading.place(x=300, y=60)

        #body frame
        self.bodyframe = Frame(self, height=650, bg="white")
        self.bodyframe.pack(fill=X)
        
         #declaration of delete book button
        delete_book_button = Button(self.bodyframe, text="Delete Book", command=self.delete_book)
        delete_book_button.place(x=350, y=320)

        #frame for database information
        info_frame = Frame(self, bd=8, relief=RIDGE, padx=20, bg="powder blue")
        info_frame.place(x=0, y=250, width=800, height=195)

        # search_frame = Frame(self, bd=8, relief=RIDGE, padx=20, bg="powder blue")
        # search_frame.place(x=0, y=150, width=800, height=50)

        # lblsearch = Label(search_frame, bg="powder blue", text="Search :", font="arial 12 bold", padx=2, pady=6)
        # lblsearch.grid(row=0, column=0, sticky=W)

        # txt_search = Entry(search_frame, font="times 11", textvariable=self.search_var, width=33)
        # txt_search.grid(row=0, column=1) 

        # search_btn = Button(search_frame, text="Search Now")
        # search_btn.grid(row=0, column=3, padx=20)

        
        #declaration of scroll 
        yscroll = ttk.Scrollbar(info_frame, orient=VERTICAL)

        #dedlaration of book details table
        self.book_details_table = ttk.Treeview(info_frame, columns=("b_name", "author", "b_subject"),
                                       yscrollcommand=yscroll.set)
        
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.book_details_table.yview)

        
        #declaration of columns for table
        self.book_details_table.heading("b_name", text="Book Name")
        self.book_details_table.heading("author", text="Book Author")
        self.book_details_table.heading("b_subject", text="Book Subject")

        
        self.book_details_table["show"] = "headings"
        self.book_details_table.pack(fill=BOTH, expand=1)
      
        
        #setting the width of columns
        self.book_details_table.column("b_name", width=100)
        self.book_details_table.column("author", width=100)
        self.book_details_table.column("b_subject", width=100)
          
        #fetching data from data base in the table
        self.fetch_data()
        self.book_details_table.bind("<ButtonRelease-1>", self.get_cursor)






    #function for delete data button
    def delete_book(self):
        if self.b_name_var.get()=="" or self.author_var.get()=="":
            messagebox.showerror("Error", "First Select Some Data TO Delete", icon="error")

        else:
            con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
            cur = con.cursor()
            query = "delete from books where b_name = %s"
            value = (self.b_name_var.get(),)
            cur.execute(query, value)

            con.commit()
            self.fetch_data()
            con.close()

            messagebox.showinfo("Library Management System", "Data Has Been Deleted Successfully!", icon= "info")
    

    #function to fetch data in the table
    def fetch_data(self):
        con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
        cur = con.cursor()
        query = "select * from books"
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows)!= 0:
            self.book_details_table.delete(*self.book_details_table.get_children())
            for i in rows:
                self.book_details_table.insert("", END, values=i)
            con.commit()
        con.close()

    
    def get_cursor(self, event=""):
        cur_row = self.book_details_table.focus()
        content = self.book_details_table.item(cur_row)
        row = content['values']


        self.b_name_var.set(row[0])
        self.author_var.set(row[1])
        self.b_subject_var.set(row[2])
    
    # def search(self):
    #     con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
    #     cur = con.cursor()
    #     value = self.txt_seerch.get()
    #     searchquery = cur.execute("select * from books where book_name like %s", ('%'+ value + '%',))
    #     searchquery = cur.fetchall()
    #     self.management_box.delete(0, 'end')
    #     counter = 0
    #     for book in searchquery:
    #         self.management_box.insert(counter, str(book[0] ) + "-" + str(book[1]))
    #         counter +=1
