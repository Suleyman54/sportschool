from tkinter import *
import time
import tkinter.messagebox as tm
import mysql.connector

cnx = mysql.connector.connect(user='pi', password='l5VPO0VpD3eWvttbKYW4',
                              host='46.101.127.123',
                              database='sportschool')
cursor = cnx.cursor()

query1 = ("SELECT id, firstname, email FROM users")

cursor.execute(query1)

firstname = []
email = []
users = []

for x in cursor:
    firstname.append(x[1])
    email.append(x[2])
    users.append(x)

query2 = ("SELECT id FROM sport_type_names WHERE name = 'loopband'")

cursor.execute(query2)

sport_id = []

for v in cursor:
    sport_id.append(v[0])

cursor.close()
cnx.close()


class LoginFrame(Frame):

    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setwarnings(False)
    # GPIO.setup(11, GPIO.OUT)
    # GPIO.setup(7, GPIO.OUT)

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
        username = self.entry_1.get()
        password = self.entry_2.get()
        if username in firstname and password in email:
            tm.showinfo("Inloggen info", "Welkom " + username)

            class StopWatch(Frame):
                """ Implements a stop watch frame widget. """

                def __init__(self, parent=None, **kw):
                    Frame.__init__(self, parent, kw)
                    self._start = 0.0
                    self._elapsedtime = 0.0
                    self._running = 0
                    self.timestr = StringVar()
                    self.makeWidgets()
                    # self._counter = 0

                def makeWidgets(self):
                    """ Make the time label. """
                    time_label = Label(self, textvariable=self.timestr)
                    self._setTime(self._elapsedtime)
                    time_label.pack(fill=X, expand=NO, pady=2, padx=2)

                def _update(self):
                    """ Update the label with elapsed time. """
                    self._elapsedtime = time.time() - self._start
                    self._setTime(self._elapsedtime)
                    self._timer = self.after(50, self._update)

                def _setTime(self, elap):
                    """ Set the time string to Minutes:Seconds:Hundreths """
                    minutes = int(elap / 60)
                    seconds = int(elap - minutes * 60.0)
                    hseconds = int((elap - minutes * 60.0 - seconds) * 100)
                    self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

                def Start(self):
                    """ Start the stopwatch, ignore if running. """
                    if not self._running:
                        self._start = time.time() - self._elapsedtime
                        self._update()
                        self._running = 1
                        return time.time
                    return self._elapsedtime

                def Stop(self):
                    """ Stop the stopwatch, ignore if stopped. """
                    if self._running:
                        self.after_cancel(self._timer)
                        self._elapsedtime = time.time() - self._start
                        duration = float(self._elapsedtime)

                        afstand = float(duration * 2.777777778)
                        print("{0:.2f}".format(afstand))

                        self._setTime(self._elapsedtime)
                        self._running = 0

                        cnx = mysql.connector.connect(user='pi', password='l5VPO0VpD3eWvttbKYW4',
                                                      host='46.101.127.123',
                                                      database='sportschool')
                        cursor_insert = cnx.cursor()

                        matching = [s for s in users if username in s]

                        user_id = int(matching[0][0])

                        try:
                            query_insert = "INSERT INTO sport_activities (duration, distance, user_id, sport_equipment_id) VALUES (%s,%s,%s,%s)"
                            cursor_insert.execute(query_insert,
                                                  (duration, afstand, user_id, int(sport_id[0])))
                            cnx.commit()

                        except:
                            cnx.rollback()
                            print('lukt niet')

                        cnx.close()

                def Reset(self):
                    """ Reset the stopwatch. """
                    self._start = time.time()
                    self._elapsedtime = 0.0
                    self._setTime(self._elapsedtime)
                    self._counter = 0

            def main():
                root = Tk()
                sw = StopWatch(root)
                sw.pack(side=TOP)

                Button(root, text='Start', command=sw.Start).pack(side=LEFT)
                Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
                Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
                Button(root, text='Quit', command=root.quit).pack(side=LEFT)

                root.mainloop()

            if __name__ == '__main__':
                main()
            cursor.close()
            cnx.close()

        else:
            tm.showerror("Login error", "Incorrect Voornaam of Email ")

root = Tk()
lf = LoginFrame(root)
root.mainloop()