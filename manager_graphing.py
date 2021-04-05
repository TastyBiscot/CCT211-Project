import tkinter as tk
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv('All_Orders_2021-04-05.csv') #reads file stores into dataframe


#result = df.sort_index(axis=1) #New dataframe with flipped data by y axis
print(df)
df2 = DataFrame(df,columns=['Seated','Time'])
df3 = DataFrame(df,columns=['Table','Time'])

print(df3)
#df3.plot.scatter(  grid = True, figsize=(10,5), ylabel='Vaccinations by %', xlabel = 'Years', title = "time table" , x = 'Table', y='Time')


"""
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Table'],df3['Time'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Seated']) 
ax3.set_xlabel('Table')
ax3.set_title('Table VS Time')
"""
LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.geometry("640x480")

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,bg = 'blue')
        label = tk.Label(self, text="Time VS Seated Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
       
        
        
        
        figure2 = plt.Figure(figsize=(5,4), dpi=100)
        ax2 = figure2.add_subplot(111)
        ax2.scatter(df2['Seated'],df2['Time'], color = 'g')
        scatter2 = FigureCanvasTkAgg(figure2, self) 
        scatter2.get_tk_widget().pack(fill=tk.BOTH)
        ax2.legend(['Seated']) 
        ax2.set_xlabel('Table')
        ax2.set_title('Time VS Seated')
        
        button = tk.Button(self, text="Visit Table VS Time",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()        
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'blue')
        label = tk.Label(self, text="Table VS Time Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        figure3 = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(df3['Table'],df3['Time'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3, self) 
        scatter3.get_tk_widget().pack(fill=tk.BOTH)
        ax3.legend(['Seated']) 
        ax3.set_xlabel('Table')
        ax3.set_title('Table VS Time')
        
        
        button1 = tk.Button(self, text="Visit Seated VS Time",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

     
        
        
        



        


app = SeaofBTCapp()
app.mainloop()
