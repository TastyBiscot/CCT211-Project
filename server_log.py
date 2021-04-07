import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import os
import csv


#start coding here
class DataRecordForm(tk.Frame): #subclass Frame
    """THe input form for our widgets"""
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs) # init the underlying frame object
        self.inputs = {} #dict to track input widgets
        recordinfo = tk.LabelFrame(self,text = "Table Information") #frame for recordinfo
                                   
        self.inputs['Date'] = LabelInput(recordinfo,"Date",input_var=tk.StringVar())
        self.inputs['Date'].grid(row=0,column=0)
        self.inputs['Date'].columnconfigure(0,weight=1)
        
        self.inputs['Time'] = LabelInput(recordinfo, "Time",input_class = ttk.Combobox, input_var = tk.StringVar(), input_args={"values":["8:00","12:00","16:00","20:00"]})
        self.inputs['Time'].grid(row = 0, column = 1)
        self.inputs['Time'].columnconfigure(0,weight=1)
        
        self.inputs['Server'] = LabelInput(
            recordinfo, "Server",
            input_var=tk.StringVar()
        )
        self.inputs['Server'].grid(row=0, column=2)
        self.inputs['Server'].columnconfigure(0,weight=1)
        

       # line 2
        self.inputs['Table'] = LabelInput(
            recordinfo, "Table",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["1", "2", "3", "4", "5","6","7","8"]}
        )
        self.inputs['Table'].grid(row=1, column=0)
        self.inputs['Table'].columnconfigure(0,weight=1)
        
        self.inputs['Seated'] = LabelInput(
            recordinfo, "Seated",
            input_class=ttk.Combobox,
            input_var=tk.IntVar(),
            input_args={"values": list(range(1, 5))}
        )
        self.inputs['Seated'].grid(row=1, column=1)
        self.inputs['Seated'].columnconfigure(0,weight=1)
             
        
        recordinfo.grid(row=0, column=0, sticky=(tk.W + tk.E))
        recordinfo.columnconfigure(0,weight=1)
        
        enviromentinfo = tk.LabelFrame(self,text="Order Info")
        
        self.inputs['Size'] = LabelInput(
            enviromentinfo, "Size",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["Small", "Medium", "Large","X-Large"]}
        )        
        
        
        self.inputs['Size'].grid(row=0,column = 0)
        self.inputs['Size'].columnconfigure(0,weight=1)
        
        self.inputs['Crust'] = LabelInput(
            enviromentinfo, "Crust",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["New York", "Chicago", "Cheese Filled"]}
        )        
        
        self.inputs['Crust'].grid(row=0,column = 1)
        self.inputs['Crust'].columnconfigure(0,weight=1)
        
        self.inputs['Sauce'] = LabelInput(
            enviromentinfo, "Sauce",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["None", "Little", "Normal","Extra"]}
        )        
        self.inputs['Sauce'].grid(row=0,column = 2)
        self.inputs['Sauce'].columnconfigure(0,weight=1)
        
        self.inputs['Topping 1'] = LabelInput(
            enviromentinfo, "Topping 1",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["Pepperoni", "Sausage", "Bacon","Pepper","Pineapple","Onion","Mushroom","Spinach"]}
        )        
        self.inputs['Topping 1'].grid(row=1,column = 0)
        self.inputs['Topping 1'].columnconfigure(0,weight=1)
        
        self.inputs['Topping 2'] = LabelInput(
            enviromentinfo, "Topping 2",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["Pepperoni", "Sausage", "Bacon","Pepper","Pineapple","Onion","Mushroom","Spinach"]}
        )        
        self.inputs['Topping 2'].grid(row=1,column = 1)
        self.inputs['Topping 2'].columnconfigure(0,weight=1)
        
        self.inputs['Topping 3'] = LabelInput(
            enviromentinfo, "Topping 3",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["Pepperoni", "Sausage", "Bacon","Pepper","Pineapple","Onion","Mushroom","Spinach"]}
        )        
        self.inputs['Topping 3'].grid(row=1,column = 2)        
        self.inputs['Topping 3'].columnconfigure(0,weight=1)
          
        
        self.inputs['Allergies'] = LabelInput(enviromentinfo,"Allergies", input_class=ttk.Checkbutton,input_var = tk.BooleanVar())
        self.inputs['Allergies'].grid(row=2,column = 0,columnspan=3)
        self.inputs['Allergies'].columnconfigure(0,weight=1)
        
        enviromentinfo.grid(row=2, column=0, sticky="we")
        enviromentinfo.columnconfigure(0,weight=1)
            
        self.inputs['Notes'] = LabelInput(self,"notes", input_class = tk.Text, input_args={"width":75,"height": 10})
        self.inputs['Notes'].grid(sticky=(tk.W+tk.E),row=3,column=0)
        self.inputs['Notes'].columnconfigure(0,weight=1)
        
        
        
        
        self.reset() #remove any tk default values at start
        
    def get(self):
        #loop through instance's inputs objects containing our LabelInput objects and build a new dictionary by calling get() on each variable.
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data
    
    def reset(self):
        #reset to empty fields
        for widget in self.inputs.values():
            widget.set('')
    
class LabelInput(tk.Frame):
    """a widget containting a label and input together. will make building form easier"""
    def __init__(self,parent,label="", input_class=ttk.Entry, input_var=None, input_args=None,label_args=None, **kwargs):
        super().__init__(parent,**kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var
        
        #differentiate way widgets handle variables and label text
        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["text"] = label
            input_args["variable"] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            #self.label.columnconfigure(0,weight=1)
            input_args["textvariable"] = input_var
            
            
        #call inputclass passed into constructor, with input_args dictionary to keyword arguments.
        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))        

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        #taking custom widget and overiding for default expansion(no tk.w,ect)
        super().grid(sticky=sticky, **kwargs)
    
    def get(self):
        #pass along the request to the input or its variable
        try:
            if self.variable:
                return self.variable.get()
            elif type(self.input) == tk.Text:
                return self.input.get('1.0', tk.END)
            else:
                return self.input.get()
        except (TypeError, tk.TclError):
            # happens when numeric fields are empty.
            return ''   
        
    def set(self, value, *args, **kwargs):
        #method abstracts away some of the differences between how various tkinter widgets set their values
        if type(self.variable) == tk.BooleanVar:
                self.variable.set(bool(value))
        elif self.variable:
                self.variable.set(value, *args, **kwargs)
        elif type(self.input) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)
    
        
class Application(tk.Frame):
    "hello world Main application"
    
    def __init__(self, parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)    
        super().__init__(parent,*args,**kwargs)
     
        
        ttk.Label(self,text= "Food Order Form",font = ("TkDefaultFont", 16)).grid(row=0,sticky=(tk.W+tk.E,tk.N,tk.S))
        
        self.recordform = DataRecordForm(self)
        
        self.recordform.grid(row=1,sticky=(tk.W+tk.E,tk.N,tk.S), padx=10)
        self.savebutton = ttk.Button(self,text = "Save",command = self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2,padx=10)
        
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self,textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W+tk.E),row=3,padx=10)
        self.columnconfigure(0,weight=1)
        self.recordform.columnconfigure(0,weight=1)
        
        self.records_saved = 0
        
    def on_save(self):
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "All_Orders_{}.csv".format(datestring)
        newfile = not os.path.exists(filename)

        data = self.recordform.get()

        with open(filename, 'a') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)

        self.records_saved += 1
        self.status.set(
            "{} records saved this session".format(self.records_saved)
        )
        self.recordform.reset()

        
if __name__ == '__main__':
    root = Tk()
    root.title("Food Data Enrty Application")
    root.geometry("800x600")
    root.s = ttk.Style()
    root.s.theme_use("clam")        
    app = Application(root)
    app.pack(expand = True, fill= BOTH)
    root.mainloop()
