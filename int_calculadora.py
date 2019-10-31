from tkinter import *
root = Tk()

#frame de cima
Tops = Frame(root, width = 300, height= 20, bd= 4, relief= 'raise')
Tops.pack(side = TOP)

#frame debaixo
Below = Frame(root, width = 300, height = 300, bd = 4, relief= 'raise')
Below.pack(side=BOTTOM)



#Funções

def btn_Click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btn_Clear():
    global operator
    operator = ''
    text_Input.set('')

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

operator = ''
text_Input = StringVar()

#entrada de numeros, se relaciona com o frame de cima.
txtDisplay = Entry(Tops, font = ('arial', 18, 'bold'), textvariable = text_Input, width = 21, bd = 3, justify = 'right')
txtDisplay.grid(row=0,column=0)

#botoes: números
btn0 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '0', command = lambda: btn_Click(0)).grid(row=3,column=1)
btn1 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '1', command = lambda: btn_Click(1)).grid(row=0,column=0)
btn2 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '2', command = lambda: btn_Click(2)).grid(row=0,column=1)
btn3 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '3', command = lambda: btn_Click(3)).grid(row=0,column=2)
btn4 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '4', command = lambda: btn_Click(4)).grid(row=1,column=0)
btn5 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '5', command = lambda: btn_Click(5)).grid(row=1,column=1)
btn6 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '6', command = lambda: btn_Click(6)).grid(row=1,column=2)
btn7 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '7', command = lambda: btn_Click(7)).grid(row=2,column=0)
btn8 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '8', command = lambda: btn_Click(8)).grid(row=2,column=1)
btn9 = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '9', command = lambda: btn_Click(9)).grid(row=2,column=2)

#botoes: Operadores
btnAdd = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '+', command = lambda: btn_Click('+')).grid(row=0,column=3)
btnSub = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '-', command = lambda: btn_Click('-')).grid(row=1,column=3)
btnMulti = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '*', command = lambda: btn_Click('*')).grid(row=2,column=3) 
btnDiv = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '/', command = lambda: btn_Click('/')).grid(row=3,column=3)
btnEquals = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = '=',command = lambda: btnEqual() ).grid(row=3,column=2) 
btnClear = Button (Below, padx = 16, pady =1, bd = 3, fg = 'black', font = ('arial', 16, 'bold'), width = 2, height = 2, text = 'C', command = lambda: btn_Clear()).grid(row=3,column=0) 
 
root.geometry('300x340+50+50')
root.title('CALCULADORA')
root.mainloop()
