from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv

# Code follows the lab on treeview
class Chef(tk.Frame):
    #Chef class takes in a csv file that is created by the server
    #It then allows the chef to select items it has finished making
    #Chef will hit complete and the order will be moved to a new completed csv

    def __init__(self, parent, controller, quecsv, Endcsv):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.quecsv = quecsv
        self.Endcsv = Endcsv

        self.s = ttk.Style()
        self.s.theme_use("clam")
        self.TableMargin = Frame(self)
        self.TableMargin.pack(side= TOP,fill="both", expand = True)
        self.currentitem = None

        self.scrollbarx = Scrollbar(self.TableMargin, orient =HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient =VERTICAL)

        # start creating treeview
        self.treeview = ttk.Treeview(self.TableMargin,selectmode= 'none')
        self.treeview['columns'] = ('date','table','server','seated','size','crust','sauce','topping1','topping2','topping3')

        self.treeview.column('#0', minwidth = 10, width = 100) #0
        self.treeview.column('#1', minwidth = 10, width = 100)
        self.treeview.column('#2', minwidth = 10, width = 100)
        self.treeview.column('#3', minwidth = 10, width = 100)
        self.treeview.column('#4', minwidth = 10, width = 100)
        self.treeview.column('#5', minwidth = 10, width = 100)
        self.treeview.column('#6', minwidth = 10, width = 100)
        self.treeview.column('#7', minwidth = 10, width = 100)
        self.treeview.column('#8', minwidth = 10, width = 100)
        self.treeview.column('#9', minwidth = 10, width = 100)
        self.treeview.column('#10', minwidth = 10, width = 100)

        self.treeview.heading('#0', text = 'Time')
        self.treeview.heading('date', text = 'Date')
        self.treeview.heading('table', text = 'Table #')
        self.treeview.heading('server',text = 'Server name')
        self.treeview.heading('seated', text = 'seated')
        self.treeview.heading('size', text = 'size ')
        self.treeview.heading('crust',text = 'crust ')
        self.treeview.heading('sauce', text = 'sauce')
        self.treeview.heading('topping1', text = 'topping1')
        self.treeview.heading('topping2',text = 'topping2')
        self.treeview.heading('topping3',text = 'topping3')

        self.scrollbarx.config(command=self.treeview.xview)
        self.scrollbarx.pack(side = BOTTOM, fill=X)
        self.scrollbary.config(command=self.treeview.yview)
        self.scrollbary.pack(side = RIGHT, fill=Y)

        self.treeview.pack(expand = True, fill =BOTH)
        self.read_file()

        self.treeview.bind('<Button-1>', self.select)

        self.button2 = ttk.Button(self, text="Back", command=self.back)

        self.button2.pack(side = 'right',pady=20,padx=20)

        self.button = ttk.Button(self, text="Completed", state=DISABLED,command=self.save)

        self.button.pack(side = 'left',pady=20,padx=20)


        #self.selected = []

    def select(self, event):
        #focus helps select the current item
        self.currentitem = self.treeview.focus()
        p = self.treeview.item(self.currentitem)
        if len(p['values']) >= 10:
            self.button.config(state=NORMAL)
        else:
            self.currentitem = None

    def print_selected(self):
        print(self.treeview.item(self.curItem)['values'])

    def save(self):
        #Code saves selected item and sends it into new csv, then is updated and deleted from treeview
        with open(self.Endcsv, 'a', newline='') as f:
            writer = csv.writer(f)
            Id = self.treeview.item(self.currentitem)
            writer.writerow([Id["values"][0],Id["text"],Id["values"][2],Id["values"][1],Id["values"][3],Id["values"][4],Id["values"][5],Id["values"][6],Id["values"][7],Id["values"][8],Id["values"][9]])

        #DELETED
        self.treeview.delete(self.currentitem)
        #rewritten current form
        with open(self.quecsv,'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date","Time","Server","Table","Seated","Size","Crust","Sauce","Topping 1","Topping 2", "Topping 3"])
            for i in self.treeview.get_children():
                #if self.currentitem  != self.treeview.item(i):
                Id = self.treeview.item(i)
                writer.writerow([Id["values"][0],Id["text"],Id["values"][2],Id["values"][1],Id["values"][3],Id["values"][4],Id["values"][5],Id["values"][6],Id["values"][7],Id["values"][8],Id["values"][9]])
        #self.currentitem = None
        self.button.config(state=DISABLED)

    def read_file(self):
        #opens and reads the csv to be put into treeview
        with open(self.quecsv,encoding='cp1252') as f:
            reader = csv.DictReader(f, delimiter=',',)
            for row in reader:
                date = row['Date']
                a = row['Time']
                b = row['Table']
                c = row["Server"]
                d = row['Seated']
                e = row['Size']
                f = row["Crust"]
                g = row['Sauce']
                h = row['Topping 1']
                i = row["Topping 2"]
                j = row["Topping 3"]
                self.treeview.insert("", 'end', text = a, values=(date,b,c,d,e,f,g,h,i,j))

    def back(self):
        #returns
        self.button.config(state=DISABLED)
        self.controller.show_frame('Login')


#============================INITIALIZATION==============================
if __name__ == '__main__':
    root = Tk()
    root.geometry("900x600")
    root.title("Import CSV File To Tkinter Table")
    root.s = ttk.Style()
    root.s.theme_use("clam")
    quecsv = "All_Orders_2021-04-10.csv"
    Endcsv = 'All_Completed_Orders.csv'
    app = CSV_Reader(root)
    app.pack(expand = True, fill= BOTH)
    root.mainloop()
