from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x200")
root.title("Tire Calculator")
Label(text="Tire").grid(row=0, column=0)
Label(text="Disc").grid(row=0, column=3)
Label(text="Width").grid(row=1, column=0)
Label(text="Profile").grid(row=1, column=1)
Label(text="Diameter").grid(row=1, column=2)
Label(text="Width").grid(row=1, column=3)
Label(text="ET").grid(row=1, column=4)
tireWidthBox = ttk.Combobox(width = 5, values=[i for i in range(115, 366, 10)])
tireWidthBox.grid(row=2, column=0)
tireProfileBox = ttk.Combobox(width = 5, values=[i for i in range(25, 91, 5)])
tireProfileBox.grid(row=2, column=1)
tireDiameterBox = ttk.Combobox(width = 5, values=[10, 12, 13, 14, 15, 16, 16.5, 17, 17.5, 18, 19, 19.5, 20, 21, 22, 23, 24])
tireDiameterBox.grid(row=2, column=2)
discWidthBox = ttk.Combobox(width = 5, values=[4, 4.5, 5, 5.5, 6, 6.5, 6.75, 7, 7.5, 8, 8.25, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13, 14])
discWidthBox.grid(row=2, column=3)
discETBox = ttk.Combobox(width = 5, values=[i for i in range(10, 73)]) #[-129, -30, -12, -10, -6, -5, -3, -2.5, -1, 0, 2, 3, 4, 5, 6, 6.4, 8, 8.9, 10, 10.6, 11, 11.4, 12, 12.7, 13, 13.5, 14, 15, 16, 17, 18, 18.5, 19, 19.05, 19.1, 19.5, 20, 21, 21.5, 22, 22.1, 22.3, 22.4, 22.5, 23, 23.3, 23.5, 23.6, 24, 24.75, 25, 25.1, 25.2, 25.3, 25.4, 25.5, 26, 27, 27.5, 28, 28.4, 29, 29.5, 30, 30.1, 30.5, i for i in range(31, 73), 75, 76, 77, 78, 83, 100, 102, 105, 107, 108, 109, 110, 113, 115, 117, 118.3, 120, 125, 127, 142]
discETBox.grid(row=2, column=4)
root.mainloop()