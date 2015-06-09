# gui_setting.py, part for parse_video : a fork from parseVideo. 
# gui_setting: o/ffmpeg_tkgui/gui_setting: PartSetting for ffmpeg Tk GUI. 
# version 0.0.3.0 test201506091957
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

TOP_PART_TITLE = '常用'
TOP_PART_TITLE_RIGHT = '(常用设置会自动保存)'
BOTTOM_PART_TITLE = '高级'
BOTTOM_PART_TITLE_BUTTON_TEXT = ['刷新', '保存高级设置']

TOP_ITEM1_TEXT = ['默认输出目录', '更改']
TOP_ITEM2_TEXT = ['自动更改默认输出目录为最后一次的输出目录', ['    开启    ', '    关闭    ']]

BITEM_TEXT1 = ['ffmpeg 可执行文件', '更改']
BITEM_TEXT2 = ['临时文件目录', '更改']
BITEM_TEXT3 = '生成的 ffmpeg 列表文件名'
BITEM_TEXT4 = ['最后一次添加文件目录', '更改']
BITEM_TEXT5 = ['最后一次导入列表文件目录', '更改']
BITEM_TEXT6 = ['最后一次合并输出目录', '更改']

# functions

# class

# setting part
class PartSetting(object):
    
    def __init__(self):
        self.parent = None
        
        self.host_t = None	# host TextBox
        self.host_f = None	# host frame
        
        self.top = None	# top part
        self.b = None	# bottom part
        
        self.callback = None	# event callback(type)
        # type in []
    
    def _send(self, event=None):
        pass
    
    # TODO on sub event
    
    def start(self, parent, font=None):
        # create style
        style = Style()
        style.configure('MyTitle.TLabel', font=('', 20, 'bold'))
        
        # create sub
        host_t = tix.ScrolledWindow(parent, scrollbar='auto')
        self.parent = parent
        self.host_t = host_t
        host_f = tix.Frame(host_t.window)
        host_f.pack(side=TOP, fill=X, expand=False)
        self.host_f = host_f
        
        top = TopBox()
        self.top = top
        
        b = BottomBox()
        self.b = b
        
        # pack it
        host_t.pack(side=TOP, fill=BOTH, expand=True)
        
        f1 = Frame(host_f)
        top.start(f1, font=font)
        f1.pack(side=TOP, fill=X, expand=False)
        
        s1 = Separator(host_f, orient=HORIZONTAL, style='TSeparator')
        s1.pack(side=TOP, fill=X, expand=False, pady=13)
        
        f2 = Frame(host_f)
        b.start(f2, font=font)
        f2.pack(side=TOP, fill=X, expand=False)
        
        # TODO set callbacks
        
        # create UI done
    
    # end PartSetting class

# top part, frequently settings
class TopBox(object):
    
    def __init__(self):
        self.parent = None
        self.t = None	# TopBoxTitle
        
        self.item_default_output = None	# default output dir
        self.item_auto_dir1 = None	# auto change defualt output dir to last used
        
        self.callback = None	# event callback(type)
        # event in ['change_output', 'change_auto_switch']
    
    def _send(self, event=None):
        pass
    
    def _on_change_output_dir(self, event=None):
        pass
    
    def _on_change_auto_switch(self, event=None):
        pass
    
    def start(self, parent, font=None):
        # create sub
        t = TopBoxTitle()
        item_d = gui_base.LabelEntryButton()
        item_a = gui_base.LabelSwitchBox()
        self.parent = parent
        self.t = t
        self.item_default_output = item_d
        self.item_auto_dir1 = item_a
        
        # pack it
        f1 = Frame(parent)
        t.start(f1)
        f2 = Frame(parent)
        item_d.start(f2, label_text=TOP_ITEM1_TEXT[0], button_text=TOP_ITEM1_TEXT[1], font=font)
        f3 = Frame(parent)
        item_a.start(f3, label_text=TOP_ITEM2_TEXT[0], switch_text=TOP_ITEM2_TEXT[1])
        
        f1.pack(side=TOP, fill=X, expand=False)
        f2.pack(side=TOP, fill=X, expand=False)
        f3.pack(side=TOP, fill=X, expand=False)
        
        # set callback
        # TODO
        
        # create UI done
    
    # end TopBox class

# top part title
class TopBoxTitle(object):
    
    def __init__(self):
        self.parent = None
        self.l1 = None	# top title left label
        self.l2 = None	# top title right label
    
    def start(self, parent):
        # create element
        l1 = Label(parent, text=TOP_PART_TITLE, style='MyTitle.TLabel')
        l2 = Label(parent, text=TOP_PART_TITLE_RIGHT)
        self.parent = parent
        self.l1 = l1
        self.l2 = l2
        
        # pack it
        l1.pack(side=LEFT, fill=Y, expand=False)
        l2.pack(side=RIGHT, fill=Y, expand=False)
        
        # create UI done
    
    # end TopBoxTitle class

# bottom part, advanced settings
class BottomBox(object):
    
    def __init__(self):
        self.parent = None
        self.t = None	# BottomBoxTitle
        
        self.item_ffmpeg_bin = None	# set ffmpeg bin file path
        self.item_tmp_path = None	# set tmp file path
        self.item_list_name = None	# output tmp file, ffmpeg list file
        self.item_last_add_file = None	# last add file path dir
        self.item_last_import_list = None	# last import list file path dir
        self.item_last_output = None	# last output merged file dir
    
    # set callbacks, TODO
    
    def start(self, parent, font=None):
        # create obj
        t = BottomBoxTitle()
        item1 = gui_base.LabelEntryButton()
        item2 = gui_base.LabelEntryButton()
        item3 = gui_base.LabelEntryBox()
        item4 = gui_base.LabelEntryButton()
        item5 = gui_base.LabelEntryButton()
        item6 = gui_base.LabelEntryButton()
        # save it
        self.parent = parent
        self.t = t
        self.item_ffmpeg_bin = item1
        self.item_tmp_path = item2
        self.item_list_name = item3
        self.item_last_add_file = item4
        self.itme_last_import_list = item5
        self.item_last_output = item6
        
        # pack it
        f1 = Frame(parent)
        t.start(f1)
        f1.pack(side=TOP, fill=X, expand=False)
        
        f2 = Frame(parent)
        item1.start(f2, label_text=BITEM_TEXT1[0], button_text=BITEM_TEXT1[1], font=font)
        f2.pack(side=TOP, fill=X, expand=False)
        
        f3 = Frame(parent)
        item2.start(f3, label_text=BITEM_TEXT2[0], button_text=BITEM_TEXT2[1], font=font)
        f3.pack(side=TOP, fill=X, expand=False)
        
        f4 = Frame(parent)
        item3.start(f4, label_text=BITEM_TEXT3, font=font)
        f4.pack(side=TOP, fill=X, expand=False)
        
        f5 = Frame(parent)
        item4.start(f5, label_text=BITEM_TEXT4[0], button_text=BITEM_TEXT4[1], font=font)
        f5.pack(side=TOP, fill=X, expand=False)
        
        f6 = Frame(parent)
        item5.start(f6, label_text=BITEM_TEXT5[0], button_text=BITEM_TEXT5[1], font=font)
        f6.pack(side=TOP, fill=X, expand=False)
        
        f7 = Frame(parent)
        item6.start(f7, label_text=BITEM_TEXT6[0], button_text=BITEM_TEXT6[1], font=font)
        f7.pack(side=TOP, fill=X, expand=False)
        
        # TODO
        
        # create UI done
    
    # end BottomBox class

# bottom part title
class BottomBoxTitle(object):
    
    def __init__(self):
        self.parent = None
        self.l = None	# title Label
        self.b_refresh = None	# refresh button
        self.b_save = None	# save setting button
        
        self.callback = None	# event callback
        # event in ['b_refresh', 'b_save']
    
    def _send(self, event=None):
        if self.callback != None:
            self.callback(event)
    
    def _on_sub_refresh(self, event=None):
        self._send('b_refresh')
    
    def _on_sub_save(self, event=None):
        self._send('b_save')
    
    def start(self, parent):
        # create obj
        l = Label(parent, text=BOTTOM_PART_TITLE, style='MyTitle.TLabel')
        b1 = Button(parent, command=self._on_sub_refresh, text=BOTTOM_PART_TITLE_BUTTON_TEXT[0])
        b2 = Button(parent, command=self._on_sub_save, text=BOTTOM_PART_TITLE_BUTTON_TEXT[1])
        self.parent = parent
        self.l = l
        self.b_refresh = b1
        self.b_save = b2
        
        # pack it
        l.pack(side=LEFT, fill=Y, expand=False)
        b2.pack(side=RIGHT, fill=Y, expand=False)
        b1.pack(side=RIGHT, fill=Y, expand=False)
        
        # create UI done
    
    # end BottomBoxTitle class

# end gui_setting.py


