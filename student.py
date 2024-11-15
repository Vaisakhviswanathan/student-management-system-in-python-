from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox

window = Tk()

window.geometry('1280x700+0+0')
window.resizable(False, False)
window.title("Student Management System")
window.config(bg="white")

titleLabel = Label(window, text="Student Management System", font=('Arial', 30, 'bold'),
                   border=12, bg="blue", foreground="yellow", relief=GROOVE)
titleLabel.pack(side=TOP, fill=X)

detailFrame = LabelFrame(window, text="Enter Details", font=('Arial', 20), bd=12, relief=GROOVE, bg="lightgrey")
detailFrame.place(x=20, y=90, width=420, height=595)

dataFrame = Frame(window, bd=12, relief=GROOVE, bg="lightgrey")
dataFrame.place(x=475, y=90, width=780, height=595)

# ======VARIABLES======

rollno = StringVar()
name = StringVar()
class_var = StringVar()
section = StringVar()
contact = StringVar()
parentsn = StringVar()
address = StringVar()
gender = StringVar()
dob = StringVar()

search_by = StringVar()


# ========FUNCTIONS=======

def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
    curr = conn.cursor()
    curr.execute("select * from data")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)
        conn.commit()
    conn.close()


def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        messagebox.showerror('Error', "Please fill all the fields")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
        curr = conn.cursor()
        curr.execute("insert into data values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (rollno.get(), name.get(), class_var.get(),
                      section.get(), contact.get(), parentsn.get(), address.get(), gender.get(), dob.get()))
        conn.commit()
        conn.close()

        fetch_data()
        clear()


def clear():
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    parentsn.set("")
    address.set("")
    gender.set("")
    dob.set("")
    addButton.config(state="normal")


def get_cursor(event):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    parentsn.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])
    addButton.config(state="disabled")


def update_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
    curr = conn.cursor()
    curr.execute("update data set name=%s,class=%s,section=%s, contact=%s, parentsn=%s, address=%s, gender=%s,dob=%s "
                 "where rollno=%s",
                 (name.get(), class_var.get(), section.get(), contact.get(), parentsn.get(), address.get(),
                  gender.get(), dob.get(), rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()


def delete_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
    curr = conn.cursor()
    curr.execute("delete from data where rollno=%s", rollno.get())
    conn.commit()
    conn.close()
    fetch_data()
    clear()
    messagebox.showinfo('Deleted', 'Successfully Deleted')


def exit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit ?')
    if res:
        window.destroy()
    else:
        pass


def search_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
    curr = conn.cursor()
    curr.execute("select * from data where name=%s", search_by.get())
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)
        conn.commit()
    conn.close()


# ==========ENTRY========


rollnoLabel = Label(detailFrame, text="Roll No", font=('Arial', 15), bg='lightgrey')
rollnoLabel.grid(row=0, column=0, padx=2, pady=2)

rollnoEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=rollno)
rollnoEntry.grid(row=0, column=1, padx=2, pady=2)

nameLabel = Label(detailFrame, text="Name", font=('Arial', 15), bg='lightgrey')
nameLabel.grid(row=1, column=0, padx=2, pady=2)

nameEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=name)
nameEntry.grid(row=1, column=1, padx=2, pady=2)

classLabel = Label(detailFrame, text="Class", font=('Arial', 15), bg="lightgrey")
classLabel.grid(row=2, column=0, padx=2, pady=2)

classEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=class_var)
classEntry.grid(row=2, column=1, padx=2, pady=2)

sectionLabel = Label(detailFrame, text="Section", font=('Arial', 15), bg="lightgrey")
sectionLabel.grid(row=3, column=0, padx=2, pady=2)

sectionEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=section)
sectionEntry.grid(row=3, column=1, padx=2, pady=2)

contactLabel = Label(detailFrame, text="Contact", font=('Arial', 15), bg="lightgrey")
contactLabel.grid(row=4, column=0, padx=2, pady=2)

contactEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=contact)
contactEntry.grid(row=4, column=1, padx=2, pady=2)

fnameLabel = Label(detailFrame, text="Parent's Name", font=('Arial', 15), bg="lightgrey")
fnameLabel.grid(row=5, column=0, padx=2, pady=2)

fnameEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=parentsn)
fnameEntry.grid(row=5, column=1, padx=2, pady=2)

addressLabel = Label(detailFrame, text="Address", font=('Arial', 15), bg="lightgrey")
addressLabel.grid(row=6, column=0, padx=2, pady=2)

addressEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=address)
addressEntry.grid(row=6, column=1, padx=2, pady=2)

genderLabel = Label(detailFrame, text="Gender", font=('Arial', 15), bg="lightgrey")
genderLabel.grid(row=7, column=0, padx=2, pady=2)

genderEntry = Combobox(detailFrame, font=('Arial', 15), state="readonly", textvariable=gender)
genderEntry['values'] = ("Male", "Female", "Others")
genderEntry.grid(row=7, column=1, padx=2, pady=2)

dobLabel = Label(detailFrame, text="D.O.B", font=('Arial', 15), bg="lightgrey")
dobLabel.grid(row=8, column=0, padx=2, pady=2)

dobEntry = Entry(detailFrame, font=('Arial', 15), bd=7, textvariable=dob)
dobEntry.grid(row=8, column=1, padx=2, pady=2)

# =======BUTTONS=============

btnFrame = Frame(detailFrame, bg="lightgrey", bd=10, relief=GROOVE)
btnFrame.place(x=22, y=390, width=340, height=155)

addButton = Button(btnFrame, bg="lightgrey", text="Add", width=15, font=('Arial', 11), bd=7, command=add_func)
addButton.grid(row=0, column=0, padx=2, pady=2)

updateButton = Button(btnFrame, bg="lightgrey", text="Update", width=15, font=('Arial', 11), bd=7, command=update_func)
updateButton.grid(row=0, column=1, padx=2, pady=2)

delButton = Button(btnFrame, bg="lightgrey", text="Delete", width=15, font=('Arial', 11), bd=7, command=delete_func)
delButton.grid(row=1, column=0, padx=2, pady=2)

clearb = Button(btnFrame, bg="lightgrey", text="Clear", width=15, font=('Arial', 11), bd=7, command=clear)
clearb.grid(row=1, column=1, padx=2, pady=2)

showb = Button(btnFrame, bg="lightgrey", text="Show", width=15, font=('Arial', 11), bd=7, command=fetch_data)
showb.grid(row=2, column=0, padx=2, pady=2)

exitb = Button(btnFrame, bg="lightgrey", text="Exit", width=15, font=('Arial', 11), bd=7, command=exit)
exitb.grid(row=2, column=1, padx=2, pady=2)

# ===========Search=============

searchFrame = Frame(dataFrame, bg="lightgrey", bd=10, relief=GROOVE)
searchFrame.pack(side=TOP, fill=X)

searchLabel = Label(searchFrame, text="Search", font=('Arial', 14), bg="lightgrey")
searchLabel.grid(row=0, column=0, padx=12, pady=2)

searchCB = Entry(searchFrame, font=('Arial', 14), bd=7, textvariable=search_by)
searchCB.grid(row=0, column=1, padx=12, pady=2)

# searchCB=Combobox(searchFrame,font=('Arial',14), state="readonly",)
# searchCB['values']=("Name","Roll No")
# searchCB.grid(row=0, column=1,padx=12,pady=2)

searchButton = Button(searchFrame, bg="lightgrey", text="Search", width=14, font=('Arial', 13), bd=9,
                      command=search_func)
searchButton.grid(row=0, column=2, padx=12, pady=2)

showallBtn = Button(searchFrame, bg="lightgrey", text="Show All", width=14, font=('Arial', 13), bd=9,
                    command=fetch_data)
showallBtn.grid(row=0, column=3, padx=12, pady=2)

# ==============Database============


dbFrame = Frame(dataFrame, bg="lightgrey", bd=11, relief=GROOVE)
dbFrame.pack(expand=True, fill=BOTH)

y_scroll = Scrollbar(dbFrame, orient=VERTICAL)
x_scroll = Scrollbar(dbFrame, orient=HORIZONTAL)

student_table = Treeview(dbFrame, columns=(
"Roll No", "Name", "Class", "Section", "Contact", "Parents Name", "Address", "Gender", "DOB"),
                         yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)

student_table.heading("Roll No", text="Roll No")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Parents Name", text="Parents Name")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("DOB", text="DOB")

student_table['show'] = 'headings'

student_table.column("Roll No", width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact", width=100)
student_table.column("Parents Name", width=100)
student_table.column("Address", width=200)
student_table.column("Gender", width=100)
student_table.column("DOB", width=100)

student_table.pack(fill=BOTH, expand=True)

fetch_data()
student_table.bind("<ButtonRelease-1>", get_cursor)

window.mainloop()
