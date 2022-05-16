# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:12:46 2022

@author: Swasti
"""

from tkinter import*

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

enter_no = Enter(root)
label1 = Label(root, text = "Fibonacci Series : ")

label2 = Label(root, text = "Fibonacci Sum : ")

def Fibonacci():
    input_no = int(enter_get.no())
    
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    
    while(counter <= input_no) : 
        label1["text"] += str(sum) + " "
        label2["text"] += "Fibonacci Sum : " + str(sum2) 
        counter = counter + 1 
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
        
        
enter_no.pack()

btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci)

btn.pack()

label1.pack()
label2.pack()

root.mainloop()