# gui_base.py, part for parse_video : a fork from parseVideo. 
# gui_base: o/ffmpeg_tkgui/gui_base: base part for ffmpeg Tk GUI. 
# version 0.0.8.0 test201506091254
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
    
    # insert a frame in text, and return that frame
    def insert_frame(self):
        t = self.t
        f = Frame(t)
        t.window_create(END, window=f)
        f.pack(side=TOP, fill=BOTH, expand=True)
        # done
        return f
    
    # end TextBox class

# label, entry, button three obj in one line
class LabelEntryButton(object):
    
    def __init__(self):
        self.parent = None
        self.l = None	# Label
        self.e = None	# EntryBox
        self.b = None	# Button
        
        self.callback_b = None	# Button click callback
    
    def start(self, parent, label_text='', button_text='', font=None):
        # create sub obj
        b = Button(parent, command=self._on_button_click, text=button_text, style='TButton')
        e = EntryBox()
        l = Label(parent, text=label_text, font=font)
        # pack element
        l.pack(side=LEFT, fill=Y, expand=False)
        b.pack(side=RIGHT, fill=Y, expand=False)
        e.start(parent, font=font)
        e.e.pack(side=LEFT, fill=BOTH, expand=True)
        
        # save it
        self.l = l
        self.e = e
        self.b = b
        # create UI done
    
    # event callbacks
    def _on_button_click(self, event=None):
        if self.callback_b != None:
            self.callback_b()
    
    # operactions
    def get_text(self):
        return self.e.get_text()
    
    def set_text(self, text=''):
        self.e.set_text(text)
    
    # end LabelEntryButton class

# LabelEntry, no Button
class LabelEntryBox(object):
    
    def __init__(self):
        self.parent = None
        self.l = None	# Label
        self.e = None	# EntryBox
    
    def start(self, parent, label_text='', font=None):
        # create sub obj
        e = EntryBox()
        l = Label(parent, text=label_text, font=font)
        # pack element
        l.pack(side=LEFT, fill=Y, expand=False)
        e.start(parent, font=font)
        e.e.pack(side=RIGHT, fill=BOTH, expand=True)
        
        # save it
        self.parent = parent
        self.l = l
        self.e = e
        # create UI done
    
    # operactions
    def get_text(self):
        return self.e.get_text()
    
    def set_text(self, text=''):
        self.e.set_text(text)
    
    # end LabelEntryBox class

# SwitchLabelBox class
class SwitchLabelBox(object):
    
    def __init__(self):
        self.parent = None
        self.l = []	# labels
        
        self.callback = None	# event callback(), status changed callback
        
        self._status = 0
    
    def _send(self, e_type=None):
        if self.callback != None:
            self.callback(e_type)
    
    def _on_sub_click0(self, event=None):
        # check status change
        if self._status == 0:
            return	# nothing to do
        # set status and send callback
        self.set_status(0)
        self._send()
        # process end
    
    def _on_sub_click1(self, event=None):
        # check status change
        if self._status == 1:
            return	# nothing to do
        # set status and send callback
        self.set_status(1)
        self._send()
        # process end
    
    def start(self, parent, text=['', ''], status=0):
        # create sub Label
        l0 = Label(parent, text=text[0])
        l1 = Label(parent, text=text[1])
        self.l.append(l0)
        self.l.append(l1)
        self.parent = parent
        # create styles
        style = Style()
        style.configure('SwitchLabelBoxOff.TLabel', background='#ccc', foreground='#444')
        style.configure('SwitchLabelBoxOn.TLabel', background='#00f', foreground='#fff')
        # set default status
        self.set_status(status)
        # pack sub
        l0.pack(side=LEFT, fill=BOTH, expand=True)
        l1.pack(side=RIGHT, fill=BOTH, expand=True)
        # add event callback
        l0.bind('<Button-1>', self._on_sub_click0)
        l1.bind('<Button-1>', self._on_sub_click1)
        # create UI done
    
    # operations
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        l0 = self.l[0]
        l1 = self.l[1]
        # set default style
        l0.config(style='SwitchLabelBoxOff.TLabel')
        l1.config(style='SwitchLabelBoxOff.TLabel')
        # set on style
        self.l[status].config(style='SwitchLabelBoxOn.TLabel')
        self._status = status
        # set status done
    
    # end SwitchLabelBox class

# LabelSwitch, Label with a SwitchLabelBox
class LabelSwitchBox(object):
    
    def __init__(self):
        self.parent = None
        self.l = None	# Label
        self.s = None	# SwitchLabelBox
        
        self.callback = None
    
    def _send(self, event=None):
        if self.callback != None:
            self.callback()
    
    def _on_sub_event(self, event=None):
        self._send(event)
    
    def start(self, parent, label_text='', switch_text=['', '']):
        # create obj
        l = Label(parent, text=label_text)
        s = SwitchLabelBox()
        self.parent = parent
        self.l = l
        self.s = s
        # pack obj
        l.pack(side=LEFT, fill=Y, expand=False)
        f = Frame(parent)
        s.start(f, text=switch_text)
        f.pack(side=RIGHT, fill=Y, expand=False)
        # set callback
        s.callback = self._on_sub_event
        
        # create UI done
    
    # operations
    def get_status(self):
        return self.s.get_status()
    
    def set_status(self, status=0):
        self.s.set_status(status)
    
    # end LabelSwitchBox class

# end gui_base.py


