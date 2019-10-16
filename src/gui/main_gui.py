from tkinter import *
from tkinter import ttk
 
main = Tk()
main.title('Writersworn')
main.geometry('500x500')
 
 
# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Character Sheet')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Moves')
 
page3 = ttk.Frame(nb)
nb.add(page3,text="Dice")

page4 = ttk.Frame(nb)
nb.add(page4,text="Oracles")

page5 = ttk.Frame(nb)
nb.add(page5,text="Journal")

main.mainloop()