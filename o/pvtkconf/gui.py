# gui.py, part for parse_video : a fork from parseVideo. 
# gui: o/pvtkconf: parse_video Tk config GUI, main window. 
# version 0.0.0.1 test201507071003
# author sceext <sceext@foxmail.com> 2009EisF2015, 2015.07. 
# copyright 2015 sceext
#
# This is FREE SOFTWARE, released under GNU GPLv3+ 
# please see README.md and LICENSE for more information. 
#
#    parse_video : a fork from parseVideo. 
#    Copyright (C) 2015 sceext <sceext@foxmail.com> 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# import

from tkinter import *
from tkinter.ttk import *

import tkinter as TK
import tkinter.ttk as ttk
import tkinter.font as TKfont
import tkinter.tix as tix
import tkinter.filedialog as TKfile

from ..gui import tk_base

from . import confd

# global vars

# function

# class

# main window
class MainWin(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        self.root = None	# root window
        
        # widget gui part
        self.b_refresh = None	# refresh Button
        self.b_save = None	# save setting Button
        
        self.v_enable_proxy = None	# 
        self.v_http_proxy = None	# http_proxy text StringVar
        
        self.v_pvtkgui_ui_type = None	# pvtkgui ui_type StringVar
        
        self.v_gen_cookie_text = None	# gen_cookie_text StringVar
    
    # operations
    
    # event list to send
    # TODO
    
    def _send(self, event, data):
        # DEBUG info
        print('pvtkconf: gui: MainWin send event [' + str(event) + '], ' + str(data) + ' ')
        # do send it
        super()._send(event, data)
    
    # on sub el
    # TODO
    
    # start main loop
    def mainloop(self):
        mainloop()
    
    # create main UI
    def start(self):
        self._create()
        self._set_el()
    
    def _create(self):
        # create root window
        root = tix.Tk()
        self.root = root
        
        # create sub part
        # TODO
    
    def _set_el(self):
        pass
    
    # end MainWin class

# end gui.py



