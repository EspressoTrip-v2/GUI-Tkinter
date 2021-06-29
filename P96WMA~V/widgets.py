import tkinter as tk
from tkinter import ttk, messagebox

##################################
# Validation Classes for widgets #
##################################

# Types Validation #
####################
# %d = Action code
# %i = index of the inserted text
# %P = The proposed validated text
# %s = text before the change
# %S = cause of call (insertion, deletion)
# %v = current value of widgets validate option
# %V = reason for the callback
# %W = the name of the widget


class Validation:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        vcmd = self.register(self._valid_func)
        invcmd = self.register(self._invalid_func)

        self.config(validate='key',
                    validatecommand=(vcmd, '%S', '%P', '%V', '%i', '%d'),
                    invalidcommand=(invcmd, '%P'))

    def _valid_func(self, what, proposed, event, index, action):
        if event == 'key':
            return self._key_validate(what, proposed, event, index, action)

    def _invalid_func(self, proposed):
        return False

    def _key_validate(self, what, proposed, event, index, action):
        return True


class My_EntryAlpha(Validation, ttk.Entry):

    # Validation Functions #
    ########################
    def _key_validate(self, what, proposed, event, index, action):
        if what in [
                '-', '_', '?', '#', '!', '$', '^', '*', '(', ')', '+', '=',
                '/', '<', ',', '.'
        ]:
            return False
        else:
            return True


class My_EntryNum(Validation, ttk.Entry):

    # Validation Functions #
    ########################
    def _key_validate(self, what, proposed, event, index, action):
        if what in [
                '-', '_', '?', '#', '!', '$', '^', '*', '(', ')', '+', '=',
                '/', '<', ',', '&', '.'
        ]:
            return False

        if what.isalpha():
            return False

        if len(proposed) > 8:
            return False

        else:
            return True
