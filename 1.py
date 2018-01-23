from tkinter import *
import tkinter.messagebox as tm
import mysql.connector

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.l_1 = Label(self, text="Naam")
        self.l_2 = Label(self, text="Email")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.l_1.grid(row=0, sticky=E)
        self.l_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Inchecken", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()
        # #print("Clicked")
        # Username = self.entry_1.get()
        # Email = self.entry_2.get()
        #
        # #print(username, password)
        #
        # if Username == user[0] and Email == user[1]:
        #     tm.showinfo("Login info", "Welkom")
        # else:
        #     tm.showerror("Login error", "Incorrect Email of wachtwoord")

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='sportschool')
        cursor = cnx.cursor()

        query = (
        "SELECT firstname, email FROM users WHERE firstname == self.entry_1.get() AND email == self.entry_2.get()")
        cursor.execute(query)
        print('hallo')

        cursor.close()
        cnx.close()
root = Tk()
lf = LoginFrame(root)
root.mainloop()