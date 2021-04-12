from tkinter import *
import tkinter.font as font


class Login(Frame):
    """The GUI for login page"""
    def __init__(self, parent, model, controller):
        Frame.__init__(self, parent)
        self.model = model
        self.controller = controller
        self.pw = ''
        self.u_str = StringVar()
        self.p_str = StringVar()
        self.e_str = StringVar()

        f = font.Font(family='Times', size=32)
        self.title = Label(self, text="Login", font=f)
        self.title.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.user_label = Label(self, text="Username")
        self.user_label.place(relx=0.38, rely=0.49, anchor=CENTER)
        self.pass_label = Label(self, text="Password")
        self.pass_label.place(relx=0.38, rely=0.53, anchor=CENTER)

        self.username = Entry(self, textvariable=self.u_str)
        self.username.place(relx=0.5, rely=0.49, anchor=CENTER)
        self.password = Entry(self, textvariable=self.p_str)
        self.password.bind("<KeyRelease>", self.press)
        self.password.bind("<BackSpace>", self.dele)
        self.password.place(relx=0.5, rely=0.53, anchor=CENTER)
        self.enter = Button(self, text="Enter", relief=GROOVE, command=self.login)
        self.enter.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.error = Label(self, textvariable=self.e_str)
        self.error.place(relx=0.5, rely=0.62, anchor=CENTER)

    def login(self):
        """Check if login info was valid and then switch to the the correct
        screen for the login"""
        if self.model.check(self.u_str.get(), self.pw):
            job = self.model.get_job(self.u_str.get())
            if job == 'Manager' or job == 'Admin':
                self.controller.show_frame('ManagerPage')
            elif job == 'Chef':
                self.controller.show_frame('ChefPage')
            else:
                self.controller.show_frame('ServerPage')
            self.u_str.set('')
            self.p_str.set('')
            self.e_str.set('')
            self.pw = ''
        else:
            self.e_str.set("Invalid username or password")

    def press(self, event):
        """save user str and replace it with * in the entry"""
        p = ""
        for x in range(0, len(self.p_str.get())):
            p += "*"
        self.p_str.set(p)
        if event.char != '':
            self.pw += event.char

    def dele(self, event):
        """Delete from the save password when they hit backspace"""
        self.pw = self.pw[0:-1]


class LoginModel:
    """Holds the login info of all employees"""
    def __init__(self, employee):
        self.logins = {}
        self._get_login(employee)

    def _get_login(self, employee):
        """save all the login info from all employees in the list"""
        for x in employee:
            self.logins[x.username] = (x.password, x.job)

    def check(self, username, password):
        """Check if the username and password is valid. Return True
        if the username is valid and the password is valid for the username"""
        if username in self.logins:
            if self.logins[username][0] == password:
                return True
        return False

    def get_job(self, username):
        """return the job position of the username"""
        return self.logins[username][1]
