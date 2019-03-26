from tkinter import *
#import calculator

window = Tk()

window.title("Resistor color code calculator")

menu = Menu(window)                          #inserts top about and exit tabs
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="About")
filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_command(label="Exit")

controlsMap = {}

options = ("Black      (0)", 'Brown      (1)', "Red         (2)", "Orange     (3)",
                      "Yellow     (4)", "Green      (5)", "Blue       (6)", "Violet     (7)", "Grey       (8)",
                      "White      (9)")

options2 = ("Black      (x1)", 'Brown      (x10)', "Red         (x100)", "Orange     (x1K)",
                      "Yellow     (x10K)", "Green      (x100K)", "Blue       (x1M)", "Violet     (x10M)",
                      "Grey       (x100M)", "White      (x1G)")

options3 = ('Brown      (1%)', "Red         (2%)","Green      (0.5%)", "Blue       (0.25%)", "Violet     (0.1%)",
                      "Grey       (0.05%)", "Gold      (5%)", 'Silver      (10%)')

#global answer, variable, variable2, variable3

def callbackFunc(name, index, mode):
    value = window.getvar(name) #getvar: return the value of Tcl variable NAME
    widget = controlsMap[name]
    if value == 'Black      (0)':
        widget.config(bg='Black',fg='White',
                 activebackground='black',
                 activeforeground='white')
    elif value == 'Brown      (1)':
        widget.config(bg='brown',fg='black',
                      activebackground='brown',
                      activeforeground='black')
    elif value == 'Red         (2)':
        widget.config(bg='red',fg='black',
                 activebackground='red',
                 activeforeground='black')
    elif value == 'Orange     (3)':
        widget.config(bg='orange',fg='black',
                      activebackground='orange',
                      activeforeground='black')
    elif value == 'Yellow     (4)' :
        widget.config(bg='yellow',fg='black',
                      activebackground='yellow',
                      activeforeground='black')
    elif value == 'Green      (5)':
        widget.config(bg='green',fg='black',
                      activebackground='green',
                      activeforeground='black')
    elif value == 'Blue       (6)':
        widget.config(bg='blue',fg='black',
                 activebackground='blue',
                 activeforeground='black')
    elif value == 'Violet     (7)':
        widget.config(bg='violet',fg='black',
                      activebackground='violet',
                      activeforeground='black')
    elif value == 'Grey       (8)':
        widget.config(bg='grey',fg='black',
                      activebackground='grey',
                      activeforeground='black')
    elif value == 'White      (9)':
        widget.config(bg='white',fg='black',
                      activebackground='white',
                      activeforeground='yellow')
    else:
        widget.config(bg='SystemButtonFace',fg='SystemButtonText',
                 activebackground='SystemButtonFace',
                 activeforeground='SystemButtonText')


def callbackFunc2(name, index, mode):
    value = window.getvar(name)  # getvar: return the value of Tcl variable NAME
    widget = controlsMap[name]
    if value == 'Black      (x1)':
        widget.config(bg='Black', fg='White',
                      activebackground='black',
                      activeforeground='white')
    elif value == 'Brown      (x10)':
        widget.config(bg='brown', fg='black',
                      activebackground='brown',
                      activeforeground='black')
    elif value == 'Red         (x100)':
        widget.config(bg='red', fg='black',
                      activebackground='red',
                      activeforeground='black')
    elif value == 'Orange     (x1K)':
        widget.config(bg='orange', fg='black',
                      activebackground='orange',
                      activeforeground='black')
    elif value == 'Yellow     (x10K)':
        widget.config(bg='yellow', fg='black',
                      activebackground='yellow',
                      activeforeground='black')
    elif value == 'Green      (x100K)':
        widget.config(bg='green', fg='black',
                      activebackground='green',
                      activeforeground='black')
    elif value == 'Blue       (x1M)':
        widget.config(bg='blue', fg='black',
                      activebackground='blue',
                      activeforeground='black')
    elif value == 'Violet     (x10M)':
        widget.config(bg='violet', fg='black',
                      activebackground='violet',
                      activeforeground='black')
    elif value == 'Grey       (x100M)':
        widget.config(bg='grey', fg='black',
                      activebackground='grey',
                      activeforeground='black')
    elif value == 'White      (x1G)':
        widget.config(bg='white', fg='black',
                      activebackground='white',
                      activeforeground='black')
    else:
        widget.config(bg='SystemButtonFace', fg='SystemButtonText',
                      activebackground='SystemButtonFace',
                      activeforeground='SystemButtonText')

def callbackFunc3(name, index, mode):
    value = window.getvar(name)  # getvar: return the value of Tcl variable NAME
    widget = controlsMap[name]
    if value == 'Brown      (1%)':
        widget.config(bg='brown', fg='black',
                      activebackground='brown',
                      activeforeground='black')
    elif value == 'Red         (2%)':
        widget.config(bg='red', fg='black',
                      activebackground='red',
                      activeforeground='black')
    elif value == 'Green      (0.5%)':
        widget.config(bg='green', fg='black',
                      activebackground='green',
                      activeforeground='black')
    elif value == 'Blue       (0.25%)':
        widget.config(bg='blue', fg='black',
                      activebackground='blue',
                      activeforeground='black')
    elif value == 'Violet     (0.1%)':
        widget.config(bg='violet', fg='black',
                      activebackground='violet',
                      activeforeground='black')
    elif value == 'Grey       (0.05%)':
        widget.config(bg='grey', fg='black',
                      activebackground='grey',
                      activeforeground='black')
    elif value == 'Gold      (5%)':
        widget.config(bg='gold', fg='black',
                      activebackground='gold',
                      activeforeground='black')
    elif value == 'Silver      (10%)':
        widget.config(bg='silver', fg='black',
                      activebackground='silver',
                      activeforeground='black')
    else:
        widget.config(bg='SystemButtonFace', fg='SystemButtonText',
                      activebackground='SystemButtonFace',
                      activeforeground='SystemButtonText')


#def color_values():                                  #works for imported calculator file to be called in convert button
    #variable = variable1.get()
    #col2 = variable2.get()
    #col3 = variable3.get()
    #calculator.colour_code()
    #t1.insert(END, resis)


def default():
    b1 = Button(window, text="3 Band", width=12, command=three_band_command)
    b1.grid(row=0, column=1)

    b2 = Button(window, text="4 Band", width=12, command=four_band_command)
    b2.grid(row=0, column=3)

    b3 = Button(window, text="5 Band", width=12, command=five_band_command)
    b3.grid(row=0, column=5)


def three_band_command():                                                                       #Design for 3 band resistance calculatio
    l1 = Label(window, text=' ')
    l1.grid(row=0, column=0)

    l2 = Label(window, text=' ')
    l2.grid(row=0, column=2)

    l3 = Label(window, text=' ')
    l3.grid(row=0, column=4)

    l4 = Label(window, text=' ')
    l4.grid(row=0, column=6)

    l5 = Label(window, text=' ')
    l5.grid(row=1, column=0)

    l6 = Label(window, text="1st Band:")
    l6.grid(row=2, column=0)

    l7 = Label(window, text="2nd Band:")
    l7.grid(row=4, column=0)

    l8 = Label(window, text="Multiplier:")
    l8.grid(row=6, column=0)

    variable1 = StringVar(window, name='variable1')
    set1 = OptionMenu(window, variable1, *options)
    set1.configure(width=20)
    set1.grid(row=2, column=1)
    controlsMap['variable1'] = set1
    variable1.trace_variable('w', callbackFunc)

    variable2 = StringVar(window, name='variable2')
    set2 = OptionMenu(window, variable2, *options)
    set2.configure(width=20)
    set2.grid(row=4, column=1)
    controlsMap['variable2'] = set2
    variable2.trace_variable('w', callbackFunc)

    variable3 = StringVar(window, name='variable3')
    set3 = OptionMenu(window, variable3, *options2)
    set3.configure(width=20)
    set3.grid(row=6, column=1)
    controlsMap['variable3'] = set3
    variable3.trace_variable('w', callbackFunc2)

    t1 = Text(window, width=10, height=2)
    t1.grid(row=12, column=4)

    l11 = Label(window, text="ohms")
    l11.grid(row=12, column=5)

    b10 = Button(window, text="Convert", command=color_values)
    b10.grid(row=12, column=3)

    # resis = calculator.colour_code(set1)



def four_band_command():                                                #Design for 4 band resistance calculation
    three_band_command()
    l8 = Label(window, text="Tolerance:")
    l8.grid(row=8, column=0)

    variable4 = StringVar(window, name='variable4')
    set4 = OptionMenu(window, variable4, *options3)
    set4.configure(width=20)
    set4.grid(row=8, column=1)
    controlsMap['variable4'] = set4
    variable4.trace_variable('w', callbackFunc3)

    t1 = Text(window, width=10, height=2)
    t1.grid(row=12, column=4)

    l11 = Label(window, text="ohms")
    l11.grid(row=12, column=5)

    #t1.insert(END, resis)

def five_band_command():                                                    #Design for 5 band resistance calculation
    default()
    four_band_command()
    l9 = Label(window, text="5th Band")
    l9.grid(row=10, column=0)

    variable5 = StringVar()
    set5 = OptionMenu(window, variable5, "Black      (1)", 'Brown      (x10)', "Red         (x100)", "Orange     (x1K)",
                      "Yellow     (x10K)", "Green      (x100K)", "Blue       (x1M)", "Violet     (x10M)",
                      "Grey       (x100M)", "White      (x1G)")


    variable5 = StringVar(window, name='variable5')
    set5 = OptionMenu(window, variable5, *options3)
    set5.configure(width=20)
    set5.grid(row=10, column=1)
    controlsMap['variable5'] = set5
    variable5.trace_variable('w', callbackFunc3)

    t1 = Text(window, width=10, height=2)
    t1.grid(row=12, column=4)

    l11 = Label(window, text="ohms")
    l11.grid(row=12, column=5)


default()

window.mainloop()