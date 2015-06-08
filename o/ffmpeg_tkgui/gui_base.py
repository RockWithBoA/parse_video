# gui_base.py, part for parse_video : a fork from parseVideo. 
# gui_base: o/ffmpeg_tkgui/gui_base: base part for ffmpeg Tk GUI. 
# version 0.0.1.0 test201506082057
# author sceext <sceext@foxmail.com> 2009EisF2015, 2015.06. 
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
from tkinter import tix, font, filedialog

# global vars

# functions

# class

# entry box, easy text Entry support
class EntryBox(object):
    
    def __init__(self):
        self.parent = None
        self.e = None	# Entry
        self.v = None	# StringVar
    
    # create sub elements
    def start(self, parent, font=None, style='TEntry'):
        # create UI
        v = StringVar()
        e = Entry(parent, textvariable=v, font=font, style=style)
        # NOTE should be pack
        # save it
        self.parent = parent
        self.v = v
        self.e = e
        # create UI done
    
    # entry operations
    def get_text(self):
        return self.v.get()
    
    def set_text(self, text):
        self.v.set(text)
    
    # end EntryBox class

# text part, TextBox, Text and Scrollbars, simple text part
class TextBox(object):
    
    def __init__(self):
        self.parent = None	# parent element
        
        self.t = None	# Text
        self.sx = None	# x Scrollbar
        self.sy = None	# y Scrollbar
        
        # init end
    
    # start create sub elements
    def start(self, parent, font=None, bg='#ddd', fg='#333'):	# parent element
        # create UI
        sx = Scrollbar(parent, orient=HORIZONTAL)
        sy = Scrollbar(parent, orient=VERTICAL)
        t = Text(parent, wrap=NONE, font=font, padx=0, pady=0, relief=FLAT, bd=0, bg=bg, fg=fg)
        
        # pack it
        sy.pack(side=RIGHT, fill=Y)
        sx.pack(side=BOTTOM, fill=X)
        t.pack(side=TOP, fill=BOTH, expand=True)
        # set scrollbar
        sx.config(command=t.xview)
        sy.config(command=t.yview)
        t.config(xscrollcommand=sx.set)
        t.config(yscrollcommand=sy.set)
        
        # save it
        self.parent = parent
        self.t = t
        self.sx = sx
        self.sy = sy
        # create UI done
    
    # text part operations
    def enable(self):
        self.t.config(state=NORMAL)
    
    def disable(self):
        self.t.config(state=DISABLED)
    
    def get_text(self):	# get all text
        return self.t.get('1.0', END)
    
    def clear(self):	# delete all text
        self.t.delete('1.0', END)
    
    def add_text(self, text='', pos=END):
        self.t.insert(pos, text)
    
    # end TextBox class

# end gui_base.py


