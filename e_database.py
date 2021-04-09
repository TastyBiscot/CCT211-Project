from employee import Employee
from tkinter import *
from tkinter.ttk import *
import csv


class EDatabase:

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
        self.employees.append(employee)

    def remove_employee(self, e):
        if e in self.employees:
            self.employees.remove(e)
            return True
        else:
            return False

    def save(self):
        """save the employees into the csv file"""
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["First", "Last", "Job", "Username", "Password"])
            for x in self.employees:
                writer.writerow([x.fname, x.lname, x.job, x.username,
                                 x.password])


class EDGUI(Frame):
    def __init__(self):

        self.Table = Frame(self, width=500)
        self.Table.pack(side=TOP)

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

        self.tree.pack(expand=True, fill=BOTH)
        self.read_file()


if __name__ == '__main__':
    n = EDatabase("employees.csv")
    e = Employee("Bob", "Larry", "Admin", "Apple", "Pie")
    n.add_employee(e)
    n.remove_employee(e)
    n.save()
