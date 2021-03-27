from tkinter import *

class Inventory:
    def __init__(self, window):
        self.window = window
        window.title('Inventory')
        window.geometry('1200x900')
        window.configure(background = 'light blue') 
        self.amount1 = 123456
        self.amount2 = 123456
        self.amount3 = 123456
        self.amount4 = 123456
        self.amount5 = 123456
        self.amount6 = 123456
        self.amount7 = 123456
        self.amount8 = 123456
        self.amount9 = 123456
        self.amount10 = 123456
        self.amount11 = 123456
        self.amount12 = 123456
        self.amount13 = 123456
        self.amount14 = 123456
        self.amount15 = 123456
        self.amount16 = 123456
        self.amount17 = 123456
        self.amount18 = 123456
        self.amount19 = 123456
        self.amount20 = 123456
        
        self.label_inventory = Label(window, text = 'Inventory', fg = 'black', bg = 'light blue', font = 'Times 50 bold')
        self.label_inventory.pack(pady = 20)
        
        #Inventory name labels
        self.label_item1 = Label(window, text = 'Item 1:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item1.place(x = 50, y = 150)
        
        self.label_item2 = Label(window, text = 'Item 2:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item2.place(x = 50, y = 200) 
        
        self.label_item3 = Label(window, text = 'Item 3:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item3.place(x = 50, y = 250)    
        
        self.label_item4 = Label(window, text = 'Item 4:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item4.place(x = 50, y = 300)
        
        self.label_item5 = Label(window, text = 'Item 5:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item5.place(x = 50, y = 350)
        
        self.label_item6 = Label(window, text = 'Item 6:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item6.place(x = 50, y = 400)
        
        self.label_item7 = Label(window, text = 'Item 7:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item7.place(x = 50, y = 450)
        
        self.label_item8 = Label(window, text = 'Item 8:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item8.place(x = 50, y = 500)
        
        self.label_item9 = Label(window, text = 'Item 9:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item9.place(x = 50, y = 550)        
        
        self.label_item10 = Label(window, text = 'Item 10:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item10.place(x = 50, y = 600)
        
        self.label_item11 = Label(window, text = 'Item 11:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item11.place(x = 650, y = 150)
        
        self.label_item12 = Label(window, text = 'Item 12:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item12.place(x = 650, y = 200)
        
        self.label_item13 = Label(window, text = 'Item 13:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item13.place(x = 650, y = 250)
        
        self.label_item14 = Label(window, text = 'Item 14:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item14.place(x = 650, y = 300)
        
        self.label_item15 = Label(window, text = 'Item 15:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item15.place(x = 650, y = 350)
        
        self.label_item16 = Label(window, text = 'Item 16:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item16.place(x = 650, y = 400)
        
        self.label_item17 = Label(window, text = 'Item 17:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item17.place(x = 650, y = 450)
        
        self.label_item18 = Label(window, text = 'Item 18:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item18.place(x = 650, y = 500)
        
        self.label_item19 = Label(window, text = 'Item 19:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item19.place(x = 650, y = 550)
        
        self.label_item20 = Label(window, text = 'Item 20:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item20.place(x = 650, y = 600)    
        
        #Inventory amount
        self.inventory_amount1 = Label(window, text = self.amount1, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount1.place(x = 350, y = 150)
        
        self.inventory_amount2 = Label(window, text = self.amount2, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount2.place(x = 350, y = 200)   
        
        self.inventory_amount3 = Label(window, text = self.amount3, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount3.place(x = 350, y = 250)
        
        self.inventory_amount4 = Label(window, text = self.amount4, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount4.place(x = 350, y = 300)
        
        self.inventory_amount5 = Label(window, text = self.amount5, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount5.place(x = 350, y = 350)
        
        self.inventory_amount6 = Label(window, text = self.amount6, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount6.place(x = 350, y = 400)
        
        self.inventory_amount7 = Label(window, text = self.amount7, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount7.place(x = 350, y = 450)
        
        self.inventory_amount8 = Label(window, text = self.amount8, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount8.place(x = 350, y = 500)
        
        self.inventory_amount9 = Label(window, text = self.amount9, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount9.place(x = 350, y = 550)
        
        self.inventory_amount10 = Label(window, text = self.amount10, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount10.place(x = 350, y = 600)
        
        self.inventory_amount11 = Label(window, text = self.amount11, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount11.place(x = 950, y = 150)  
        
        self.inventory_amount12 = Label(window, text = self.amount12, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount12.place(x = 950, y = 200)
        
        self.inventory_amount13 = Label(window, text = self.amount13, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount13.place(x = 950, y = 250)
        
        self.inventory_amount14 = Label(window, text = self.amount14, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount14.place(x = 950, y = 300)
        
        self.inventory_amount15 = Label(window, text = self.amount15, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount15.place(x = 950, y = 350)
        
        self.inventory_amount16 = Label(window, text = self.amount16, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount16.place(x = 950, y = 400)
        
        self.inventory_amount17 = Label(window, text = self.amount17, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount17.place(x = 950, y = 450)
        
        self.inventory_amount18 = Label(window, text = self.amount18, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount18.place(x = 950, y = 500)
        
        self.inventory_amount19 = Label(window, text = self.amount19, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount19.place(x = 950, y = 550)
        
        self.inventory_amount20 = Label(window, text = self.amount20, fg = 'black', bg = 'light blue', font = 'Timtes 30 bold')
        self.inventory_amount20.place(x = 950, y = 600)
            
        self.plus_button = Button(window, text = '+', fg = 'black', state = DISABLED)
        self.plus_button.place(x = 500, y = 150)        

root = Tk()
inventory_gui = Inventory(root)
root.mainloop()