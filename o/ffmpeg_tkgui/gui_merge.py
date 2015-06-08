# gui_merge.py, part for parse_video : a fork from parseVideo. 
# gui_merge: o/ffmpeg_tkgui/gui_merge: PartMerge for ffmpeg Tk GUI. 
# version 0.0.2.0 test201506082218
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

from . import gui_base

# global vars

BUTTON_BAR_TEXT = [
    '添加文件', 
    '上移', 
    '下移', 
    '按文件名排序', 
    '删除选定', 
]

BOTTOM_OUT_TEXT = ['合并输出', '更改']
BOTTOM_LIST_TEXT = ['列表文件', '导入']
BOTTOM_START_BUTTON_TEXT = '  开 始 合 并  '

# functions

# class

# merge part
class PartMerge(object):
    
    def __init__(self):
        self.parent = None
        
        self.top_bar = None	# TopButtonBar
        self.main_list = None	# MainFileList
        self.bp = None	# ButtonPart
        
        self.callback = None	# event callback(e_type)
        # e_type in []	# TODO
        
        pass
    
    def _send(self, e_type):
        pass	# TODO
    
    # TODO on sub event
    
    def start(self, parent, font=None):
        # creat obj
        top = TopButtonBar()
        mlist = MainFileList()
        bp = BottomPart()
        # pack obj
        f1 = Frame(parent)
        top.start(top)
        f1.pack(side=TOP, fill=X, expand=False)
        
        f2 = Frame(parent)
        mlist.start(f2)
        f2.pack(side=TOP, fill=BOTH, expand=True)
        
        f3 = Frame(parent)
        bp.start(f3, font=font)
        f3.pack(side=BOTTOM, fill=X, expand=False)
        
        # set callback
        # TODO
        
        # save it
        self.top_bar = top
        self.main_list = mlist
        self.bp = bp
        
        # create ui done
        pass
    
    # operations TODO
    
    # end PartMerge class

# top button bar
class TopButtonBar(object):
    
    def __init__(self):
        self.parent = None
        
        self.b_add_file = None	# Button add files
        self.b_move_up = None	# move selected item up
        self.b_move_down = None	# move selected item down
        self.b_sort_by_filename = None	# sort items by file name
        self.b_delete_selected = None	# delete selected
        
        self.callback_b = None	# one button be clicked callback(b_type)
        # b_type in ['b_add_file', 'b_move_up', 'b_move_down', 'b_sort_by_filename', 'b_delete_selected']
    
    # send event
    def _send_event(self, b_type):
        # DEBUG info
        print('DEBUG: gui.PartMerge.TopButtonBar send event \"' + b_type + '\"')
        # check callback
        if self.callback_b != None:
            self.callback_b(b_type)
        # done
    
    # on button clicked
    def _on_b_add_file(self, event=None):
        self._send_event('b_add_file')
    
    def _on_b_move_up(self, event=None):
        self._send_event('b_move_up')
    
    def _on_b_move_down(self, event=None):
        self._send_event('b_move_down')
    
    def _on_b_sort_by_filename(self, event=None):
        self._send_event('b_sort_by_filename')
    
    def _on_b_delete_selected(self, event=None):
        self._send_event('b_delete_selected')
    
    # create ui
    def start(self, parent):
        # create obj
        b1 = Button(parent, command=self._on_b_add_file, text=BUTTON_BAR_TEXT[0], style='TButton')
        b2 = Button(parent, command=self._on_b_move_up, text=BUTTON_BAR_TEXT[1], style='TButton')
        b3 = Button(parent, command=self._on_b_move_down, text=BUTTON_BAR_TEXT[2], style='TButton')
        b4 = Button(parent, command=self._on_b_sort_by_filename, text=BUTTON_BAR_TEXT[3], style='TButton')
        b5 = Button(parent, command=self._on_b_delete_selected, text=BUTTON_BAR_TEXT[4], style='TButton')
        
        # pack obj
        b1.pack(side=LEFT, fill=Y, expand=False)
        
        # add one Separator
        s = Separator(parent, orient=VERTICAL)
        s.pack(side=LEFT, fill=Y, expand=False)
        
        b2.pack(side=LEFT, fill=Y, expand=False)
        b3.pack(side=LEFT, fill=Y, expand=False)
        
        # add one Separator
        s = Separator(parent, orient=VERTICAL)
        s.pack(side=LEFT, fill=Y, expand=False)
        
        b4.pack(side=LEFT, fill=Y, expand=False)
        
        b5.pack(side=RIGHT, fill=Y, expand=False)
        
        # add one Separator
        s = Separator(parent, orient=VERTICAL)
        s.pack(side=RIGHT, fill=Y, expand=False)
        
        # save it
        self.b_add_file = b1
        self.b_move_up = b2
        self.b_move_down = b3
        self.b_sort_by_filename = b4
        self.b_delete_selected = b5
        
        # create ui done
    
    # operations
    # TODO
    
    # end TopButtonBar class

# main file list, TODO very important part
class MainFileList(object):
    
    def __init__(self):
        self.parent = None
        pass
    
    def start(self, parent):
        pass
    
    # end MainFileList class

# bottom part
class BottomPart(object):
    
    def __init__(self):
        self.parent = None
        
        self.bar_output = None	# output file name, bar
        self.bar_listfile = None	# ffmpeg list file, bar
        self.button_start = None	# start merge button
        
        self.callback = None	# common event callback(e_type)
        # e_type in ['change_out', 'import_list', 'start_merge']
        #	change output file button
        #	import ffmpeg list file button
        #	start merge button
    
    def _send(self, e_type):
        # DEBUG info
        print('DEBUG: gui.PartMerge.BottomPart send event \"' + e_type + '\"')
        # check callback
        if self.callback != None:
            self.callback(e_type)
    
    def _on_button_start(self, event=None):
        self._send('start_merge')
    
    def _on_button_output(self, event=None):
        self._send('change_out')
    
    def _on_button_list(self, event=None):
        self._send('import_list')
    
    # create ui
    def start(self, parent, font=None):
        # create obj
        out = gui_base.LabelEntryButton()
        listf = gui_base.LabelEntryButton()
        bstart = Button(parent, command=self._on_button_start, text=BOTTOM_START_BUTTON_TEXT, style='TButton')
        
        # pack obj
        f1 = Frame(parent)
        f2 = Frame(parent)
        out.start(f1, label_text=BOTTOM_OUT_TEXT[0], button_text=BOTTOM_OUT_TEXT[1], font=font)
        f1.pack(side=TOP, fill=X, expand=False)
        listf.start(f2, label_text=BOTTOM_LIST_TEXT[0], button_text=BOTTOM_LIST_TEXT[1], font=font)
        f2.pack(side=TOP, fill=X, expand=False)
        
        bstart.pack(side=BOTTOM, fill=BOTH, expand=True)
        
        # set callback
        out.callback_b = self._on_button_output
        out.callback_b = self._on_button_list
        
        # save obj
        self.bar_output = out
        self.bar_listfile = listf
        self.button_start = bstart
        
        # create ui done
    
    # operations
    def get_output_filename(self):
        out = self.bar_output
        return out.get_text()
    
    def set_output_filename(self, text=''):
        out = self.bar_output
        out.set_text(text)
    
    def get_listfilename(self):
        listf = self.bar_listfile
        return listf.get_text()
    
    def set_listfilename(self, text=''):
        listf = self.bar_listfile
        listf.set_text(text)
    
    # end BottomPart class

# end gui_merge.py


