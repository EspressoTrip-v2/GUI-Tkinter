import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from datetime import datetime
import time
time_day = str(datetime.now())[:10]
from PIL import ImageTk as itk
from constants import ImageFiles as image
import models as m
import widgets as w


####################
# Home Screen Form #
####################
class Home_Screen(ttk.Frame):
    """Home Screen main window 
    Arguments:
        ttk {[Frame]} -- [master = root, new_command=new button action, update_command= update button action, industrial_command=industrial button action]
    """
    def __init__(self, master, callbacks, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        png_files = image.home_window

        # Image Files #
        ###############
        self.logo = itk.PhotoImage(file=png_files['logo'])

        self.new_cus_logo = itk.PhotoImage(file=png_files['new_cus_logo'])

        self.update_cus_logo = itk.PhotoImage(
            file=png_files['update_cus_logo'])

        self.exit_logo = itk.PhotoImage(file=png_files['exit_logo'])

        self.help_logo = itk.PhotoImage(file=png_files['help_logo'])

        # Self Configuration #
        ######################
        self.callbacks = callbacks
        self.grid_propagate(0)
        self.columnconfigure((0, 1, 2), weight=1)

        # Frame Style #
        ###############
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('TFrame', background='#fff')

        # Label Style #
        ###############
        s.configure('TLabel', background='#fff')
        self.label = ttk.Label(self, image=self.logo)
        self.label.grid(row=0, column=1)

        # Frame Setups #
        ################
        s.configure('TFrame', relief=tk.FLAT)
        self.labelframe = ttk.Frame(self)
        self.labelframe.columnconfigure((0, 1, 2), weight=1)
        self.labelframe.grid(column=0, columnspan=3, pady=40, sticky='nsew')

        # Buttun Setups #
        #################
        s.configure('TButton', background='#fff', relief=tk.FLAT)
        self.new_cus_button = ttk.Button(self.labelframe,
                                         image=self.new_cus_logo,
                                         cursor='hand2',
                                         command=self.on_new)
        self.new_cus_button.grid(row=1, column=1, pady=20)

        self.update_cus_button = ttk.Button(self.labelframe,
                                            image=self.update_cus_logo,
                                            cursor='hand2',
                                            command=self.on_update_customer)
        self.update_cus_button.grid(row=2, column=1, pady=10)

        self.exit_button = ttk.Button(self.labelframe,
                                      image=self.exit_logo,
                                      cursor='hand2',
                                      command=self.callbacks['root_exit'])
        self.exit_button.grid(row=3, column=1, pady=20)

        self.help_button = ttk.Button(self.labelframe,
                                      image=self.help_logo,
                                      cursor='question_arrow')
        self.help_button.grid(row=4, column=1, pady=15)

    def on_new(self):
        self.master.withdraw()
        self.add_new_topB = MainEditing(self.master,
                                        self.callbacks,
                                        update=False,
                                        bg='#fff')

    def on_update_customer(self):
        self.master.withdraw()
        self.update_form = MainEditing(self.master,
                                       self.callbacks,
                                       update=True,
                                       bg='#fff')


#######################
# Main Editing Window #
#######################


class MainEditing(tk.Toplevel):
    ''' Top Level Window for editing '''
    def __init__(self, master, callbacks, update, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", self.form_close)
        # self.attributes('-fullscreen', True)
        png_files = image.main_window

        self.from_price_logo = itk.PhotoImage(
            file=png_files['from_price_logo'])

        self.from_region_logo = itk.PhotoImage(
            file=png_files['from_region_logo'])

        self.home_logo = itk.PhotoImage(file=png_files['home_logo'])

        self.footer_logo = itk.PhotoImage(file=png_files['footer_logo'])

        self.whitcher_logo = itk.PhotoImage(file=png_files['whitcher_logo'])

        self.update_existing_logo = itk.PhotoImage(
            file=png_files['update_existing_logo'])

        self.cancel = itk.PhotoImage(file=png_files['cancel'])

        self.save = itk.PhotoImage(file=png_files['save'])

        self.footer_sep = itk.PhotoImage(file=png_files['footer_sep'])
        self.edit_label = itk.PhotoImage(file=png_files['edit_label'])

        self.warning_cus = itk.PhotoImage(file=png_files['warning_cus'])

        self.select_template = itk.PhotoImage(
            file=png_files['select_template'])
        self.new_customer_label = itk.PhotoImage(
            file=png_files['new_customer_label'])

        # Self Configuration #
        ######################
        self.callbacks = callbacks
        self.update = update
        self.columnconfigure(0, weight=1)

        # Styles #
        ##########
        self.s = ttk.Style()
        self.s.theme_use('alt')
        self.s.configure('TFrame', background='#fff')
        self.s.configure('TButton', relief=tk.FLAT, anchor=tk.CENTER)
        self.s.configure('TCheckbutton',
                         relief=tk.FLAT,
                         font=('TkDefault 11 bold'),
                         background='#fff',
                         anchor=tk.CENTER)

        # Frame Setups #
        #################
        self.top_frameA = ttk.Frame(self)
        self.top_frameA.grid(row=0, column=0, pady=10, sticky='ew')
        self.top_frameA.columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.ac_whitcher_label = ttk.Label(self.top_frameA,
                                           image=self.whitcher_logo)
        self.ac_whitcher_label.grid(row=0, column=2, sticky='nsew')

        self.middle_frame = ttk.Frame(self)
        self.middle_frame.grid(row=1, column=0, pady=10, sticky='nsew')
        self.middle_frame.columnconfigure((0), weight=1)

        self.savecontrol_frame = ttk.Frame(self)
        self.savecontrol_frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.savecontrol_frame.grid(row=2, column=0, sticky='nsew')

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.columnconfigure((0, 2), weight=1)
        self.bottom_frame.grid(row=2, column=0, sticky='nsew')

        # Label Setups #
        ################
        self.footer_sys = ttk.Label(self.bottom_frame, image=self.footer_logo)
        self.footer_sys.grid(row=0, column=1, sticky='nsew', padx=25)

        self.footer_sepA = ttk.Label(self.bottom_frame, image=self.footer_sep)
        self.footer_sepA.grid(row=0, column=0, sticky='nsew', padx=25)
        self.footer_sepB = ttk.Label(self.bottom_frame, image=self.footer_sep)
        self.footer_sepB.grid(row=0, column=2, sticky='nsew', padx=25)
        # Buttons Setups #
        ##################
        self.home_buttonA = ttk.Button(self.top_frameA,
                                       image=self.home_logo,
                                       cursor='hand2',
                                       command=self.form_close)
        self.home_buttonA.grid(row=0, column=0, padx=25)

        self.from_price_button = ttk.Button(self.top_frameA,
                                            image=self.from_price_logo,
                                            cursor='hand2',
                                            command=None)  # TODO: Add func
        self.from_price_button.grid(row=0, column=1, padx=25)

        self.from_region_button = ttk.Button(self.top_frameA,
                                             image=self.from_region_logo,
                                             cursor='hand2',
                                             command=None)
        self.from_region_button.grid(row=0, column=3, padx=25)

        self.edit_existing_button = ttk.Button(
            self.top_frameA,
            image=self.update_existing_logo,
            cursor='hand2',
            command=self.update_window_control)
        self.edit_existing_button.grid(row=0, column=4, padx=25)

        self.cancel_button = ttk.Button(self.savecontrol_frame,
                                        cursor='hand2',
                                        image=self.cancel,
                                        command=self.form_close,
                                        style='TButton')
        self.cancel_button.grid(row=0, column=1, padx=25)

        self.save_button = ttk.Button(
            self.savecontrol_frame,
            image=self.save,
            cursor='hand2',
        )
        self.save_button.grid(row=0, column=2, padx=25, sticky='ns')

        if self.update:
            self.update_window_control()
        else:
            self.new_window_control()

    # Functions #
    #############

    def back(self):
        self.home_buttonA.config(state=tk.ACTIVE)
        self.edit_existing_button.config(state=tk.ACTIVE)
        self.from_region_button.config(state=tk.ACTIVE)
        self.from_price_button.config(state=tk.ACTIVE)

    # Popup windows #
    #################
    def ask_existing_number(self):

        self.cus_pricelist_num = tk.StringVar()

        self.cus_pricelist_num.set('Select here...')
        self.windowA = tk.Toplevel(self, background='#fff')
        self.windowA.protocol("WM_DELETE_WINDOW", self.form_close)
        self.windowA.columnconfigure((0), weight=1)
        self.windowA.rowconfigure((0, 1, 2, 3), weight=1)

        self.warning_label = ttk.Label(self.windowA, image=self.warning_cus)
        self.warning_label.grid(row=0, sticky='ew')

        self.ask_label = ttk.Label(self.windowA, image=self.edit_label)
        self.ask_label.grid(row=0, sticky='ew')

        self.combo_frame = tk.Frame(self.windowA, background='#fff')
        self.combo_frame.columnconfigure(0, weight=1)
        self.combo_frame.grid(row=1, column=0, sticky='ew', pady=10, padx=10)
        self.combo_cus = ttk.Combobox(
            self.combo_frame,
            textvariable=self.cus_pricelist_num,
            values=list(self.callbacks['exist_cus_price_db']))
        self.combo_cus.grid(row=0, column=0, sticky='nsew', pady=10)
        self.combo_cus.configure(font=('TkDefault 12 normal'))
        self.combo_cus.bind('<Button-1>',
                            func=lambda x: self.combo_cus.delete(0, 'end'))

        self.button_frame = tk.Frame(self.windowA, background='#fff')
        self.button_frame.columnconfigure((0, 1), weight=1)
        self.button_frame.grid(row=2, column=0, sticky='ew', pady=10, padx=10)
        self.ac_save_button = ttk.Button(
            self.button_frame,
            cursor='hand2',
            image=self.save,
            command=self.window_control_after_cus_selection)
        self.ac_save_button.grid(row=0, column=1, sticky='ew')

        self.ac_cancel_button = ttk.Button(self.button_frame,
                                           image=self.cancel,
                                           cursor='hand2',
                                           command=self.form_close)
        self.ac_cancel_button.grid(row=0, column=0, sticky='ew')

    def ask_type_template(self):
        self.type_template = tk.BooleanVar()
        self.windowB = tk.Toplevel(self, background='#fff', borderwidth=2)
        self.windowB.protocol("WM_DELETE_WINDOW", self.form_close)

        self.windowB.columnconfigure((0), weight=1)
        self.windowB.rowconfigure((0, 1, 2, 3), weight=1)

        self.ask_label_template = ttk.Label(self.windowB,
                                            image=self.select_template)
        self.ask_label_template.grid(row=1,
                                     column=0,
                                     columnspan=2,
                                     sticky='ew',
                                     padx=10)
        # Template Frame #
        self.template_check_frame = tk.Frame(self.windowB, background='#fff')
        self.template_check_frame.columnconfigure((0, 1, 2), weight=1)
        self.template_check_frame.rowconfigure((0, 1), weight=1)
        self.template_check_frame.grid(row=2, sticky='ew')
        self.template_select_checkboxA = ttk.Checkbutton(
            self.template_check_frame,
            variable=self.type_template,
            text='  SYSTEM TEMPLATE',
            onvalue=False)

        self.template_select_checkboxA.grid(row=0,
                                            column=1,
                                            sticky='ew',
                                            padx=10,
                                            pady=10)

        self.template_select_checkboxB = ttk.Checkbutton(
            self.template_check_frame,
            variable=self.type_template,
            text='  CUSTOM TEMPLATE',
            onvalue=True)
        self.template_select_checkboxB.grid(row=1,
                                            column=1,
                                            sticky='ew',
                                            padx=10)

        # Button #
        self.button_frame_template = tk.Frame(self.windowB, background='#fff')
        self.button_frame_template.columnconfigure((0, 1), weight=1)
        self.button_frame_template.grid(row=3,
                                        column=0,
                                        columnspan=2,
                                        sticky='ew',
                                        pady=10)
        self.ac_save_button_template = ttk.Button(self.button_frame_template,
                                                  image=self.save,
                                                  cursor='hand2',
                                                  command=None)
        self.ac_save_button_template.grid(row=0, column=1)

        self.ac_cancel_button_template = ttk.Button(self.button_frame_template,
                                                    image=self.cancel,
                                                    cursor='hand2',
                                                    command=self.form_close)
        self.ac_cancel_button_template.grid(row=0, column=0)

    def create_new_customer_number(self):
        self.new_number = tk.StringVar()

        self.windowC = tk.Toplevel(self, background='#fff', borderwidth=2)
        self.windowC.protocol("WM_DELETE_WINDOW", self.form_close)

        self.windowC.columnconfigure((0), weight=1)
        self.windowC.rowconfigure((0, 1, 2, 3), weight=1)

        self.ask_new_number = ttk.Label(self.windowC,
                                        image=self.new_customer_label)
        self.ask_new_number.grid(row=1,
                                 column=0,
                                 columnspan=2,
                                 sticky='ew',
                                 padx=10)
        # New Number Frame #
        self.ask_new_number_frame = tk.Frame(self.windowC, background='#fff')
        self.ask_new_number_frame.columnconfigure((0, 1, 2), weight=1)
        self.ask_new_number_frame.rowconfigure((0, 1), weight=1)
        self.ask_new_number_frame.grid(row=2, sticky='ew')
        self.ask_new_number_entry = w.My_EntryAlpha(
            self.ask_new_number_frame,
            textvariable=self.new_number,
            validate='key')

        self.ask_new_number_entry.focus()
        self.ask_new_number_entry.bind(
            '<KeyRelease>',
            func=lambda x: self.new_number.set(self.new_number.get().upper()))
        self.ask_new_number_entry.bind(
            '<KeyRelease-KP_Enter>',
            func=lambda x: self.check_customer_number(self.new_number.get()))

        self.ask_new_number_entry.grid(row=0,
                                       column=1,
                                       sticky='ew',
                                       padx=10,
                                       pady=15)
        self.ask_new_number_entry.configure(font=('TkDefault 12 normal'))

        # Button #
        self.button_frame_ask_new = tk.Frame(self.windowC, background='#fff')
        self.button_frame_ask_new.columnconfigure((0, 1), weight=1)
        self.button_frame_ask_new.grid(row=3,
                                       column=0,
                                       columnspan=2,
                                       sticky='ew',
                                       pady=10)
        self.an_save_button = ttk.Button(
            self.button_frame_ask_new,
            image=self.save,
            cursor='hand2',
            command=lambda: self.check_customer_number(self.new_number.get()))
        self.an_save_button.grid(row=0, column=1)

        self.an_cancel_button = ttk.Button(self.button_frame_ask_new,
                                           image=self.cancel,
                                           cursor='hand2',
                                           command=self.form_close)
        self.an_cancel_button.grid(row=0, column=0)

    def check_customer_number(self, number):
        numbers = list(self.callbacks['exist_cus_price_db'].keys())
        if number in numbers:
            message = messagebox.showerror('WARNING',
                                           'Customer number already exists')
            self.ask_new_number_entry.focus()
            self.ask_new_number_entry.delete(0, 'end')
        else:
            self.windowC.destroy()
            self.deiconify()
            self.newform_window = NewCustomerForm(self.middle_frame, number,
                                                  self.callbacks)
            self.newform_window.grid(sticky='nsew')
            self.from_price_button.config(state=tk.DISABLED)
            self.save_cancel()
            self.home_buttonA.config(state=tk.DISABLED)
            self.edit_existing_button.config(state=tk.DISABLED)
            self.from_region_button.config(state=tk.DISABLED)

    # Window Control Functions #
    ############################
    def window_control_after_cus_selection(self):
        if self.cus_pricelist_num.get(
        ) == 'Please select a customer number...':
            self.windowA.withdraw()
            self.ask_existing_number()

        elif self.cus_pricelist_num.get() not in (
                self.callbacks['exist_cus_price_db'].keys()):
            self.warning_label.tkraise()

        else:
            self.windowA.withdraw()
            self.ask_type_template()

    def window_control_after_template_selection(self):
        self.windowB.withdraw()
        self.deiconify()
        self.save_cancel()

    def update_window_control(self):
        self.withdraw()
        self.ask_existing_number()

    def new_window_control(self):
        self.withdraw()
        self.create_new_customer_number()

    def form_close(self):
        self.master.deiconify()
        self.destroy()

    def save_cancel(self):
        self.savecontrol_frame.tkraise()


#####################
# New Customer Form #
#####################


class NewCustomerForm(tk.Frame):
    def __init__(self, master, customer_number, callbacks, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Self Config #
        ###############
        # self.master.bind_class('TEntry', '<KeyRelease>',
        #                        self.treated_untreated_calculation)
        self.callbacks = callbacks
        png_file = image.new_form
        self.configure(background='#fff')
        self.columnconfigure(0, weight=1)
        self.customer_values = m.Models()
        self.customer_number = customer_number
        self.autofill_var = tk.StringVar()
        self.customer_inputs = {}

        # Vars #
        ########
        self.customer_num_var = tk.StringVar()
        self.customer_num_var.set(self.customer_number)

        self.cca_price_var = tk.DoubleVar()
        self.cca_price_var.set('Enter Price')

        # Style #
        #########
        self.os = ttk.Style()
        self.os.theme_use('alt')
        self.os.configure('TLabel', background='#fff')
        self.os.configure('TFrame', background='#fff')

        # Images #
        ##########

        self.customer_num_logo = itk.PhotoImage(file=png_file['customer_num'])
        self.cca_price_logo = itk.PhotoImage(file=png_file['cca_price'])
        self.bundle_size_logo = itk.PhotoImage(file=png_file['bundle_size'])
        self.dimension_logo = itk.PhotoImage(file=png_file['dimension'])
        self.length_logo = itk.PhotoImage(file=png_file['length'])
        self.odd_even_logo = itk.PhotoImage(file=png_file['odd_even'])
        self.inclusions_logo = itk.PhotoImage(file=png_file['inclusions'])
        self.price_untreated_logo = itk.PhotoImage(
            file=png_file['price_untreated'])
        self.price_treated_logo = itk.PhotoImage(
            file=png_file['price_treated'])
        self.autofill_logo = itk.PhotoImage(file=png_file['auto_fill'])
        self.odd_even_items = itk.PhotoImage(file=png_file['odd_even_items'])
        self.show_button = itk.PhotoImage(file=png_file['show_button'])
        self.show_blank = itk.PhotoImage(file=png_file['show_blank'])

        # Frames #
        ##########
        self.customer_number_cca_frame = ttk.Frame(self)
        self.customer_number_cca_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6),
                                                       weight=1)
        self.customer_number_cca_frame.grid(row=0,
                                            column=0,
                                            columnspan=4,
                                            sticky='ew')
        self.customer_num_combine_frame = ttk.Frame(
            self.customer_number_cca_frame)
        self.customer_num_combine_frame.grid(row=0, column=0, sticky='w')

        self.cca_price_combine_frame = ttk.Frame(
            self.customer_number_cca_frame)
        self.cca_price_combine_frame.grid(row=0, column=1, sticky='w')

        self.heading_frame = ttk.Frame(self)
        self.heading_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.heading_frame.grid(row=1, pady=5, padx=10, sticky='ew')

        # Component Setup #
        ###############
        # customer number section
        self.customer_num = ttk.Label(self.customer_num_combine_frame,
                                      image=self.customer_num_logo)
        self.customer_num.grid(row=0, column=0)
        self.customer_num_entry = ttk.Label(self.customer_num_combine_frame,
                                            textvariable=self.customer_num_var)
        self.customer_num_entry.config(font=('TkDefault 12 normal'),
                                       relief=tk.SUNKEN,
                                       width=15,
                                       anchor=tk.CENTER,
                                       borderwidth=.5)

        self.customer_num_entry.grid(row=0, column=1)
        self.cca_price = ttk.Label(self.cca_price_combine_frame,
                                   image=self.cca_price_logo)
        self.cca_price.grid(row=0, column=3)
        self.cca_price_entry = w.My_EntryNum(self.cca_price_combine_frame,
                                             textvariable=self.cca_price_var,
                                             width=14,
                                             justify=tk.CENTER,
                                             font=('TkDefault 12 normal'))
        self.cca_price_entry.bind(
            '<Button-1>', func=lambda x: self.cca_price_entry.delete(0, 'end'))
        self.cca_price_entry.bind('<KeyRelease>', None)
        self.cca_price_entry.grid(row=0, column=4)

        # heading section
        self.bundle_size_label = ttk.Label(self.heading_frame,
                                           image=self.bundle_size_logo,
                                           anchor=tk.CENTER)
        self.bundle_size_label.grid(row=1, column=0, sticky='ew')

        self.dimension_label = ttk.Label(self.heading_frame,
                                         image=self.dimension_logo,
                                         anchor=tk.CENTER)
        self.dimension_label.grid(row=1, column=1, sticky='ew')

        self.length_label = ttk.Label(self.heading_frame,
                                      image=self.length_logo,
                                      anchor=tk.CENTER)
        self.length_label.grid(row=1, column=2, sticky='ew')

        self.odd_even_label = ttk.Label(self.heading_frame,
                                        image=self.odd_even_logo,
                                        anchor=tk.CENTER)
        self.odd_even_label.grid(row=1, column=3, sticky='ew')

        self.inclusions_label = ttk.Label(self.heading_frame,
                                          image=self.inclusions_logo,
                                          anchor=tk.CENTER)
        self.inclusions_label.grid(row=1, column=4, sticky='ew')

        self.price_untreated_label = ttk.Label(self.heading_frame,
                                               image=self.price_untreated_logo,
                                               anchor=tk.CENTER)
        self.price_untreated_label.grid(row=1, column=5, sticky='ew')

        self.price_treated_label = ttk.Label(self.heading_frame,
                                             image=self.price_treated_logo,
                                             anchor=tk.CENTER)
        self.price_treated_label.grid(row=1, column=6, sticky='ew')

        self.autofill_checkbutton = ttk.Checkbutton(
            self.cca_price_combine_frame,
            image=self.autofill_logo,
            variable=self.autofill_var,
            command=self.auto_fill)

        self.autofill_checkbutton.grid(row=0, column=2, sticky='ew', padx=10)

        if self.customer_number:
            self.populate_customer_template()

    def populate_customer_template(self):

        # Config Files #
        ################
        self.odd_dict = {
            '0': '_038_038',
            '3': '_038_050',
            '6': '_038_076',
            '9': '_038_114',
            '12': '_038_152',
            '15': '_038_228',
            '18': '_050_076',
            '21': '_050_152',
            '24': '_050_228',
            '27': '_076_228'
        }
        self.label_dict = {
            '_038_038': 0,
            '_038_050': 3,
            '_038_076': 6,
            '_038_114': 9,
            '_038_152': 12,
            '_038_228': 15,
            '_050_076': 18,
            '_050_152': 21,
            '_050_228': 24,
            '_076_228': 27,
        }

        # Styles #
        ##########
        self.os.configure('TCheckbutton',
                          background='#fff',
                          font=('TkDefault 12 normal'),
                          anchor=tk.CENTER)

        self.os.configure('Cell.TLabel',
                          background='#fff',
                          font=('TkDefault 12 normal'),
                          justify=tk.CENTER)

        self.os.configure('Even.TLabel',
                          background='#7FBF7F',
                          foreground='#fff',
                          font=('TkDefault 12 normal'),
                          justify=tk.CENTER)
        self.os.configure('Odd.TLabel',
                          background='#FFA64C',
                          foreground='#fff',
                          font=('TkDefault 12 normal'),
                          justify=tk.CENTER)

        self.os.configure('Check.TButton',
                          background='#fff',
                          justify=tk.CENTER,
                          anchor=tk.CENTER)

        # Columns #
        ###########
        self.length_cell = self.customer_values.template_custom['LENGTH']
        self.size_cell = self.customer_values.template_custom['SIZES']
        self.dimension_cell = self.customer_values.template_custom['DIMENSION']
        self.treated_cell = self.customer_values.template_custom['TREATED']
        self.untreated_cell = self.customer_values.template_custom['UNTREATED']
        self.odd_cell = self.customer_values.template_custom['ODD_EVEN']

        # Setup dictionary #
        ####################
        self.customer_inputs[self.customer_number] = {}
        self.customer_inputs[self.customer_number]['SIZES'] = {}
        self.customer_inputs[self.customer_number]['DIMENSION'] = {}
        self.customer_inputs[self.customer_number]['LENGTH'] = {}
        self.customer_inputs[self.customer_number]['SET ODD'] = {}
        self.customer_inputs[self.customer_number]['INCLUSIONS'] = {}
        self.customer_inputs[self.customer_number]['TREATED'] = {}
        self.customer_inputs[self.customer_number]['UNTREATED'] = {}
        self.customer_inputs[self.customer_number]['ODD_EVEN'] = {}
        self.customer_inputs[self.customer_number]['CHECK'] = {}

        # Size #
        ########
        for index, value in self.size_cell.items():
            row = int(index) + 2
            self.customer_inputs[
                self.customer_number]['SIZES'][index] = ttk.Label(
                    self.heading_frame,
                    text=self.size_cell[index],
                    anchor=tk.CENTER,
                    style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['SIZES'][index].grid(
                row=row, column=0, sticky='nsew')

        # Dimension #
        #############
        for index, value in self.dimension_cell.items():
            row = int(index) + 2
            self.customer_inputs[
                self.customer_number]['DIMENSION'][index] = ttk.Label(
                    self.heading_frame,
                    text=self.dimension_cell[index],
                    anchor=tk.CENTER,
                    style='Cell.TLabel')

            self.customer_inputs[
                self.customer_number]['DIMENSION'][index].grid(row=row,
                                                               column=1,
                                                               sticky='nsew')

        # Untreated #
        #############
        for index, value in self.untreated_cell.items():
            row = int(index) + 2
            self.customer_inputs[
                self.customer_number]['UNTREATED'][index] = w.My_EntryNum(
                    self.heading_frame,
                    textvariable=self.untreated_cell[index],
                    width=14,
                    justify=tk.CENTER,
                    font=('TkDefault 12 normal'))
            self.customer_inputs[
                self.customer_number]['UNTREATED'][index].grid(row=row,
                                                               column=5)

            # Key Bindings
            self.customer_inputs[
                self.customer_number]['UNTREATED'][index].bind(
                    '<KeyRelease>', self.treated_untreated_calculation)
            self.customer_inputs[
                self.customer_number]['UNTREATED'][index].bind(
                    '<KeyRelease-Return>',
                    lambda x: self.customer_inputs[self.customer_number][
                        'UNTREATED'][index].event_generate('<Tab>'))
            self.customer_inputs[
                self.customer_number]['UNTREATED'][index].bind(
                    '<KeyRelease-KP_Enter>',
                    lambda x: self.customer_inputs[self.customer_number][
                        'UNTREATED'][index].event_generate('<Tab>'))

        # Treated #
        ###########
        for index, value in self.treated_cell.items():
            row = int(index) + 2
            self.customer_inputs[
                self.customer_number]['TREATED'][index] = w.My_EntryNum(
                    self.heading_frame,
                    textvariable=self.treated_cell[index],
                    width=14,
                    justify=tk.CENTER,
                    font=('TkDefault 12 normal'))
            self.customer_inputs[self.customer_number]['TREATED'][index].grid(
                row=row, column=6)

            # Key Bindings
            self.customer_inputs[self.customer_number]['TREATED'][index].bind(
                '<KeyRelease-Return>',
                lambda x: self.customer_inputs[self.customer_number][
                    'TREATED'][index].event_generate('<Tab>'))
            self.customer_inputs[self.customer_number]['TREATED'][index].bind(
                '<KeyRelease-KP_Enter>',
                lambda x: self.customer_inputs[self.customer_number][
                    'TREATED'][index].event_generate('<Tab>'))

        # Set Odd/ Even #
        #################

        for index, value in self.odd_dict.items():
            row = int(index) + 2
            # self.odd_cell[value].trace('w', self.label_color_change)
            self.odd_cell[value].trace('w', self.set_length_label)

            self.customer_inputs[self.customer_number]['ODD_EVEN'][
                self.odd_dict[index]] = ttk.Checkbutton(
                    self.heading_frame,
                    variable=self.odd_cell[value],
                    onvalue=1,
                    offvalue='',
                    image=self.odd_even_items,
                    style='TCheckbutton')
            self.customer_inputs[self.customer_number]['ODD_EVEN'][
                self.odd_dict[index]].grid(row=row,
                                           rowspan=2,
                                           column=3,
                                           sticky='ew')

        # Check Sizes Buttons #
        #######################
        # '_038_038'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_038'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_038'),
                style='Check.TButton')
        self.customer_inputs[self.customer_number]['CHECK']['_038_038'].grid(
            row=4, column=3, sticky='w')
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_038_blank'] = ttk.Label(
                self.heading_frame, image=self.show_blank)
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_038_blank'].grid(
                row=4, column=3, sticky='nsew')

        # '_038_050'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_050'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_050'))
        self.customer_inputs[self.customer_number]['CHECK']['_038_050'].grid(
            row=7, column=3, sticky='w')
        # '_038_076'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_076'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_076'))
        self.customer_inputs[self.customer_number]['CHECK']['_038_076'].grid(
            row=10, column=3, sticky='w')
        # '_038_114'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_114'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_114'))
        self.customer_inputs[self.customer_number]['CHECK']['_038_114'].grid(
            row=13, column=3, sticky='w')
        # '_038_152'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_152'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_152'))
        self.customer_inputs[self.customer_number]['CHECK']['_038_152'].grid(
            row=16, column=3, sticky='w')
        # '_038_228'
        self.customer_inputs[
            self.customer_number]['CHECK']['_038_228'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_038_228'))
        self.customer_inputs[self.customer_number]['CHECK']['_038_228'].grid(
            row=19, column=3, sticky='w')
        # '_050_076'
        self.customer_inputs[
            self.customer_number]['CHECK']['_050_076'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_050_076'))
        self.customer_inputs[self.customer_number]['CHECK']['_050_076'].grid(
            row=22, column=3, sticky='w')
        # '_050_152'
        self.customer_inputs[
            self.customer_number]['CHECK']['_050_152'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_050_152'))
        self.customer_inputs[self.customer_number]['CHECK']['_050_152'].grid(
            row=25, column=3, sticky='w')
        # '_050_228'
        self.customer_inputs[
            self.customer_number]['CHECK']['_050_228'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_050_228'))
        self.customer_inputs[self.customer_number]['CHECK']['_050_228'].grid(
            row=28, column=3, sticky='w')
        # '_076_228'
        self.customer_inputs[
            self.customer_number]['CHECK']['_076_228'] = ttk.Button(
                self.heading_frame,
                image=self.show_button,
                command=lambda: self.check_size('_076_228'))
        self.customer_inputs[self.customer_number]['CHECK']['_076_228'].grid(
            row=31, column=3, sticky='w')

        # Length #
        ##########

        for index, values in self.length_cell.items():
            text = self.length_cell[index]['normal']
            row = int(index) + 2
            self.customer_inputs[
                self.customer_number]['LENGTH'][index] = ttk.Label(
                    self.heading_frame,
                    text=f'{text[0]} - {text[-1]}',
                    anchor=tk.CENTER,
                    style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['LENGTH'][index].grid(
                row=row, column=2, sticky='nsew')

    def check_size(self, size):
        print(size)

    def set_length_label(self, *args):

        index = self.label_dict[args[0]]
        valuea = self.odd_cell[args[0]].get()
        size_list_odd = self.length_cell[str(index)]['odd']
        size_list_even = self.length_cell[str(index)]['even']
        size_list_normal = self.length_cell[str(index)]['normal']

        size_list_odd_next_row = self.length_cell[str(index + 1)]['odd']
        size_list_even_next_row = self.length_cell[str(index + 1)]['even']
        size_list_normal_next_row = self.length_cell[str(index + 1)]['normal']

        if valuea == '1':
            self.customer_inputs[self.customer_number]['CHECK'][
                args[0]].tkraise()
            self.length_cell[str(index)]['set'].set(size_list_even)
            self.length_cell[str(index + 1)]['set'].set(size_list_odd_next_row)

            self.customer_inputs[self.customer_number]['LENGTH'][str(
                index)].config(text='Long EVENS')

            self.customer_inputs[self.customer_number]['LENGTH'][str(
                index + 1)].config(text='Long ODDS')

        else:
            self.customer_inputs[self.customer_number]['CHECK'][
                args[0] + '_blank'].tkraise()
            self.length_cell[str(index)]['set'].set(size_list_normal)
            self.length_cell[str(index +
                                 1)]['set'].set(size_list_normal_next_row)

            self.customer_inputs[self.customer_number]['LENGTH'][str(
                index)].config(
                    text=f'{size_list_normal[0]} - {size_list_normal[-1]}')
            self.customer_inputs[self.customer_number]['LENGTH'][str(
                index + 1
            )].config(
                text=
                f'{size_list_normal_next_row[0]} - {size_list_normal_next_row[-1]}'
            )

        # Label color change #
        temp = str(self.label_dict[args[0]]), str(self.label_dict[args[0]] + 1)
        value = self.odd_cell[args[0]].get()
        if value == '1':

            self.customer_inputs[self.customer_number]['SIZES'][
                temp[0]].config(style='Even.TLabel')
            self.customer_inputs[self.customer_number]['DIMENSION'][
                temp[0]].config(style='Even.TLabel')
            self.customer_inputs[self.customer_number]['LENGTH'][
                temp[0]].config(style='Even.TLabel')

            self.customer_inputs[self.customer_number]['SIZES'][
                temp[1]].config(style='Odd.TLabel')
            self.customer_inputs[self.customer_number]['DIMENSION'][
                temp[1]].config(style='Odd.TLabel')
            self.customer_inputs[self.customer_number]['LENGTH'][
                temp[1]].config(style='Odd.TLabel')

        else:

            self.customer_inputs[self.customer_number]['SIZES'][
                temp[0]].config(style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['DIMENSION'][
                temp[0]].config(style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['LENGTH'][
                temp[0]].config(style='Cell.TLabel')

            self.customer_inputs[self.customer_number]['SIZES'][
                temp[1]].config(style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['DIMENSION'][
                temp[1]].config(style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['LENGTH'][
                temp[1]].config(style='Cell.TLabel')
            self.customer_inputs[self.customer_number]['ODD_EVEN'][
                args[0]].config(state=tk.ACTIVE)

    def auto_fill(self):
        if self.autofill_var.get() == '1':
            self.calculation_flag = True
            for value in self.customer_inputs[self.customer_number]['TREATED']:
                self.customer_inputs[
                    self.customer_number]['TREATED'][value].config(
                        state=tk.DISABLED)

        else:
            for value in self.customer_inputs[self.customer_number]['TREATED']:
                self.customer_inputs[
                    self.customer_number]['TREATED'][value].config(
                        state=tk.ACTIVE)

    def treated_untreated_calculation(self, *args, **kwargs):
        if self.autofill_var.get() == '1':
            for index in self.customer_inputs[self.customer_number]['TREATED']:
                try:
                    self.treated_cell[index].set(
                        int(self.untreated_cell[index].get()) +
                        int(self.cca_price_var.get()))
                    l = [int(x) for x in self.untreated_cell[index].get()]
                    if sum(l) < 1:
                        self.treated_cell[index].set('0')

                except:
                    pass

    # TODO: Continue here


#################
# TreeView Form #
#################
class TreeViewSetup(ttk.Treeview):
    def __init__(self, master, callbacks, dataframe, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Self Variables #
        ##################
        self.dataframe = dataframe
        self.callbacks = callbacks
        self.columns = [x.upper() for x in list(dataframe.columns)]

        # Build Tree #
        ##############
