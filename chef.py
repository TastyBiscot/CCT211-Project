from tkinter import *

class Chef:
    def __init__(self, window):
        self.window = window
        window.title('Chef')
        window.geometry('1200x900')
        window.configure(background = 'black')
        
        self.label_orders = Label(window, text = 'Orders', width = 10, font = 'Times 50 bold', bg = 'black', fg = 'green')
        self.label_orders.pack(pady = 20)
        
        #Order Queue Title 
        self.label_order_queue = Label(window, text = 'Order Queue', width = 25, font = 'Times 30 bold', bg = 'red', fg = 'white')
        self.label_order_queue.place(x = 50, y = 150)
        
        #Orders Labels and Buttons
        self.label_order1 = Label(window, text = 'Order 1', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order1.place(x = 50, y = 192)
        
        self.button_order1 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order1.place(x = 299, y = 192)
        
        self.label_order2 = Label(window, text = 'Order 2', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order2.place(x = 50, y = 223)
        
        self.button_order2 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order2.place(x = 299, y = 223)
        
        self.label_order3 = Label(window, text = 'Order 3', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order3.place(x = 50, y = 254)
        
        self.button_order3 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order3.place(x = 299, y = 254)
        
        self.label_order4 = Label(window, text = 'Order 4', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order4.place(x = 50, y = 285)
        
        self.button_order4 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order4.place(x = 299, y = 285) 
        
        self.label_order5 = Label(window, text = 'Order 5', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order5.place(x = 50, y = 316)
        
        self.button_order5 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order5.place(x = 299, y = 316)         
        
        self.label_order6 = Label(window, text = 'Order 6', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order6.place(x = 50, y = 347)
        
        self.button_order6 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order6.place(x = 299, y = 347)
        
        self.label_order7 = Label(window, text = 'Order 7', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order7.place(x = 50, y = 378)
        
        self.button_order7 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order7.place(x = 299, y = 378)  
        
        self.label_order8 = Label(window, text = 'Order 8', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order8.place(x = 50, y = 409)
        
        self.button_order8 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order8.place(x = 299, y = 409)
        
        self.label_order9 = Label(window, text = 'Order 9', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order9.place(x = 50, y = 440)
        
        self.button_order9 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order9.place(x = 299, y = 440)
        
        self.label_order10 = Label(window, text = 'Order 10', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order10.place(x = 50, y = 471)
        
        self.button_order10 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order10.place(x = 299, y = 471)
        
        self.label_order11 = Label(window, text = 'Order 11', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order11.place(x = 50, y = 502)
        
        self.button_order11 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order11.place(x = 299, y = 502)
        
        self.label_order12 = Label(window, text = 'Order 12', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order12.place(x = 50, y = 533)
        
        self.button_order12 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order12.place(x = 299, y = 533)
        
        self.label_order13 = Label(window, text = 'Order 13', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order13.place(x = 50, y = 564)
        
        self.button_order13 = Button(window, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green')
        self.button_order13.place(x = 299, y = 564)        
        
        #Working On Title
        self.label_working = Label(window, text = 'Working On', width = 25, font = 'Times 30 bold', bg = 'yellow', fg = 'green')
        self.label_working.place(x = 450, y = 150)
        
        #Working on Orders and Complete buttons
        self.working_order1 = Label(window, text = 'Order 1', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order1.place(x = 450, y = 192)
        
        self.complete_order1 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order1.place(x = 699, y = 192)
        
        self.working_order2 = Label(window, text = 'Order 2', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order2.place(x = 450, y = 223)
        
        self.complete_order2 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order2.place(x = 699, y = 223)        
        
        self.working_order3 = Label(window, text = 'Order 3', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order3.place(x = 450, y = 254)
        
        self.complete_order3 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order3.place(x = 699, y = 254)
        
        self.working_order4 = Label(window, text = 'Order 4', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order4.place(x = 450, y = 285)
        
        self.complete_order4 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order4.place(x = 699, y = 285)  
        
        self.working_order5 = Label(window, text = 'Order 5', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order5.place(x = 450, y = 316)
        
        self.complete_order5 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order5.place(x = 699, y = 316)  
        
        self.working_order6 = Label(window, text = 'Order 6', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order6.place(x = 450, y = 347)
        
        self.complete_order6 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order6.place(x = 699, y = 347)
        
        self.working_order7 = Label(window, text = 'Order 7', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order7.place(x = 450, y = 378)
        
        self.complete_order7 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order7.place(x = 699, y = 378)
        
        self.working_order8 = Label(window, text = 'Order 8', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order8.place(x = 450, y = 409)
        
        self.complete_order8 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order8.place(x = 699, y = 409)  
        
        self.working_order9 = Label(window, text = 'Order 9', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order9.place(x = 450, y = 440)
        
        self.complete_order9 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order9.place(x = 699, y = 440) 
        
        self.working_order10 = Label(window, text = 'Order 10', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order10.place(x = 450, y = 471)
        
        self.complete_order10 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order10.place(x = 699, y = 471) 
        
        self.working_order11 = Label(window, text = 'Order 11', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order11.place(x = 450, y = 502)
        
        self.complete_order11 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order11.place(x = 699, y = 502) 
        
        self.working_order12 = Label(window, text = 'Order 12', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order12.place(x = 450, y = 533)
        
        self.complete_order12 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order12.place(x = 699, y = 533)  
        
        self.working_order13 = Label(window, text = 'Order 13', bg = 'yellow', fg = 'green', font = 'Times 20 bold', width = 25)
        self.working_order13.place(x = 450, y = 564)
        
        self.complete_order13 = Button(window, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green')
        self.complete_order13.place(x = 699, y = 564)         
        
        #Ready Title
        self.label_ready = Label(window, text = 'Ready', width = 15, font = 'Times 30 bold', bg = 'green', fg = 'white')
        self.label_ready.place(x = 850, y = 150)   
        
        #Ready Order labels and Serve buttons
        self.ready_order1 = Label(window, text = 'Order 1', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order1.place(x = 850, y = 192)
        
        self.remove_button1 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button1.place(x = 1000, y = 192)
        
        self.ready_order2 = Label(window, text = 'Order 2', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order2.place(x = 850, y = 223)
        
        self.remove_button2 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button2.place(x = 1000, y = 223)
        
        self.ready_order3 = Label(window, text = 'Order 3', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order3.place(x = 850, y = 254)
        
        self.remove_button3 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button3.place(x = 1000, y = 254)
        
        self.ready_order4 = Label(window, text = 'Order 4', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order4.place(x = 850, y = 285)
        
        self.remove_button4 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button4.place(x = 1000, y = 285)   
        
        self.ready_order4 = Label(window, text = 'Order 4', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order4.place(x = 850, y = 285)
        
        self.remove_button4 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button4.place(x = 1000, y = 285)  
        
        self.ready_order5 = Label(window, text = 'Order 5', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order5.place(x = 850, y = 316)
        
        self.remove_button5 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button5.place(x = 1000, y = 316)    
        
        self.ready_order6 = Label(window, text = 'Order 6', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order6.place(x = 850, y = 347)
        
        self.remove_button6 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button6.place(x = 1000, y = 347) 
        
        self.ready_order7 = Label(window, text = 'Order 7', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order7.place(x = 850, y = 378)
        
        self.remove_button7 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button7.place(x = 1000, y = 378)  
        
        self.ready_order8 = Label(window, text = 'Order 8', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order8.place(x = 850, y = 409)
        
        self.remove_button8 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button8.place(x = 1000, y = 409)         
        
        self.ready_order9 = Label(window, text = 'Order 9', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order9.place(x = 850, y = 440)
        
        self.remove_button9 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button9.place(x = 1000, y = 440) 
        
        self.ready_order10 = Label(window, text = 'Order 10', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order10.place(x = 850, y = 471)
        
        self.remove_button10 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button10.place(x = 1000, y = 471) 
        
        self.ready_order11 = Label(window, text = 'Order 11', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order11.place(x = 850, y = 502)
        
        self.remove_button11 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button11.place(x = 1000, y = 502)   
        
        self.ready_order12 = Label(window, text = 'Order 12', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order12.place(x = 850, y = 533)
        
        self.remove_button12 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button12.place(x = 1000, y = 533)  
        
        self.ready_order13 = Label(window, text = 'Order 13', bg = 'green', fg = 'white', font = 'Times 20 bold', width = 15)
        self.ready_order13.place(x = 850, y = 564)
        
        self.remove_button13 = Button(window, text = 'Serve', width = 6, font = 'Times 15 bold',bg = 'green', fg = 'green')
        self.remove_button13.place(x = 1000, y = 564)         


root = Tk()
chef_gui = Chef(root)
root.mainloop()