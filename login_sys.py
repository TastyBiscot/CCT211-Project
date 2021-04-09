from tkinter import *
import tkinter.font as font


class Login(Frame):
    def __init__(self, parent, model):
        Frame.__init__(self, parent)
        self.model = model

        f = font.Font(family='Times', size=32)
        self.title = Label(self, text="Login", font=f)
        self.title.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.user_label = Label(self, text="Username")
        self.user_label.place(relx=0.38, rely=0.49, anchor=CENTER)
        self.pass_label = Label(self, text="Password")
        self.pass_label.place(relx=0.38, rely=0.53, anchor=CENTER)

        self.username = Entry(self)
        self.username.place(relx=0.5, rely=0.49, anchor=CENTER)
        self.password = Entry(self)
        self.password.place(relx=0.5, rely=0.53, anchor=CENTER)
        self.enter = Button(self, text="Enter", relief=GROOVE)
        self.enter.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.error = Label(self)
        self.error.place(relx=0.5, rely=0.62, anchor=CENTER)

    def login(self):
        if self.model.check(self.username.get(), self.password.get()):
            pass
        else:
            self.error.configure(Text="Invalid username or password")


class LoginModel:
    def __init__(self, employee):
        self.logins = {}
        self._get_login(employee)

    def _get_login(self, employee):
        for x in employee:
            self.logins[x.username] = x.password

    def check(self, username, password):
        if username in self.logins:
            if self.logins[username] == password:
                return True
        return False


if __name__ == '__main__':
    root = Tk()
    root.title("Ex1")
    root.geometry("800x600")
    log = Login(root)
    log.pack(expand=True, fill=BOTH)
    root.mainloop()
