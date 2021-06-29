import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import pandas as pd

root = tk.Tk()
root.config(background='#fff')
root.columnconfigure(0, weigh=1)
root.rowconfigure(0, weight=1)
# root.attributes('-type', 'splash')
# root.overrideredirect()
# Vars
selection = {
    '0900': tk.BooleanVar(),
    '1200': tk.BooleanVar(),
    '1500': tk.BooleanVar(),
    '1800': tk.BooleanVar(),
    '2100': tk.BooleanVar(),
    '2400': tk.BooleanVar(),
    '2700': tk.BooleanVar(),
    '3000': tk.BooleanVar(),
    '3300': tk.BooleanVar(),
    '3600': tk.BooleanVar(),
    '3900': tk.BooleanVar(),
    '4200': tk.BooleanVar(),
    '4500': tk.BooleanVar(),
    '4800': tk.BooleanVar(),
    '5100': tk.BooleanVar(),
    '5400': tk.BooleanVar(),
    '5700': tk.BooleanVar(),
    '6000': tk.BooleanVar(),
    '6300': tk.BooleanVar(),
    '6600': tk.BooleanVar()
}

# Frame Style
s = ttk.Style()
s.theme_use('alt')
s.configure('TFrame', background='#fff')

# Frame
main_frame = ttk.Frame(root)
main_frame.grid(sticky='ns')
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

with open('/home/juan/Documents/json_test.json', 'r') as reader:
    dictionary = json.load(reader)

df = pd.DataFrame.from_dict(dictionary)
df.reset_index(inplace=True, drop=True)
df.drop('SPEC', axis=1, inplace=True)
df.fillna(0, inplace=True)
print(df.head())

# treeview = ttk.Treeview(main_frame,
#                         columns=list(df.columns),
#                         selectmode='browse')
# treeview.heading('#0', text='INDEX')
# for i in df.columns:
#     treeview.heading(i, text=f'{i}')
# treeview.grid(column=0, sticky='ns')
# treeview.grid_propagate(0)

# for i in list(df.index):
#     treeview.insert('', 'end', i, text=i, values=list(df.loc[i].values))

# # Radio Button
# for k, v in selection.items():
#     s.configure('TRadiobutton', background='#fff', font=('arial 10 bold'))
#     rad = ttk.Radiobutton(main_frame,
#                           text=f'038 x 038 x {k}',
#                           variable=selection[k],
#                           value=True)
#     rad.grid(column=1, sticky='nesw')
# root.mainloop()

d = df.to_dict()
with open(
        '/mnt/DATA-A/Whitcher Docs/Pricing_Program/GUI Price conversion/Price>>sys/data_files/base_template.json',
        'w') as writer:
    json.dump(d, writer)
