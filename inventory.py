from tkinter import *

class Inventory:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1200x900')
        self.root.title('Inventory')
        self.root.configure(background = 'light blue')
        self.initGUI()
        self.root.mainloop()
               
    def initGUI(self):
        global amount
        
        self.amount = [123456, 123456, 123456, 123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456,123456, 123456]
        
        self.label_inventory = Label(self.root, text = 'Inventory', fg = 'black', bg = 'light blue', font = 'Times 50 bold')
        self.label_inventory.pack(pady = 20)
        
        #Inventory name labels
        self.label_item1 = Label(self.root, text = 'Item 1:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item1.place(x = 50, y = 150)
        
        self.label_item2 = Label(self.root, text = 'Item 2:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item2.place(x = 50, y = 200) 
        
        self.label_item3 = Label(self.root, text = 'Item 3:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item3.place(x = 50, y = 250)    
        
        self.label_item4 = Label(self.root, text = 'Item 4:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item4.place(x = 50, y = 300)
        
        self.label_item5 = Label(self.root, text = 'Item 5:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item5.place(x = 50, y = 350)
        
        self.label_item6 = Label(self.root, text = 'Item 6:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item6.place(x = 50, y = 400)
        
        self.label_item7 = Label(self.root, text = 'Item 7:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item7.place(x = 50, y = 450)
        
        self.label_item8 = Label(self.root, text = 'Item 8:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item8.place(x = 50, y = 500)
        
        self.label_item9 = Label(self.root, text = 'Item 9:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item9.place(x = 50, y = 550)        
        
        self.label_item10 = Label(self.root, text = 'Item 10:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item10.place(x = 50, y = 600)
        
        self.label_item11 = Label(self.root, text = 'Item 11:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item11.place(x = 650, y = 150)
        
        self.label_item12 = Label(self.root, text = 'Item 12:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item12.place(x = 650, y = 200)
        
        self.label_item13 = Label(self.root, text = 'Item 13:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item13.place(x = 650, y = 250)
        
        self.label_item14 = Label(self.root, text = 'Item 14:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item14.place(x = 650, y = 300)
        
        self.label_item15 = Label(self.root, text = 'Item 15:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item15.place(x = 650, y = 350)
        
        self.label_item16 = Label(self.root, text = 'Item 16:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item16.place(x = 650, y = 400)
        
        self.label_item17 = Label(self.root, text = 'Item 17:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item17.place(x = 650, y = 450)
        
        self.label_item18 = Label(self.root, text = 'Item 18:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item18.place(x = 650, y = 500)
        
        self.label_item19 = Label(self.root, text = 'Item 19:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item19.place(x = 650, y = 550)
        
        self.label_item20 = Label(self.root, text = 'Item 20:', fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.label_item20.place(x = 650, y = 600)    
        
        #Inventory amount
        self.inventory_amount1 = Label(self.root, text = self.amount[0], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount1.place(x = 350, y = 150)
        
        self.inventory_amount2 = Label(self.root, text = self.amount[1], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount2.place(x = 350, y = 200)   
        
        self.inventory_amount3 = Label(self.root, text = self.amount[2], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount3.place(x = 350, y = 250)
        
        self.inventory_amount4 = Label(self.root, text = self.amount[3], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount4.place(x = 350, y = 300)
        
        self.inventory_amount5 = Label(self.root, text = self.amount[4], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount5.place(x = 350, y = 350)
        
        self.inventory_amount6 = Label(self.root, text = self.amount[5], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount6.place(x = 350, y = 400)
        
        self.inventory_amount7 = Label(self.root, text = self.amount[6], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount7.place(x = 350, y = 450)
        
        self.inventory_amount8 = Label(self.root, text = self.amount[7], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount8.place(x = 350, y = 500)
        
        self.inventory_amount9 = Label(self.root, text = self.amount[8], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount9.place(x = 350, y = 550)
        
        self.inventory_amount10 = Label(self.root, text = self.amount[9], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount10.place(x = 350, y = 600)
        
        self.inventory_amount11 = Label(self.root, text = self.amount[10], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount11.place(x = 950, y = 150)  
        
        self.inventory_amount12 = Label(self.root, text = self.amount[11], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount12.place(x = 950, y = 200)
        
        self.inventory_amount13 = Label(self.root, text = self.amount[12], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount13.place(x = 950, y = 250)
        
        self.inventory_amount14 = Label(self.root, text = self.amount[13], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount14.place(x = 950, y = 300)
        
        self.inventory_amount15 = Label(self.root, text = self.amount[14], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount15.place(x = 950, y = 350)
        
        self.inventory_amount16 = Label(self.root, text = self.amount[15], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount16.place(x = 950, y = 400)
        
        self.inventory_amount17 = Label(self.root, text = self.amount[16], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount17.place(x = 950, y = 450)
        
        self.inventory_amount18 = Label(self.root, text = self.amount[17], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount18.place(x = 950, y = 500)
        
        self.inventory_amount19 = Label(self.root, text = self.amount[18], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount19.place(x = 950, y = 550)
        
        self.inventory_amount20 = Label(self.root, text = self.amount[19], fg = 'black', bg = 'light blue', font = 'Times 30 bold')
        self.inventory_amount20.place(x = 950, y = 600)
        
        #Plus Buttons   
        self.plus_button1 = Button(self.root,text = '+',fg ='black',command = self.increase1)        
        self.plus_button1.place(x = 460, y = 155)
        
        self.plus_button2 = Button(self.root,text = '+',fg ='black',command = self.increase2)        
        self.plus_button2.place(x = 460, y = 205)
        
        self.plus_button3 = Button(self.root,text = '+',fg ='black',command = self.increase3)        
        self.plus_button3.place(x = 460, y = 255)
        
        self.plus_button4 = Button(self.root,text = '+',fg ='black',command = self.increase4)        
        self.plus_button4.place(x = 460, y = 305) 
        
        self.plus_button5 = Button(self.root,text = '+',fg ='black',command = self.increase5)        
        self.plus_button5.place(x = 460, y = 355)   
        
        self.plus_button6 = Button(self.root,text = '+',fg ='black',command = self.increase6)        
        self.plus_button6.place(x = 460, y = 405)
        
        self.plus_button7 = Button(self.root,text = '+',fg ='black',command = self.increase7)        
        self.plus_button7.place(x = 460, y = 455)
        
        self.plus_button8 = Button(self.root,text = '+',fg ='black',command = self.increase8)        
        self.plus_button8.place(x = 460, y = 505)
        
        self.plus_button9 = Button(self.root,text = '+',fg ='black',command = self.increase9)        
        self.plus_button9.place(x = 460, y = 555) 
        
        self.plus_button10 = Button(self.root,text = '+',fg='black',command= self.increase10)        
        self.plus_button10.place(x = 460, y = 605)
        
        self.plus_button11 = Button(self.root,text = '+',fg='black',command= self.increase11)        
        self.plus_button11.place(x = 1055, y = 155)
        
        self.plus_button12 = Button(self.root,text = '+',fg='black',command= self.increase12)        
        self.plus_button12.place(x = 1055, y = 205)
        
        self.plus_button13 = Button(self.root,text = '+',fg='black',command= self.increase13)        
        self.plus_button13.place(x = 1055, y = 255)
        
        self.plus_button14 = Button(self.root,text = '+',fg='black',command= self.increase14)        
        self.plus_button14.place(x = 1055, y = 305) 
        
        self.plus_button15 = Button(self.root,text = '+',fg='black',command= self.increase15)        
        self.plus_button15.place(x = 1055, y = 355)   
        
        self.plus_button16 = Button(self.root,text = '+',fg='black',command= self.increase16)        
        self.plus_button16.place(x = 1055, y = 405)
        
        self.plus_button17 = Button(self.root,text = '+',fg='black',command= self.increase17)        
        self.plus_button17.place(x = 1055, y = 455)
        
        self.plus_button18 = Button(self.root,text = '+',fg='black',command= self.increase18)        
        self.plus_button18.place(x = 1055, y = 505)
        
        self.plus_button19 = Button(self.root,text = '+',fg='black',command= self.increase19)        
        self.plus_button19.place(x = 1055, y = 555) 
        
        self.plus_button20 = Button(self.root,text = '+',fg='black',command= self.increase20)        
        self.plus_button20.place(x = 1055, y = 605)        
        
        #Minus Buttons
        self.minus_button1 = Button(self.root,text = '_',fg = 'black',command = self.decrease1) 
        self.minus_button1.place(x = 300, y = 155)
        
        self.minus_button2 = Button(self.root,text = '_',fg = 'black',command = self.decrease2) 
        self.minus_button2.place(x = 300, y = 205)
        
        self.minus_button3 = Button(self.root,text = '_',fg = 'black',command = self.decrease3) 
        self.minus_button3.place(x = 300, y = 255)
        
        self.minus_button4 = Button(self.root,text = '_',fg = 'black',command = self.decrease4) 
        self.minus_button4.place(x = 300, y = 305)
        
        self.minus_button5 = Button(self.root,text = '_',fg = 'black',command = self.decrease5) 
        self.minus_button5.place(x = 300, y = 355) 
        
        self.minus_button6 = Button(self.root,text = '_',fg = 'black',command = self.decrease6) 
        self.minus_button6.place(x = 300, y = 405)
        
        self.minus_button7 = Button(self.root,text = '_',fg = 'black',command = self.decrease7) 
        self.minus_button7.place(x = 300, y = 455)
        
        self.minus_button8 = Button(self.root,text = '_',fg = 'black',command = self.decrease8) 
        self.minus_button8.place(x = 300, y = 505)
        
        self.minus_button9 = Button(self.root,text = '_',fg = 'black',command = self.decrease9) 
        self.minus_button9.place(x = 300, y = 555)
        
        self.minus_button10 = Button(self.root,text = '_',fg = 'black',command = self.decrease10) 
        self.minus_button10.place(x = 300, y = 605)          
        
        self.minus_button11 = Button(self.root,text = '_',fg = 'black',command = self.decrease11) 
        self.minus_button11.place(x = 895, y = 155)
        
        self.minus_button12 = Button(self.root,text = '_',fg = 'black',command = self.decrease12) 
        self.minus_button12.place(x = 895, y = 205)
        
        self.minus_button13 = Button(self.root,text = '_',fg = 'black',command = self.decrease13) 
        self.minus_button13.place(x = 895, y = 255)
        
        self.minus_button14 = Button(self.root,text = '_',fg = 'black',command = self.decrease14) 
        self.minus_button14.place(x = 895, y = 305)
        
        self.minus_button15 = Button(self.root,text = '_',fg = 'black',command = self.decrease15) 
        self.minus_button15.place(x = 895, y = 355) 
        
        self.minus_button16 = Button(self.root,text = '_',fg = 'black',command = self.decrease16) 
        self.minus_button16.place(x = 895, y = 405)
        
        self.minus_button17 = Button(self.root,text = '_',fg = 'black',command = self.decrease17) 
        self.minus_button17.place(x = 895, y = 455)
        
        self.minus_button18 = Button(self.root,text = '_',fg = 'black',command = self.decrease18) 
        self.minus_button18.place(x = 895, y = 505)
        
        self.minus_button19 = Button(self.root,text = '_',fg = 'black',command = self.decrease19) 
        self.minus_button19.place(x = 895, y = 555)
        
        self.minus_button20 = Button(self.root,text = '_',fg = 'black',command = self.decrease20) 
        self.minus_button20.place(x = 895, y = 605)         
    
    #Increase Commands
    def increase1(self):
        self.inventory_amount1['text'] = self.inventory_amount1['text'] + 1
        
    def increase2(self):
        self.inventory_amount2['text'] = self.inventory_amount2['text'] + 1
        
    def increase3(self):
        self.inventory_amount3['text'] = self.inventory_amount3['text'] + 1
        
    def increase4(self):
        self.inventory_amount4['text'] = self.inventory_amount4['text'] + 1
        
    def increase5(self):
        self.inventory_amount5['text'] = self.inventory_amount5['text'] + 1
        
    def increase6(self):
        self.inventory_amount6['text'] = self.inventory_amount6['text'] + 1
        
    def increase7(self):
        self.inventory_amount7['text'] = self.inventory_amount7['text'] + 1
        
    def increase8(self):
        self.inventory_amount8['text'] = self.inventory_amount8['text'] + 1
        
    def increase9(self):
        self.inventory_amount9['text'] = self.inventory_amount9['text'] + 1
        
    def increase10(self):
        self.inventory_amount10['text'] = self.inventory_amount10['text'] + 1  
        
    def increase11(self):
        self.inventory_amount11['text'] = self.inventory_amount11['text'] + 1
        
    def increase12(self):
        self.inventory_amount12['text'] = self.inventory_amount12['text'] + 1
        
    def increase13(self):
        self.inventory_amount13['text'] = self.inventory_amount13['text'] + 1
        
    def increase14(self):
        self.inventory_amount14['text'] = self.inventory_amount14['text'] + 1
        
    def increase15(self):
        self.inventory_amount15['text'] = self.inventory_amount15['text'] + 1
        
    def increase16(self):
        self.inventory_amount16['text'] = self.inventory_amount16['text'] + 1
        
    def increase17(self):
        self.inventory_amount17['text'] = self.inventory_amount17['text'] + 1
        
    def increase18(self):
        self.inventory_amount18['text'] = self.inventory_amount18['text'] + 1
        
    def increase19(self):
        self.inventory_amount19['text'] = self.inventory_amount19['text'] + 1
        
    def increase20(self):
        self.inventory_amount20['text'] = self.inventory_amount20['text'] + 1    
        
               
    #Decrease commands
    def decrease1(self):
        self.inventory_amount1['text'] = self.inventory_amount1['text'] - 1
        
    def decrease2(self):
        self.inventory_amount2['text'] = self.inventory_amount2['text'] - 1
        
    def decrease3(self):
        self.inventory_amount3['text'] = self.inventory_amount3['text'] - 1
        
    def decrease4(self):
        self.inventory_amount4['text'] = self.inventory_amount4['text'] - 1
        
    def decrease5(self):
        self.inventory_amount5['text'] = self.inventory_amount5['text'] - 1
        
    def decrease6(self):
        self.inventory_amount6['text'] = self.inventory_amount6['text'] - 1
        
    def decrease7(self):
        self.inventory_amount7['text'] = self.inventory_amount7['text'] - 1
        
    def decrease8(self):
        self.inventory_amount8['text'] = self.inventory_amount8['text'] - 1
        
    def decrease9(self):
        self.inventory_amount9['text'] = self.inventory_amount9['text'] - 1
        
    def decrease10(self):
        self.inventory_amount10['text'] = self.inventory_amount10['text'] - 1 
        
    def decrease11(self):
        self.inventory_amount11['text'] = self.inventory_amount11['text'] - 1
        
    def decrease12(self):
        self.inventory_amount12['text'] = self.inventory_amount12['text'] - 1
        
    def decrease13(self):
        self.inventory_amount13['text'] = self.inventory_amount13['text'] - 1
        
    def decrease14(self):
        self.inventory_amount14['text'] = self.inventory_amount14['text'] - 1
        
    def decrease15(self):
        self.inventory_amount15['text'] = self.inventory_amount15['text'] - 1  
        
    def decrease16(self):
        self.inventory_amount16['text'] = self.inventory_amount16['text'] - 1
        
    def decrease17(self):
        self.inventory_amount17['text'] = self.inventory_amount17['text'] - 1
        
    def decrease18(self):
        self.inventory_amount18['text'] = self.inventory_amount18['text'] - 1
        
    def decrease19(self):
        self.inventory_amount19['text'] = self.inventory_amount19['text'] - 1
        
    def decrease20(self):
        self.inventory_amount20['text'] = self.inventory_amount20['text'] - 1     
        
        
            
            
            

if __name__ == '__main__':
    app = Inventory()