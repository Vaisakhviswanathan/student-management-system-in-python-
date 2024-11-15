from tkinter import *
from tkinter import messagebox

window=Tk()

def login():
    if usernameEntry.get()== '' or passwordEntry.get()=='':
        messagebox.showerror("Error", 'Fields cannot be empty')
    elif usernameEntry.get()=='user' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import student
    else:
        messagebox.showerror('Error','Please enter correct credentials')



window.geometry('1280x700+0+0')
window.resizable(False,False)
window.title("Student Login")
window.config(bg="white")

loginframe=Frame(window,bg='white')
loginframe.place(x=400,y=150)

usernameLabel=Label(loginframe, text="Username", font=('times new roman',20,'bold'), bg='white')
usernameLabel.grid(row=1,column=0)

passwordLabel=Label(loginframe, text="Password",  font=('times new roman',20,'bold'), bg='white')
passwordLabel.grid(row=2,column=0,padx=20,pady=10)

usernameEntry=Entry(loginframe, font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,padx=20)

passwordEntry=Entry(loginframe, font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,padx=20,pady=10)

loginButton=Button(loginframe,text='Login',font=('times new roman',14,'bold'),width=15,fg='white', bg='cornflowerblue'
                   , activebackground='cornflowerblue', activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1)







window.mainloop()
