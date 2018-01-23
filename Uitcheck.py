from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.l_1 = Label(self, text="Email")
        self.l_2 = Label(self, text="Wachtwoord")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.l_1.grid(row=0, sticky=E)
        self.l_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Uitchecken", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        if username == 'Suleyman' and password == "Henk1":
            tm.showinfo("Logout info", "Tot ziens Suleyman")
        else:
            tm.showerror("Login error", "Incorrect Email of wachtwoord")
root = Tk()
lf = LoginFrame(root)
root.mainloop()