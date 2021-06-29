import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
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

# main_menu = tk.Menu(tearoff=False)
# # root.config(menu=main_menu)
menubutton = tk.Menubutton(root, text='Sizes')
selection_menu = tk.Menu(menubutton, tearoff=False)
menubutton.config(menu=selection_menu)
selection_menu.add_cascade(label='Selection')

for k in selection:
    selection_menu.add_radiobutton(label=f'038 x 038 x {k}',
                                   variable=selection[k],
                                   value=True)

menubutton.pack()
root.mainloop()
for k, v in selection.items():
    print(f'{k}: {selection[k].get()}')