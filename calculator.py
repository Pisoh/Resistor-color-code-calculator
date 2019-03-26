from tkinter import *

window = Tk()

def colour_code():
    resistance = 1
    #variable = input("Enter first colour band: ")
    #col2 = input("Enter second colour band: ")
    #col3 = input("Enter third colour band: ")

    variable = e1.get()
    col2 = e2.get()
    col3 = e3.get()

    #variable = e1_value.lower()
    #col2 = e2_value.lower()
    #col3 = e3_value.lower()

    if variable == 'black':                                  #Accounts for first band
        if col2 == 'black':                              #2nd band
            resis = resistance * 0
        elif col2 == 'brown':                             #second band
            if col3 == 'black':                            #Third band
               resis = ((resistance * 0) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 0) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 0) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 0) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 0) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 0) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 0) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 0) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 0) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 0) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 0) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 0) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 0) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 0) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 0) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 0) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 0) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 0) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 0) + 9) * 0.01
            else:
                resis = "Invalid"

        else:
            resis = "Invalid"

    elif variable == 'brown':                                      #Band 1
        if col2 == 'black':                                   # 2nd band
            if col3 == 'black':  # Third band
                resis = ((resistance * 10))
            elif col3 == 'brown':
                resis = (resistance * 10) * 10
            elif col3 == 'red':
                resis = (resistance * 10) * 100
            elif col3 == 'orange':
                resis = (resistance * 10) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 10) * 10000
            elif col3 == 'green':
                resis = (resistance * 10) * 100000
            elif col3 == 'blue':
                resis = (resistance * 10) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 10) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 10) * 100000000
            elif col3 == 'white':
                resis = (resistance * 10) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 10) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 10)  * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':                                     # second band
            if col3 == 'black':                                     # Third band
                resis = ((resistance * 10) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 10) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 10) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 10) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 10) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 10) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 10) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 10) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 10) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 10) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 10) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 10) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 10) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 10) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 10) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 10) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 10) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 10) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 10) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 10) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'red':
        if col2 == 'black':                                        # 2nd band
            if col3 == 'black':                                     # Third band
                resis = (resistance * 20)
            elif col3 == 'brown':
                resis = (resistance * 20) * 10
            elif col3 == 'red':
                resis = (resistance * 20) * 100
            elif col3 == 'orange':
                resis = (resistance * 20) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 20) * 10000
            elif col3 == 'green':
                resis = (resistance * 20) * 100000
            elif col3 == 'blue':
                resis = (resistance * 20) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 20) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 20) * 100000000
            elif col3 == 'white':
                resis = (resistance * 20) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 20) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 20) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':                               # second band
            if col3 == 'black':                             # Third band
                resis = ((resistance * 20) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 20) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 20) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 20) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 20) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 20) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 20) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 20) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 20) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'orange':
        if col2 == 'black':                                        # 2nd band
            if col3 == 'black':                                     # Third band
                resis = (resistance * 30)
            elif col3 == 'brown':
                resis = (resistance * 30) * 10
            elif col3 == 'red':
                resis = (resistance * 30) * 100
            elif col3 == 'orange':
                resis = (resistance * 30) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 30) * 10000
            elif col3 == 'green':
                resis = (resistance * 30) * 100000
            elif col3 == 'blue':
                resis = (resistance * 30) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 30) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 30) * 100000000
            elif col3 == 'white':
                resis = (resistance * 30) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 30) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 30) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':                               # second band
            if col3 == 'black':                             # Third band
                resis = ((resistance * 30) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 30) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 30) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 30) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 30) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 30) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 30) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 30) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 30) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"


    elif variable == 'yellow':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 40)
            elif col3 == 'brown':
                resis = (resistance * 40) * 10
            elif col3 == 'red':
                resis = (resistance * 40) * 100
            elif col3 == 'orange':
                resis = (resistance * 40) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 40) * 10000
            elif col3 == 'green':
                resis = (resistance * 40) * 100000
            elif col3 == 'blue':
                resis = (resistance * 40) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 40) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 40) * 100000000
            elif col3 == 'white':
                resis = (resistance * 40) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 40) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 40) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 40) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 40) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 40) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 40) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 40) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 40) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 40) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 40) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 40) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 40) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 40) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 40) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 40) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 40) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 40) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 40) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 40) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 40) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 40) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 40) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'green':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 50)
            elif col3 == 'brown':
                resis = (resistance * 50) * 10
            elif col3 == 'red':
                resis = (resistance * 50) * 100
            elif col3 == 'orange':
                resis = (resistance * 50) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 50) * 10000
            elif col3 == 'green':
                resis = (resistance * 50) * 100000
            elif col3 == 'blue':
                resis = (resistance * 50) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 50) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 50) * 100000000
            elif col3 == 'white':
                resis = (resistance * 50) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 50) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 50) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 50) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 50) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 50) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 50) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 50) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 50) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 50) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 50) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 50) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 50) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 50) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 50) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 50) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 50) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 50) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 50) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 50) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 50) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 50) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 50) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'blue':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 60)
            elif col3 == 'brown':
                resis = (resistance * 60) * 10
            elif col3 == 'red':
                resis = (resistance * 60) * 100
            elif col3 == 'orange':
                resis = (resistance * 60) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 60) * 10000
            elif col3 == 'green':
                resis = (resistance * 60) * 100000
            elif col3 == 'blue':
                resis = (resistance * 60) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 60) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 60) * 100000000
            elif col3 == 'white':
                resis = (resistance * 60) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 60) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 60) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 60) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 60) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 60) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 60) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 60) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 60) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 60) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 60) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 60) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 60) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 60) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 60) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 60) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 60) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 60) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 60) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 60) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 60) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 60) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 60) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'violet':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 70)
            elif col3 == 'brown':
                resis = (resistance * 70) * 10
            elif col3 == 'red':
                resis = (resistance * 70) * 100
            elif col3 == 'orange':
                resis = (resistance * 70) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 70) * 10000
            elif col3 == 'green':
                resis = (resistance * 70) * 100000
            elif col3 == 'blue':
                resis = (resistance * 70) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 70) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 70) * 100000000
            elif col3 == 'white':
                resis = (resistance * 70) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 70) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 70) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 70) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 70) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 70) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 70) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 70) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 70) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 70) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 70) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 70) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 70) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 70) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 70) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 70) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 70) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 70) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 70) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 70) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 70) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 70) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 70) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'grey':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 80)
            elif col3 == 'brown':
                resis = (resistance * 80) * 10
            elif col3 == 'red':
                resis = (resistance * 80) * 100
            elif col3 == 'orange':
                resis = (resistance * 80) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 80) * 10000
            elif col3 == 'green':
                resis = (resistance * 80) * 100000
            elif col3 == 'blue':
                resis = (resistance * 80) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 80) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 80) * 100000000
            elif col3 == 'white':
                resis = (resistance * 80) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 80) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 80) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 80) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 80) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 80) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 80) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 80) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 80) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 80) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 80) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 80) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 80) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 80) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 80) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 80) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 80) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 80) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 80) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 80) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 80) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 80) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 80) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 80) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 80) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 80) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 80) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 80) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 80) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 80) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 80) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 80) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 80) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 80) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 80) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 80) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 80) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 80) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 80) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 80) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 80) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 80) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 80) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 80) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 80) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 80) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 80) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 80) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 80) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 80) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 80) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 80) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 80) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 80) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 80) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 80) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 80) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 80) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 80) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 80) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 80) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 80) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 80) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 80) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 0) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 20) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 20) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 20) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 20) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 20) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 20) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 20) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 20) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 20) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 20) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 20) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 20) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 20) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    elif variable == 'orange':
        if col2 == 'black':  # 2nd band
            if col3 == 'black':  # Third band
                resis = (resistance * 30)
            elif col3 == 'brown':
                resis = (resistance * 30) * 10
            elif col3 == 'red':
                resis = (resistance * 30) * 100
            elif col3 == 'orange':
                resis = (resistance * 30) * 1000
            elif col3 == 'yellow':
                resis = (resistance * 30) * 10000
            elif col3 == 'green':
                resis = (resistance * 30) * 100000
            elif col3 == 'blue':
                resis = (resistance * 30) * 1000000
            elif col3 == 'violet':
                resis = (resistance * 30) * 10000000
            elif col3 == 'grey':
                resis = (resistance * 30) * 100000000
            elif col3 == 'white':
                resis = (resistance * 30) * 1000000000
            elif col3 == 'gold':
                resis = (resistance * 30) * 0.1
            elif col3 == 'silver':
                resis = (resistance * 30) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'brown':  # second band
            if col3 == 'black':  # Third band
                resis = ((resistance * 30) + 1)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 1) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 1) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 1) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 1) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 1) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 1) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 1) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 1) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 1) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 1) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 1) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'red':
            if col3 == 'black':
                resis = ((resistance * 30) + 2)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 2) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 2) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 2) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 2) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 2) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 2) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 2) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 2) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 2) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 2) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 2) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'orange':
            if col3 == 'black':
                resis = ((resistance * 30) + 3)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 3) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 3) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 3) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 3) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 3) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 3) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 3) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 3) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 3) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 3) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 3) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'yellow':
            if col3 == 'black':
                resis = ((resistance * 30) + 4)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 4) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 4) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 4) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 4) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 4) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 4) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 4) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 4) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 4) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 4) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 4) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'green':
            if col3 == 'black':
                resis = ((resistance * 30) + 5)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 5) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 5) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 5) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 5) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 5) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 5) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 5) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 5) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 5) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 5) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 5) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'blue':
            if col3 == 'black':
                resis = ((resistance * 30) + 6)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 6) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 6) * 100
            elif col3 == 'orange':
                resis = ((resistance * 20) + 6) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 6) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 6) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 6) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 6) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 6) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 6) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 6) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 6) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'violet':
            if col3 == 'black':
                resis = ((resistance * 30) + 7)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 7) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 7) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 7) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 7) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 7) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 7) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 7) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 7) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 7) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 7) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 7) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'grey':
            if col3 == 'black':
                resis = ((resistance * 30) + 8)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 8) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 8) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 8) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 8) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 8) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 8) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 8) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 8) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 8) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 8) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 8) * 0.01
            else:
                resis = "Invalid"

        elif col2 == 'white':
            if col3 == 'black':
                resis = ((resistance * 30) + 9)
            elif col3 == 'brown':
                resis = ((resistance * 30) + 9) * 10
            elif col3 == 'red':
                resis = ((resistance * 30) + 9) * 100
            elif col3 == 'orange':
                resis = ((resistance * 30) + 9) * 1000
            elif col3 == 'yellow':
                resis = ((resistance * 30) + 9) * 10000
            elif col3 == 'green':
                resis = ((resistance * 30) + 9) * 100000
            elif col3 == 'blue':
                resis = ((resistance * 30) + 9) * 1000000
            elif col3 == 'violet':
                resis = ((resistance * 30) + 9) * 10000000
            elif col3 == 'grey':
                resis = ((resistance * 30) + 9) * 100000000
            elif col3 == 'white':
                resis = ((resistance * 30) + 9) * 1000000000
            elif col3 == 'gold':
                resis = ((resistance * 30) + 9) * 0.1
            elif col3 == 'silver':
                resis = ((resistance * 30) + 9) * 0.01
            else:
                resis = "Invalid"
        else:
            resis = "Invalid"

    t1.insert(END, resis)

var1 = StringVar
e1 = Entry(window, textvariable=var1)
e1.grid(row=0, column=0)

var2 = StringVar
e2 = Entry(window, textvariable=var2)
e2.grid(row=0, column=1)

var3 = StringVar
e3 = Entry(window, textvariable=var3)
e3.grid(row=0, column=2)

b1 = Button(window, text="Convert", command = colour_code)
b1.grid(row=1, column=0)

t1 = Text(window, width=10, height=1)
t1.grid(row=2,column=0)


#print(colour_code())

window.mainloop()
