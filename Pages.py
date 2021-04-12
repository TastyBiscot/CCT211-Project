import tkinter as tk
import tkinter.ttk as ttk
from tkinter import*
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from login_sys import Login, LoginModel
from e_database import EDatabase, EDGUI
from server_log import Application
from TreeViewManager import CSV_Reader
from chef import Chef
from datetime import datetime
import os

df = pd.read_csv('All_Completed_Orders.csv') #reads file stores into dataframe


#result = df.sort_index(axis=1) #New dataframe with flipped data by y axis
#print(df)
df_server = df.groupby(['Server']).sum()
#print(df_server)

df2 = DataFrame(df,columns=['Seated','Server'])
#print(df2)
df2 = df2.groupby(['Server']).sum()
#print(df2)
df3 = DataFrame(df,columns=['Table','Time'])

topping_frames = [df['Topping 1'], df['Topping 2'], df['Topping 3']]
result = pd.concat(topping_frames).value_counts()
#print(result)
LARGE_FONT= ("Verdana", 12)
H1_FONT = ("Verdana", 24)
H2_FONT = ("Verdana", 20)


class FrameMoving(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Restaurant Management")
        container = tk.Frame(self)
        self.geometry("1200x900")
        self.s = ttk.Style()
        self.s.theme_use("clam")

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        e = EDatabase('employees.csv')
        e_gui = EDGUI(container, e, self)
        e_gui.grid(row=0, column=0, sticky="nsew")
        self.frames['EmployeePage'] = e_gui

        login_model = LoginModel(e.employees)
        login = Login(container, login_model, self)
        login.grid(row=0, column=0, sticky="nsew")
        self.frames['Login'] = login

        datestring = datetime.today().strftime("%Y-%m-%d")
        q = "All_Orders_{}.csv".format(datestring)
        e = 'All_Completed_Orders.csv'
        chef = Chef(container, self, q, e)
        chef.grid(row=0, column=0, sticky="nsew")
        self.frames['ChefPage'] = chef

        for F in (ManagerPage, ServerPage, GraphPageOne, GraphPageTwo, GraphPageThree, TreeViewPage):
            frame = F(container, self)

            self.frames[F.__name__] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('Login')

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class ManagerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Manager Page", font=H1_FONT)
        label.pack(pady=50,padx=10)

        button = ttk.Button(self, text="Purchase Statistics",width=30,
                            command=lambda: controller.show_frame("GraphPageOne"))
        button.pack(pady=20,padx=20)

        button = ttk.Button(self, text="All Sales Viewer",width=30,
                            command=lambda: controller.show_frame("TreeViewPage"))
        button.pack(pady=20,padx=20)

        button = ttk.Button(self, text="Employee Management",width=30,
                            command=lambda: controller.show_frame("EmployeePage"))
        button.pack(pady=20,padx=20)

        button = ttk.Button(self, text="Log Out",width=20,
                            command=lambda: controller.show_frame("Login"))
        button.pack(pady=20,padx=20)


class GraphPageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Table X Time Page", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)

        figure3 = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(df3['Time'], df3['Table'], color='r')
        scatter3 = FigureCanvasTkAgg(figure3, self)
        scatter3.get_tk_widget().pack(fill=tk.BOTH)
        ax3.legend(['Seated'])
        ax3.set_xlabel('Table')
        ax3.set_title('Table X Time')

        button = ttk.Button(self, text="Server X Seated Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageTwo"))
        button.pack(side = 'left', pady=10,padx=30)

        button = ttk.Button(self, text="Favourite Toppings Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageThree"))
        button.pack(side = 'left',pady=10,padx=30)


        button1 = ttk.Button(self, text="Return",width=25,
                            command=lambda: controller.show_frame("ManagerPage"))
        button1.pack(side = 'left',pady=10,padx=30)


class GraphPageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Server X Seated Page", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)

        figure3 = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.barh(df2['Seated'].keys(),df2['Seated'], color = 'b')
        scatter3 = FigureCanvasTkAgg(figure3, self)
        scatter3.get_tk_widget().pack(fill=tk.BOTH)
        ax3.legend(['Seated'])
        ax3.set_xlabel('Seated')
        ax3.set_title('Server X Seated')

        button = ttk.Button(self, text="Time X Seated Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageOne"))
        button.pack(side = 'left',pady=10,padx=30)


        button = ttk.Button(self, text="Favourite Toppings Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageThree"))
        button.pack(side = 'left',pady=10,padx=30)


        button1 = ttk.Button(self, text="Return",width=25,
                            command=lambda: controller.show_frame("ManagerPage"))
        button1.pack(side = 'left',pady=10,padx=30)


class GraphPageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Graph of Favourite Toppings", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)


        figure3 = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.barh(result.keys(),result, color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3, self)
        scatter3.get_tk_widget().pack(fill=tk.BOTH)
        ax3.legend(['Ordered'])
        ax3.set_xlabel('Total Amount')
        ax3.set_title('Graph of Favourite Toppings')

        button = ttk.Button(self, text="Time X Seated Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageOne"))
        button.pack(side = 'left',pady=10,padx=30)


        button = ttk.Button(self, text="Server X Seated Graph",width=25,
                            command=lambda: controller.show_frame("GraphPageTwo"))
        button.pack(side = 'left', pady=10,padx=30)


        button1 = ttk.Button(self, text="Return",width=25,
                            command=lambda: controller.show_frame("ManagerPage"))
        button1.pack(side = 'left',pady=10,padx=30)


class TreeViewPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'blue')
        label = ttk.Label(self, text="All Sales", font=H1_FONT)
        label.pack(pady=10,padx=10)

        view = CSV_Reader(self)
        view.pack(expand=True, fill="both",pady=10,padx=10)

        button1 = ttk.Button(self, text="Return",width=25,
                            command=lambda: controller.show_frame("ManagerPage"))
        button1.pack(pady=10,padx=10)

class ServerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'blue')
        label = tk.Label(self, text="Server", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        app = Application(self)
        app.pack(expand=True, fill=BOTH)

        button1 = ttk.Button(self, text="Log Out",
                            command=lambda: controller.show_frame("Login"))
        button1.pack()

class ChefPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'blue')
        label = ttk.Label(self, text="Kitchen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        button1 = ttk.Button(self, text="Log Out",
                            command=lambda: controller.show_frame("Login"))
        button1.pack()

