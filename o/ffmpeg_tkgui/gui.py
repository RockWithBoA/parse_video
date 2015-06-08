# gui.py, part for parse_video : a fork from parseVideo. 
# gui: o/ffmpeg_tkgui/gui: parse_video Tk GUI, main gui file. 
# version 0.0.3.0 test201506082029
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

TEXT_MAIN_FONT_SIZE = 16	# 16px
MAIN_WIN_TITLE = 'ffmpeg Tk GUI,  ffmpeg 图形界面 (parse_video) 1 '
MAIN_FONT_NAME = '微软雅黑'
MAIN_PAGE_NAME = [
    '  合 并  ', 
    '  日 志  ', 
    '  设 置  ', 
    '  帮 助  ', 
]

# functions

# class

# main window
class MainWin(object):
    
    def __init__(self):
        self.root = None	# root window
        self.nb = None		# tkinter.ttk Notebook
        self.p = []		# Notebook pages
        self.pf = []		# Notebook pages Frames
        
        # TODO
        
        # __init__ done
    
    # start create and show main window
    def start(self):
        # create root window
        root = Tk()
        self.root = root
        # set main window title
        root.title(MAIN_WIN_TITLE)
        
        # create fonts and set styles
        mf = font.Font(root, size=TEXT_MAIN_FONT_SIZE)	# main font
        style = Style()
        style.configure('.', font=(MAIN_FONT_NAME, TEXT_MAIN_FONT_SIZE))
        style.configure('My.TEntry', padding=5)
        
        # create Notebook and each pages
        nb = Notebook(root, padding=0)
        self.nb = nb
        # create each page with name
        for i in range(len(MAIN_PAGE_NAME)):
            pf = Frame(nb)
            nb.add(pf, text=MAIN_PAGE_NAME[i])
            self.pf.append(pf)
        # create sub part
        pf = self.pf
        # create merge
        p = PartMerge()
        p.start(pf[0])
        self.p.append(p)
        # create log
        p = PartLog()
        p.start(pf[1], font=mf)
        self.p.append(p)
        # create Setting
        p = PartSetting()
        p.start(pf[2])
        self.p.append(p)
        # create about part
        p = PartAbout()
        p.start(pf[3], font=mf)
        self.p.append(p)
        
        # pack main Notebook
        nb.pack(side=TOP, fill=BOTH, expand=True)
        # TODO
        # create UI done
    
    # show one notebook page
    def show_page(self, p_n):
        # TODO
        pass
    
    # start main loop
    def mainloop(self):
        # just start main loop
        mainloop()
    
    # end MainWin class

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

# merge part
class PartMerge(object):
    
    def __init__(self):
        self.parent = None
        pass
    
    def start(self, parent):
        pass
    
    # end PartMerge class

# log part
class PartLog(object):
    
    def __init__(self):
        self.parent = None
        
        self.t = None	# TextBox
        
    
    def start(self, parent, font=None):
        
        # just create TextBox
        self.t = TextBox()
        self.t.start(parent, font=font)
        # TODO
        pass
    
    # end PartLog class

# setting part
class PartSetting(object):
    
    def __init__(self):
        self.parent = None
        pass
    
    def start(self, parent):
        pass
    
    # end PartSetting class

# about part
class PartAbout(object):
    
    def __init__(self):
        self.parent = None
        
        self.t = None	# sub TextBox
    
    def start(self, parent, font=None):
        # just create TextBox
        self.t = TextBox()
        self.t.start(parent, font=font)
        # TODO
        pass
    
    # end PartAbout class

# debug
def test():
    # just create and show UI
    w = MainWin()
    w.start()
    # start mainloop
    w.mainloop()
    # test done

# auto start test
if __name__ == '__main__':
    test()

# end gui.py


