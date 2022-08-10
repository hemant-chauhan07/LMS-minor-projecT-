from tkinter import *
from tkinter import messagebox
import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="database@23", database="project_lms")
cur = con.cursor()


class StoreBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        #main frame
        self.geometry("800x800")
        self.title("Add Book")
        self.resizable(False, False)
        
        #top frame with title
        self.top_frame = Frame(self, height=150, bg="powder blue")
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text="Add Book", font="arial 18 bold", bg="powder blue", fg="black")
        heading.place(x=300, y=60)

        #body frame
        self.bodyframe = Frame(self, height=650, bg="white")
        self.bodyframe.pack(fill=X)

      
        #declaration of book name label
        self.lbl_book_name = Label(self.bodyframe, text="Enter Book Name:", font="arial 12 bold", bg="white")
        self.lbl_book_name.place(x=40, y=45)
        self.txt_bookname_box = Entry(self.bodyframe, width=30, bd=2)
        self.txt_bookname_box.place(x=200, y=40)
       
        
        
        #declaration of book author label
        self.lbl_book_author = Label(self.bodyframe, text="Enter Book Author:", font="arial 12 bold", bg="white")
        self.lbl_book_author.place(x=40, y=80)
        self.txt_bookauthor_box = Entry(self.bodyframe, width=30, bd=2)
        self.txt_bookauthor_box.place(x=200, y=80)
        

        #declaration of book subject label
        self.lbl_book_subject = Label(self.bodyframe, text="Enter Book Subject:", font="arial 12 bold", bg="white")
        self.lbl_book_subject.place(x=40, y=120)
        self.txt_booksubject_box = Entry(self.bodyframe, width=30, bd=2)
        self.txt_booksubject_box.place(x=200, y=120)
       
        # declaration of save book button
        save_book_button = Button(self.bodyframe, text="Save Now", command=self.savebook)
        save_book_button.place(x=270, y=200)

        
     #function for save book button   
    def savebook(self):
        bookname = self.txt_bookname_box.get()
        bauthor = self.txt_bookauthor_box.get()
        booksubject = self.txt_booksubject_box.get()



        if (bookname and booksubject !=0) :
            try: 
                query = "insert into books(b_name, author, subject) values(%s,%s,%s)"
                value = (bookname, bauthor, booksubject)
                cur.execute(query, value)
                con.commit()
                messagebox.showinfo("ADDING BOOK","Data Entered Successfully!", icon="info")
            
            except:
                messagebox.showerror("ADDING BOOK","Something Went Wrong!!", icon="error")

        
        else:
            messagebox.showwarning("ADDING BOOK","All Fields Are Mandatory", icon="warning")
        con.close()
