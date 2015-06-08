# gui.py, part for parse_video : a fork from parseVideo. 
# gui: o/ffmpeg_tkgui/gui: parse_video Tk GUI, main gui file. 
# version 0.0.5.0 test201506082219
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
from . import gui_merge
from . import gui_setting

# global vars

TEXT_MAIN_FONT_SIZE = 16	# 16px
MAIN_WIN_TITLE = 'ffmpeg Tk GUI,  ffmpeg 图形界面 (parse_video) 1 '
MAIN_FONT_NAME = '微软雅黑'
MAIN_PAGE_NAME = [
    '    合 并                ', 
    '    日 志                ', 
    '    设 置                ', 
    '    帮 助                ', 
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
        style.configure('TEntry', padding=5)
        
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
        p = gui_merge.PartMerge()
        p.start(pf[0], font=mf)
        self.p.append(p)
        # create log
        p = PartLog()
        p.start(pf[1], font=mf)
        self.p.append(p)
        # create Setting
        p = gui_setting.PartSetting()
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

# log part
class PartLog(object):
    
    def __init__(self):
        self.parent = None
        
        self.t = None	# TextBox
    
    def start(self, parent, font=None):
        
        # just create TextBox
        self.t = gui_base.TextBox()
        self.t.start(parent, font=font)
        # set log init text
        t = self.t
        t.enable()
        t.clear()
        t.add_text(PART_LOG_INIT_TEXT)
        # create UI done
    
    def log_time(self):
        # TODO
        pass
    
    def log_text(self, text=''):
        # just write text
        t = self.t
        t.add_text(text)
    
    # end PartLog class

# PartLog init text
PART_LOG_INIT_TEXT = '''
日志: 以下显示的是 ffmpeg 图形界面 (本程序) 运行过程中产生的日志信息文本. 
=====================================================================

'''

# about part
class PartAbout(object):
    
    def __init__(self):
        self.parent = None
        
        self.t = None	# sub TextBox
    
    def start(self, parent, font=None):
        # just create TextBox
        self.t = gui_base.TextBox()
        self.t.start(parent, font=font)
        # set main text
        t = self.t
        t.enable()
        t.clear()
        t.add_text(PART_ABOUT_TEXT)
        t.disable()
        # create UI done
    
    # end PartAbout class

# About text
PART_ABOUT_TEXT = '''
关于

    ffmpeg Tk GUI,  ffmpeg 图形界面 (parse_video) 1
           version 0.0.0.1 test201506082042

    本程序为 ffmpeg 的 合并视频文件功能 提供 图形界面. 













更多帮助信息, 请见
    https://github.com/sceext2/parse_video/wiki/zh_cn-easy-guide

copyright 2015 sceext <sceext@foxmail.com>
'''

# debug
def test():
    # just create and show UI
    w = MainWin()
    w.start()
    # start mainloop
    w.mainloop()
    # test done

# end gui.py


