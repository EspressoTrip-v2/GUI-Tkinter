import tkinter as tk
from tkinter import ttk, messagebox
import app_views as av
import json
import models as m


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load in existing customer listings
        with open(
                '/mnt/DATA-A/Whitcher Docs/Pricing_Program/GUI Price conversion/Price>>sys/data_files/cust_price_json.json',
                'r') as objA:
            self.exist_cus_pric_db = json.load(objA)

        # Load Custom form base
        with open(
                '/mnt/DATA-A/Whitcher Docs/Pricing_Program/GUI Price conversion/Price>>sys/data_files/base_template.json',
                'r') as objB:
            self.template_base = json.load(objB)

        self.callbacks = {
            'on_home_raise': self.home_raise,
            'on_new': self.on_new,
            'root_exit': self.quit,
            'exist_cus_price_db': self.exist_cus_pric_db,
            'base_template': self.template_base
        }

        # Self Configuration #
        #####################
        self.protocol("WM_DELETE_WINDOW", self.e_pop)
        self.title('')
        self.tk.call(
            'wm', 'iconphoto', self._w,
            tk.PhotoImage(
                file=
                '/mnt/DATA-A/Whitcher Docs/Pricing_Program/GUI Price conversion/Price>>sys/icons/task_icon.png'
            ))
        self.resizable(width=False, height=False)
        self.columnconfigure((0, 1, 2), weight=1)

        # Setting Widgets #
        ###################

        self.frame = av.Home_Screen(self,
                                    self.callbacks,
                                    height='150m',
                                    width='120m')
        self.frame.propagate(0)
        self.frame.grid(row=0, column=1)

    # Functions #
    #############

    def home_raise(self):
        self.frame.tkraise()

    def on_new(self):
        self.withdraw()
        self.add_new_topB = av.MainEditing(self,
                                           self.callbacks,
                                           update=False,
                                           bg='#fff')

    def e_pop(self):
        if messagebox.askokcancel("WARNING",
                                  "Exit without saving?",
                                  icon='warning'):
            self.destroy()


app = Application()
app.mainloop()