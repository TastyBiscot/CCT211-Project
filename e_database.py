from employee import Employee
from tkinter import *
from tkinter.ttk import *
import csv
import tkinter.font as font
import re


class EDatabase:
    """
    The model of the Employee database. Read and write Employee information
    into a CSV files.
    Username for each employee is unique.
    """

    def __init__(self, filename):
        self.employees = []
        self.filename = filename
        self._get_employee()

    def _get_employee(self):
        """read from csv file to get employees"""
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                fname = row['First']
                lname = row['Last']
                job = row['Job']
                username = row['Username']
                password = row['Password']
                self.employees.append(Employee(fname, lname, job, username,
                                               password))

    def add_employee(self, employee):
        """Takes an employee and add it and then save it to the CSV."""
        self.employees.append(employee)
        self.save()

    def check_username(self, un):
        """Check if the username is already taken. Return True if not taken"""
        for x in self.employees:
            if x.username == un:
                return False
        return True

    def remove_employee(self, un):
        """remove an employee base on there username"""
        rm = None
        for x in self.employees:
            if x.username == un:
                rm = x
        if rm is not None:
            self.employees.remove(rm)
            self.save()

    def save(self):
        """save the employees into the csv file"""
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["First", "Last", "Job", "Username", "Password"])
            for x in self.employees:
                writer.writerow([x.fname, x.lname, x.job, x.username,
                                 x.password])


class EDGUI(Frame):
    """
    The GUI for the Database.
    """
    def __init__(self, parent, model, controller):
        Frame.__init__(self, parent)
        # save a reference to database model
        self.model = model
        # Controller is use to transfer between screen on the main program
        self.controller = controller
        # The item on the tree view currently selected
        self.curItem = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Font for the title
        t_size = font.Font(family='Times', size=32)

        # Build the add employee page
        self.addframe = Frame(self)
        self.addframe.grid(row=0, column=0, sticky="nsew")

        validation = self.addframe.register(self.v)

        self.a_title = Label(self.addframe, text="Employee Information",
                             font=t_size)
        self.a_title.place(relx=0.48, rely=0.3, anchor=CENTER)

        self.fn_l = Label(self.addframe, text='First Name')
        self.fn_l.place(relx=0.37, rely=0.37, anchor=CENTER)

        self.ln_l = Label(self.addframe, text='Last Name')
        self.ln_l.place(relx=0.37, rely=0.42, anchor=CENTER)

        self.job_l = Label(self.addframe, text='Job')
        self.job_l.place(relx=0.37, rely=0.47, anchor=CENTER)

        self.un_l = Label(self.addframe, text='Username')
        self.un_l.place(relx=0.37, rely=0.52, anchor=CENTER)

        self.pw_l = Label(self.addframe, text='Password')
        self.pw_l.place(relx=0.37, rely=0.57, anchor=CENTER)

        self.fn = StringVar()
        self.fn_e = Entry(self.addframe, textvariable=self.fn, validate="key",
                          validatecommand=(validation, "%S"))
        self.fn_e.place(relx=0.5, rely=0.37, anchor=CENTER)

        self.ln = StringVar()
        self.ln_e = Entry(self.addframe, textvariable=self.ln, validate="key",
                          validatecommand=(validation, "%S"))
        self.ln_e.place(relx=0.5, rely=0.42, anchor=CENTER)

        self.options = ["Manager", "Chef", "Server"]
        self.job = StringVar()
        self.job.set(self.options[0])
        self.job_e = OptionMenu(self.addframe, self.job, *self.options)
        self.job_e.place(relx=0.5, rely=0.47, anchor=CENTER)

        validation = self.addframe.register(self.un_v)
        self.un = StringVar()
        self.un_e = Entry(self.addframe, textvariable=self.un, validate="key",
                          validatecommand=(validation, "%S"))
        self.un_e.place(relx=0.5, rely=0.52, anchor=CENTER)

        self.pw = StringVar()
        self.pw_e = Entry(self.addframe, textvariable=self.pw)
        self.pw_e.place(relx=0.5, rely=0.57, anchor=CENTER)

        self.add_e = Button(self.addframe, text='Add', command=self.add)
        self.add_e.place(relx=0.48, rely=0.62, anchor=CENTER)

        self.errors = []
        for x in range(0, 4):
            self.errors.append(StringVar())

        self.fn_error = Label(self.addframe, textvariable=self.errors[0],
                              justify=LEFT, foreground='red')
        self.fn_error.place(relx=0.64, rely=0.37, anchor=CENTER)

        self.ln_error = Label(self.addframe, textvariable=self.errors[1],
                              justify=LEFT, foreground='red')
        self.ln_error.place(relx=0.64, rely=0.42, anchor=CENTER)

        self.un_error = Label(self.addframe, textvariable=self.errors[2],
                              justify=LEFT, foreground='red')
        self.un_error.place(relx=0.64, rely=0.52, anchor=CENTER)

        self.pw_error = Label(self.addframe, textvariable=self.errors[3],
                              justify=LEFT, foreground='red')
        self.pw_error.place(relx=0.64, rely=0.57, anchor=CENTER)

        self.back_db = Button(self.addframe, text='Back',
                              command=lambda: self.go_to_page(self.mainframe))
        self.back_db.place(relx=0.04, rely=0.97, anchor=CENTER)

        # Build a main frame that display each employee
        self.mainframe = Frame(self)
        self.mainframe.grid(row=0, column=0, sticky="nsew")

        self.d_title = Label(self.mainframe, text='Employee Database',
                             font=t_size)
        self.d_title.pack(side=TOP, fill=X)

        # Build a frame to hold all the button
        self.buttons = Frame(self.mainframe)
        self.buttons.pack(side=LEFT, fill=Y)
        self.add = Button(self.buttons, text='Add Employee',
                          command=lambda: self.go_to_page(self.addframe))
        self.add.pack()
        self.dele = Button(self.buttons, text='Delete Employee', state=DISABLED,
                           command=self.delete)
        self.dele.pack()
        self.back = Button(self.buttons, text='Back', command=self.go_back)
        self.back.pack()

        # Build a frame to hold the Treeview of the employee
        self.Table = Frame(self.mainframe)
        self.Table.pack(side=RIGHT, expand=True, fill=BOTH)

        self.sx = Scrollbar(self.Table, orient=HORIZONTAL)
        self.sy = Scrollbar(self.Table, orient=VERTICAL)

        self.tree = Treeview(self.Table, selectmode='none')
        self.tree['columns'] = ('Last_Name', 'Job', 'Username')

        self.tree.column('#0', minwidth=10, width=100)
        self.tree.column('Last_Name', minwidth=10, width=100)
        self.tree.column('Job', minwidth=10, width=100)
        self.tree.column('Username', minwidth=10, width=100)

        self.tree.heading('#0', text="First Name", anchor=W)
        self.tree.heading('Last_Name', text='Last Name')
        self.tree.heading('Job', text='Position')
        self.tree.heading('Username', text='Username')

        self.sx.config(command=self.tree.xview)
        self.sx.pack(side=BOTTOM, fill=X)
        self.sy.config(command=self.tree.yview)
        self.sy.pack(side=RIGHT, fill=Y)

        # Bind the mouse click to select method to the tree
        self.tree.bind("<Button-1>", self.select)

        self.tree.pack(expand=True, fill=BOTH)

        # Add all the employee to the tree
        self._insert_employees()

        # raise the main interface frame the the front
        self.mainframe.tkraise()

    def _insert_employees(self):
        """Add all the employee to the treeview"""
        for x in self.model.employees:
            self.tree.insert("", 'end', text=x.fname, values=(x.lname, x.job,
                                                              x.username))

    def select(self, event):
        """ Get the item the user click on in the treeview and enable the delete
        button if it was a valid item"""
        self.curItem = self.tree.focus()
        if len(self.tree.item(self.curItem)['values']) >= 3:
            self.dele.config(state=NORMAL)
        else:
            self.dele.config(state=DISABLED)
            self.curItem = None

    def delete(self):
        """remove the employee from the database"""
        self.model.remove_employee(self.tree.item(self.curItem)['values'][2])
        self.tree.delete(self.curItem)
        self.curItem = None
        self.dele.configure(state=DISABLED)

    def go_to_page(self, frame):
        """Method to move between the adding user frame and the main database
        frame"""
        self.fn.set('')
        self.ln.set('')
        self.job.set(self.options[0])
        self.un.set('')
        self.pw.set('')
        self.dele.configure(state=DISABLED)
        frame.tkraise()

    def add(self):
        """Add user to the data base"""
        fn = self.fn.get()
        ln = self.ln.get()
        job = self.job.get()
        un = self.un.get()
        pw = self.pw.get()
        error = False

        # Check if there is any error in the information
        if fn == '':
            self.errors[0].set("Cannot be blank")
            error = True

        if ln == '':
            self.errors[1].set("Cannot be blank")
            error = True

        if un == '':
            self.errors[2].set("Cannot be blank")
            error = True
        elif not self.model.check_username(un):
            self.errors[2].set("Username taken")
            error = True

        if pw == '':
            self.errors[3].set("Cannot be blank")
            error = True

        # Add new employee to the database if there is no error
        if not error:
            self.model.add_employee(Employee(fn, ln, job, un, pw))
            self.tree.insert("", 'end', text=fn, values=(ln, job, un))
            self.go_to_page(self.mainframe)

    def go_back(self):
        """Use to go back the the Manager Menu"""
        self.fn.set('')
        self.ln.set('')
        self.job.set(self.options[0])
        self.un.set('')
        self.pw.set('')
        self.dele.configure(state=DISABLED)
        self.controller.show_frame('ManagerPage')

    def v(self, e):
        """Validate input to make sure only alphabet are used"""
        p = re.compile("[a-zA-Z]")
        return p.match(e) is not None

    def un_v(self, e):
        """Validate input to make sure no space was used"""
        p = re.compile("\S")
        return p.match(e) is not None
