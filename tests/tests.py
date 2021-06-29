import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os
import pandas as pd
import numpy as np

cols = ['DESC', 'UNITPRICE', 'BUNDLE SIZE', 'PRICELIST']

anchor = tk.CENTER


def file_(cust='', columns=cols):
    column = ['desc', 'unitprice', 'bundle size', 'pricelist']

    if not cust:
        main = tk.Tk()
        main.withdraw()
        tk.messagebox.showerror(title='Error',
                                message='Please enter customer',
                                parent=main)
    else:

        pickle_file = pickle.load(
            open(
                '/home/juan/DATA-A/Whitcher Docs/Pricing_Program/GUI Price conversion/tests/reforms.p',
                'rb'))
        customer = pickle_file[cust]
        customer = customer[column].copy()
        customer = customer[customer['unitprice'] > 0]
        return customer


def edit_price(event):
    item = tv.identify("item", event.x, event.y)
    integer = integer_box()

    tv.set(item, 'UNITPRICE', 20)


def integer_box():
    def check():
        print(price.get())
        top.withdraw()

    price = tk.StringVar()
    top = tk.Toplevel()
    top.title('Price Change')
    top.geometry('200x100')
    top.resizable(width=False, height=False)
    top.columnconfigure((0, 1, 2), weight=1)
    top.rowconfigure((0, 1, 2), weight=1)
    label = ttk.Label(top, text='Enter Price', font=('arial 12 italic'))
    label.grid(row=0, column=1)

    entry = ttk.Entry(top, textvariable=price, validate='all')
    entry.grid(row=1, column=1)
    entry.focus_set()
    button = tk.Button(top, text='Check', command=check)
    button.grid(row=2, column=1)


f = file_('AHM001', cols)

root = tk.Tk()
root.title(f'AHM001')
root.geometry('1400x600')
tv = ttk.Treeview(root, columns=cols, selectmode='browse')
tv.heading('#0', text='ITEMNO', anchor=anchor)

# Create event for double click
tv.event_add('<<select>>', '<Double-Button-1>')
# Bind to a function
tv.bind('<<select>>', edit_price)

# Populate tree
for i in cols:
    tv.heading(i, text=i, anchor=anchor)

for i in f.index:
    tv.insert('', 'end', i, text=i, values=list(f.loc[i].values))
for i in cols:
    if i == 'DESC':
        tv.column(i, anchor='w')
    else:
        tv.column(i, anchor=anchor)

scrollv = tk.Scrollbar(root, orient=tk.VERTICAL, command=tv.yview)
tv.configure(yscrollcommand=scrollv.set)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
tv.grid(sticky='nesw')
scrollv.grid(row=0, column=1, sticky='nsw')

root.mainloop()
