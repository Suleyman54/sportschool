from tkinter import *
import tkinter.messagebox as tm
from time import gmtime, strftime

import mysql.connector

# cnx = mysql.connector.connect(host='rdbms.strato.de', port=3306, user='U3010298', password='JXe7m0e94KJytDETU4nuCL6efy10RsGvTxULGz1t', database='DB3010298', use_pure=False)

config = {
  'user': 'U3010298',
  'password': 'JXe7m0e94KJytDETU4nuCL6efy10RsGvTxULGz1t',
  'host': 'rdbms.strato.de',
  'database': 'DB3010298',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT id, firstname, email FROM users")

cursor.execute(query)

firstname = []
email = []
users = []

for x in cursor:
    firstname.append(x[1])
    email.append(x[2])
    users.append(x)

cursor.close()
cnx.close()


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.l_1 = Label(self, text="Voornaam")
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

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()
        start_date = str(strftime("%Y-%m-%d", gmtime()))
        if username in firstname and password in email:
            tm.showinfo("Inloggen info", "Welkom " + username)
            cnx = mysql.connector.connect(host='rdbms.strato.de', port=3306, user='U3010298',
                                          password='JXe7m0e94KJytDETU4nuCL6efy10RsGvTxULGz1t', database='DB3010298')
            cursor2 = cnx.cursor()

            matching = [s for s in users if username in s]

            user_id = int(matching[0][0])
            try:
                query_insert = "INSERT INTO tracks (start_date, user_id, location_id) VALUES (%s, %s, %s)"
                cursor2.execute(query_insert, (start_date, user_id, 1))
                cnx.commit()
            except:
                cnx.rollback()


            cnx.close()
        else:
            tm.showerror("Login error", "Incorrect Voornaam of Email ")

root = Tk()
lf = LoginFrame(root)
root.mainloop()