from tkinter import *
from tkinter import ttk

def calculate():
    result.delete(0, END)
    try:
        result.insert(END, f"Disk size: {discWidthBox.get()}x{tireDiameterBox.get()} ET {discETBox.get()}")
        result.insert(END, f"Tire size: {tireWidthBox.get()}/{tireProfileBox.get()} R{tireDiameterBox.get()}")
    except:
        result.insert(END, "Error")

root = Tk()
root.geometry("300x200")
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
discETBox = ttk.Combobox(width = 5, values=[i for i in range(10, 73)])
discETBox.grid(row=2, column=4)
Button(text="Calculate", command=calculate).grid(row=3, column=1, columnspan=3)
result = Listbox(selectmode=EXTENDED)
result.grid(row=4, column=1, columnspan=3)
root.mainloop()