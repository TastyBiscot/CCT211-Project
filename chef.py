from tkinter import *
import csv

class Chef:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1200x900')
        self.root.title('Chef')
        self.root.configure(background = 'black')
        self.initGUI()
        self.root.mainloop()
    
    def initGUI(self):
        
        self.label_orders = Label(self.root, text = 'Orders', width = 10, font = 'Times 50 bold', bg = 'black', fg = 'green')
        self.label_orders.pack(pady = 20)
        
        #Order Queue Title 
        self.label_order_queue = Label(self.root, text = 'Order Queue', width = 25, font = 'Times 30 bold', bg = 'red', fg = 'white')
        self.label_order_queue.place(x = 200, y = 150)
        

        #Orders Labels and Buttons
        self.label_order1 = Label(self.root, text = self.order_name, width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order1.place(x = 200, y = 192)
        
        self.button_order1 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command1)
        self.button_order1.place(x = 449, y = 192)
        
        self.label_order2 = Label(self.root, text = 'Order 2', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order2.place(x = 200, y = 223)
        
        self.button_order2 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command2)
        self.button_order2.place(x = 449, y = 223)
        
        self.label_order3 = Label(self.root, text = 'Order 3', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order3.place(x = 200, y = 254)
        
        self.button_order3 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command3)
        self.button_order3.place(x = 449, y = 254)
        
        self.label_order4 = Label(self.root, text = 'Order 4', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order4.place(x = 200, y = 285)
        
        self.button_order4 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command4)
        self.button_order4.place(x = 449, y = 285) 
        
        self.label_order5 = Label(self.root, text = 'Order 5', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order5.place(x = 200, y = 316)
        
        self.button_order5 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command5)
        self.button_order5.place(x = 449, y = 316)         
        
        self.label_order6 = Label(self.root, text = 'Order 6', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order6.place(x = 200, y = 347)
        
        self.button_order6 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command6)
        self.button_order6.place(x = 449, y = 347)
        
        self.label_order7 = Label(self.root, text = 'Order 7', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order7.place(x = 200, y = 378)
        
        self.button_order7 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command7)
        self.button_order7.place(x = 449, y = 378)
        
        self.label_order8 = Label(self.root, text = 'Order 8', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order8.place(x = 200, y = 409)
        
        self.button_order8 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command8)
        self.button_order8.place(x = 449, y = 409)
        
        self.label_order9 = Label(self.root, text = 'Order 9', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order9.place(x = 200, y = 440)
        
        self.button_order9 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command9)
        self.button_order9.place(x = 449, y = 440)
        
        self.label_order10 = Label(self.root, text = 'Order 10', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order10.place(x = 200, y = 471)
        
        self.button_order10 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command10)
        self.button_order10.place(x = 449, y = 471)
        
        self.label_order11 = Label(self.root, text = 'Order 11', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order11.place(x = 200, y = 502)
        
        self.button_order11 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command11)
        self.button_order11.place(x = 449, y = 502)
        
        self.label_order12 = Label(self.root, text = 'Order 12', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order12.place(x = 200, y = 533)
        
        self.button_order12 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command12)
        self.button_order12.place(x = 449, y = 533)
        
        self.label_order13 = Label(self.root, text = 'Order 13', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order13.place(x = 200, y = 564)
        
        self.button_order13 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command13)
        self.button_order13.place(x = 449, y = 564)
        
        #Working On Title
        self.label_working = Label(self.root, text = 'Working On', width = 25, font = 'Times 30 bold', bg = 'yellow', fg = 'green')
        self.label_working.place(x = 600, y = 150) 
        
        #Commands
    def start_command1(self):
        self.label_order1.destroy()
        self.button_order1.destroy()
        
        self.label_order1_start = Label(self.root, text = 'Order 1', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order1_start.place(x = 600, y = 192)
        
        self.complete_button1 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command1)
        self.complete_button1.place(x = 849, y = 192)  
        
    def start_command2(self):
        self.label_order2.destroy()
        self.button_order2.destroy()
        
        self.label_order2_start = Label(self.root, text = 'Order 2', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order2_start.place(x = 600, y = 223)
        
        self.complete_button2 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command2)
        self.complete_button2.place(x = 849, y = 223)
        
    def start_command3(self):
        self.label_order3.destroy()
        self.button_order3.destroy()
        
        self.label_order3_start = Label(self.root, text = 'Order 3', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order3_start.place(x = 600, y = 254)
        
        self.complete_button3 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command3)
        self.complete_button3.place(x = 849, y = 254)
        
    def start_command4(self):
        self.label_order4.destroy()
        self.button_order4.destroy()
        
        self.label_order4_start = Label(self.root, text = 'Order 4', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order4_start.place(x = 600, y = 285)
        
        self.complete_button4 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command4)
        self.complete_button4.place(x = 849, y = 285)
        
    def start_command5(self):
        self.label_order5.destroy()
        self.button_order5.destroy()
        
        self.label_order5_start = Label(self.root, text = 'Order 5', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order5_start.place(x = 600, y = 316)
        
        self.complete_button5 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command5)
        self.complete_button5.place(x = 849, y = 316)
        
    def start_command6(self):
        self.label_order6.destroy()
        self.button_order6.destroy()
        
        self.label_order6_start = Label(self.root, text = 'Order 6', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order6_start.place(x = 600, y = 347)
        
        self.complete_button6 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command6)
        self.complete_button6.place(x = 849, y = 347)
        
    def start_command7(self):
        self.label_order7.destroy()
        self.button_order7.destroy()
        
        self.label_order7_start = Label(self.root, text = 'Order 7', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order7_start.place(x = 600, y = 378)
        
        self.complete_button7 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command7)
        self.complete_button7.place(x = 849, y = 378)  
        
    def start_command8(self):
        self.label_order8.destroy()
        self.button_order8.destroy()
        
        self.label_order8_start = Label(self.root, text = 'Order 8', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order8_start.place(x = 600, y = 409)
        
        self.complete_button8 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command8)
        self.complete_button8.place(x = 849, y = 409)  
        
    def start_command9(self):
        self.label_order9.destroy()
        self.button_order9.destroy()
        
        self.label_order9_start = Label(self.root, text = 'Order 9', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order9_start.place(x = 600, y = 440)
        
        self.complete_button9 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command9)
        self.complete_button9.place(x = 849, y = 440)  
        
    def start_command10(self):
        self.label_order10.destroy()
        self.button_order10.destroy()
        
        self.label_order10_start = Label(self.root, text = 'Order 10', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order10_start.place(x = 600, y = 471)
        
        self.complete_button10 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command10)
        self.complete_button10.place(x = 849, y = 471)  
        
    def start_command11(self):
        self.label_order11.destroy()
        self.button_order11.destroy()
        
        self.label_order11_start = Label(self.root, text = 'Order 11', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order11_start.place(x = 600, y = 502)
        
        self.complete_button11 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command11)
        self.complete_button11.place(x = 849, y = 502)  
        
    def start_command12(self):
        self.label_order12.destroy()
        self.button_order12.destroy()
        
        self.label_order12_start = Label(self.root, text = 'Order 12', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order12_start.place(x = 600, y = 533)
        
        self.complete_button12 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command12)
        self.complete_button12.place(x = 849, y = 533)  
        
    def start_command13(self):
        self.label_order13.destroy()
        self.button_order13.destroy()
        
        self.label_order13_start = Label(self.root, text = 'Order 13', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order13_start.place(x = 600, y = 564)
        
        self.complete_button13 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command13)
        self.complete_button13.place(x = 849, y = 564)
        
    def start_command14(self):
        self.label_order14.destroy()
        self.button_order14.destroy()
        
        self.label_order14_start = Label(self.root, text = 'Order 14', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order14_start.place(x = 600, y = 192)
        
        self.complete_button14 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command14)
        self.complete_button14.place(x = 849, y = 192)    
        
    def start_command15(self):
        self.label_order15.destroy()
        self.button_order15.destroy()
        
        self.label_order15_start = Label(self.root, text = 'Order 15', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order15_start.place(x = 600, y = 223)
        
        self.complete_button15 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command15)
        self.complete_button15.place(x = 849, y = 223)    
        
    def start_command16(self):
        self.label_order16.destroy()
        self.button_order16.destroy()
        
        self.label_order16_start = Label(self.root, text = 'Order 16', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order16_start.place(x = 600, y = 254)
        
        self.complete_button16 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command16)
        self.complete_button16.place(x = 849, y = 254)    
    
    def start_command17(self):
        self.label_order17.destroy()
        self.button_order17.destroy()
        
        self.label_order17_start = Label(self.root, text = 'Order 17', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order17_start.place(x = 600, y = 285)
        
        self.complete_button17 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command17)
        self.complete_button17.place(x = 849, y = 285)
        
    def start_command18(self):
        self.label_order18.destroy()
        self.button_order18.destroy()
        
        self.label_order18_start = Label(self.root, text = 'Order 18', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order18_start.place(x = 600, y = 316)
        
        self.complete_button18 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command18)
        self.complete_button18.place(x = 849, y = 316)    
        
    def start_command19(self):
        self.label_order19.destroy()
        self.button_order19.destroy()
        
        self.label_order19_start = Label(self.root, text = 'Order 19', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order19_start.place(x = 600, y = 347)
        
        self.complete_button19 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command19)
        self.complete_button19.place(x = 849, y = 347)
        
    def start_command20(self):
        self.label_order20.destroy()
        self.button_order20.destroy()
        
        self.label_order20_start = Label(self.root, text = 'Order 20', width = 25, font = 'Times 20 bold', bg = 'yellow', fg = 'green')
        self.label_order20_start.place(x = 600, y = 378)
        
        self.complete_button20 = Button(self.root, text = 'Complete', width = 12, font = 'Times 15 bold',bg = 'yellow', fg = 'green', command = self.complete_command20)
        self.complete_button20.place(x = 849, y = 378)      
    
    def complete_command1(self):
        self.label_order1_start.destroy()
        self.complete_button1.destroy()
        
        self.label_order14 = Label(self.root, text = 'Order 14', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order14.place(x = 200, y = 192)
        
        self.button_order14 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command14)
        self.button_order14.place(x = 449, y = 192)  
        
    def complete_command2(self):
        self.label_order2_start.destroy()
        self.complete_button2.destroy()
        
        self.label_order15 = Label(self.root, text = 'Order 15', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order15.place(x = 200, y = 223)
        
        self.button_order15 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command15)
        self.button_order15.place(x = 449, y = 223)    
        
    def complete_command3(self):
        self.label_order3_start.destroy()
        self.complete_button3.destroy()
        
        self.label_order16 = Label(self.root, text = 'Order 16', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order16.place(x = 200, y = 254)
        
        self.button_order16 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command16)
        self.button_order16.place(x = 449, y = 254)  
        
    def complete_command4(self):
        self.label_order4_start.destroy()
        self.complete_button4.destroy()
        
        self.label_order17 = Label(self.root, text = 'Order 17', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order17.place(x = 200, y = 285)
        
        self.button_order17 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command17)
        self.button_order17.place(x = 449, y = 285)  
        
    def complete_command5(self):
        self.label_order5_start.destroy()
        self.complete_button5.destroy()
        
        self.label_order18 = Label(self.root, text = 'Order 18', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order18.place(x = 200, y = 316)
        
        self.button_order18 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command18)
        self.button_order18.place(x = 449, y = 316)    
        
    def complete_command6(self):
        self.label_order6_start.destroy()
        self.complete_button6.destroy()
        
        self.label_order19 = Label(self.root, text = 'Order 19', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order19.place(x = 200, y = 347)
        
        self.button_order19 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command19)
        self.button_order19.place(x = 449, y = 347) 
        
    def complete_command7(self):
        self.label_order7_start.destroy()
        self.complete_button7.destroy()
        
        self.label_order20 = Label(self.root, text = 'Order 20', width = 25, font = 'Times 20 bold', bg = 'red', fg = 'white')
        self.label_order20.place(x = 200, y = 378)
        
        self.button_order20 = Button(self.root, text = 'Start', width = 12, font = 'Times 15 bold', bg='yellow', fg = 'green', command = self.start_command20)
        self.button_order20.place(x = 449, y = 378)
        
    def complete_command8(self):
        self.label_order8_start.destroy()
        self.complete_button8.destroy()
        
    def complete_command9(self):
        self.label_order9_start.destroy()
        self.complete_button9.destroy()
        
    def complete_command10(self):
        self.label_order10_start.destroy()
        self.complete_button10.destroy()
        
    def complete_command11(self):
        self.label_order11_start.destroy()
        self.complete_button11.destroy()
        
    def complete_command12(self):
        self.label_order12_start.destroy()
        self.complete_button12.destroy() 
        
    def complete_command13(self):
        self.label_order13_start.destroy()
        self.complete_button13.destroy()
        
    def complete_command14(self):
        self.label_order14_start.destroy()
        self.complete_button14.destroy()
        
    def complete_command15(self):
        self.label_order15_start.destroy()
        self.complete_button15.destroy()
        
    def complete_command16(self):
        self.label_order16_start.destroy()
        self.complete_button16.destroy()
        
    def complete_command17(self):
        self.label_order17_start.destroy()
        self.complete_button17.destroy()  
        
    def complete_command18(self):
        self.label_order18_start.destroy()
        self.complete_button18.destroy()
        
    def complete_command19(self):
        self.label_order19_start.destroy()
        self.complete_button19.destroy()
        
    def complete_command20(self):
        self.label_order20_start.destroy()
        self.complete_button20.destroy()       
    
    
    def read_file(self):
        global order_name
        with open('All_Orders.csv') as csvfile:
            read = csv.reader(csvfile, delimiter = ',')
            for row in read:
                order_name = row['Order Name']
                



if __name__ == '__main__':
    app = Chef()