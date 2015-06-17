# gui.py, part for parse_video : a fork from parseVideo. 
# gui: o/pvtkgui/gui: parse_video Tk GUI, main window gui. 
# version 0.1.6.0 test201506171837
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

import tkinter as TK
import tkinter.ttk as ttk
import tkinter.font as TKfont
import tkinter.tix as tix

from . import gui_style as guis
from ..gui import tk_base

# global vars

# functions

# class

# main window
class MainWin(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        self.root = None	# root window
        
        self.p_top = None	# top part
        self.p_body = None	# body part
        self.p_footer = None	# footer part
        
        self.tk_f = []	# TK frames, used as part parent
        
        self.p_m = None	# MenuHost part
    
    # operations
    # TODO
    
    # event to send, event list
    #	start_stop	top part, start_stop button
    #	top_paste	top part, paste URL
    #
    #	xunlei_dl_path_change	footer part, change xunlei dl path button
    #
    #	top_paste
    #	top_copy
    #
    #	body_copy_selected
    #	body_copy_all_url
    #
    #	xunlei_dl_all_url
    #	xunlei_dl_rest_url
    
    def _send(self, event, data):
        # DEBUG info
        print('pvtkgui: gui: MainWin send event [' + str(event) + '] ' + str(data))
        # use super to send
        super()._send(event, data)
    
    # on sub el
    
    def _on_hide_menu(self, event=None):
        # just hide menu
        self.p_m.hide()
    
    def _on_part_top(self, event, data):
        if event == 'start_stop':
            # just send it
            self._send('start_stop', data)
        elif event == 'show_menu':
            # show top menu
            self.p_m.show('top', data)
        elif event == 'paste':
            self._send('top_paste', data)
        # process sub event done
    
    def _on_part_body(self, event, data):
        if event == 'show_main_menu':
            # show body part menu
            self.p_m.show('body', data)
        # process sub event done
    
    def _on_part_footer(self, event, data):
        if event == 'change':
            self._send('xunlei_dl_path_change', data)
        # process sub event done
    
    def _on_part_menu(self, event, data):
        if event == 'paste_url':
            self._send('top_paste', data)
        elif event == 'copy_url':
            self._send('top_copy', data)
        
        elif event == 'copy_selected':
            self._send('body_copy_selected', data)
        elif event == 'copy_all_url':
            self._send('body_copy_all_url', data)
        
        elif event == 'xunlei_dl_all_url':
            self._send('xunlei_dl_all_url', data)
        elif event == 'xunlei_dl_rest_url':
            self._send('xunlei_dl_rest_url', data)
        # process sub event done
    
    # operations
    
    # start main loop
    def mainloop(self):
        # just start main loop
        mainloop()
    
    # create main UI
    def start(self):
        # create UI
        self._create()
        self._set_el()
    
    def _create(self):
        # create root window
        root = tix.Tk()
        self.root = root
        
        # create sub part
        top = PartTop()
        self.p_top = top
        body = PartBody()
        self.p_body = body
        footer = PartFooter()
        self.p_footer = footer
        
        # create main font
        main_font, main_font_bold, main_big_font_bold = guis.create_main_font(root)
        # set main style
        guis.set_ttk_style()
        
        # set sub styles
        top.hd_font = main_font
        top.hd_entry_font = main_big_font_bold
        top.entry_font = main_font_bold
        
        body.text_font = main_font
        
        footer.label_font = main_font
        footer.entry_font = main_font
        
        # create frames, and pack each part
        f = Frame(root)
        self.tk_f.append(f)
        top.start(f)
        f.pack(side=TOP, fill=X, expand=False)
        
        f = Frame(root)
        self.tk_f.append(f)
        footer.start(f)
        f.pack(side=BOTTOM, fill=X, expand=False)
        
        f = Frame(root)
        self.tk_f.append(f)
        body.start(f)
        f.pack(side=TOP, fill=BOTH, expand=True, padx=(0, 0))
        
        # create MenuHost
        m = MenuHost()
        self.p_m = m
        m.start(root)
        
        # set main window title
        root.title(guis.ui_text['main_win_title'])
        
        # create UI done
    
    def _set_el(self):
        root = self.root
        top = self.p_top
        body = self.p_body
        footer = self.p_footer
        m = self.p_m
        # add callback for sub part
        top.callback = self._on_part_top
        body.callback = self._on_part_body
        footer.callback = self._on_part_footer
        m.callback = self._on_part_menu
        
        # add callback for hide menu
        root.bind('<Button-1>', self._on_hide_menu)
        # set el done
    
    # end MainWin class

# menu host, show menus
class MenuHost(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        self.m1 = None	# top menu
        self.m2 = None	# body menu
    
    def start(self, parent):
        # save parent
        self.parent = parent
        # create menu
        self._create()
        # create UI done
    
    # event to send, event list
    #	paste_url	top entry paste url
    #	copy_url	top entry copy url
    #
    #	copy_selected	body text, copy selected text
    #	copy_all_url
    #	xunlei_dl_all_url
    #	xunlei_dl_rest_url
    
    # on sub el
    
    def _on_paste_url(self, event=None):
        # just send event
        self._send('paste_url', event)
    
    def _on_copy_url(self, event=None):
        self._send('copy_url', event)
    
    def _on_copy_selected(self, event=None):
        self._send('copy_selected', event)
    
    def _on_copy_all_url(self, event=None):
        self._send('copy_all_url', event)
    
    def _on_xunlei_dl_all_url(self, event=None):
        self._send('xunlei_dl_all_url', event)
    
    def _on_xunlei_dl_rest_url(self, event=None):
        self._send('xunlei_dl_rest_url', event)
    
    # hide all menus
    def hide(self):
        self.m1.unpost()
        self.m2.unpost()
    
    # show one menu
    # supported menu type list
    #	entry	top part entry menu
    #	main	body part, text menu
    def show(self, menu_type, event):
        # hide menu first
        self.hide()
        # check which menu
        if menu_type == 'top':
            # show top menu
            m = self.m1
        elif menu_type == 'body':
            # show body menu
            m = self.m2
        else:
            raise Exception('menu type error')
        # show menu
        m.post(event.x_root, event.y_root)
        # show menu done
    
    def _create(self):
        m1 = Menu(self.parent, tearoff=0)
        m2 = Menu(self.parent, tearoff=0)
        self.m1 = m1
        self.m2 = m2
        
        m1t = guis.ui_top_menu	# menu 1 text
        m2t = guis.ui_body_menu
        
        # add command
        m1.add_command(label=m1t['paste_url'], command=self._on_paste_url)
        m1.add_command(label=m1t['copy_url'], command=self._on_copy_url)
        
        m2.add_command(label=m2t['copy_selected'], command=self._on_copy_selected)
        m2.add_command(label=m2t['copy_all_url'], command=self._on_copy_all_url)
        m2.add_separator()
        m2.add_command(label=m2t['xunlei_dl_all_url'], command=self._on_xunlei_dl_all_url)
        m2.add_command(label=m2t['xunlei_dl_rest_url'], command=self._on_xunlei_dl_rest_url)
        
        # create menu done
    
    # end MenuHost class

# top part
class PartTop(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        # NOTE font and style should be set
        self.hd_font = None
        self.hd_entry_font = None
        self.hd_style = guis.top_conf['hd_style']
        self.hd_entry_style = guis.top_conf['hd_entry_style']
        self.button_style = guis.top_conf['button_style']
        
        self.entry_font = None
        self.entry_style = guis.top_conf['entry_style']
        
        self.p_hd = None	# hd part
        self.p_e = None		# main URL entry
        self.p_b = None		# main button
        
        self.tk_f = []	# tkinter frames
    
    # operations
    def get_hd_text(self):
        return self.p_hd.get_text()
    
    def set_hd_text(self, text=''):
        self.p_hd.set_text(text=text)
    
    def get_url_text(self):
        return self.p_e.get_text()
    
    def set_url_text(self, text=''):
        self.p_e.set_text(text=text)
    
    def set_url_text_style(self, style='TEntry'):
        self.p_e.set_entry_style(style=style)
    
    def set_button_text(self, text=''):
        self.p_b.config(text=text)
    
    def set_button_style(self, style='TButton'):
        self.p_b.config(style=style)
    
    # to send event list
    #	start_stop	start or stop analyse
    #	show_menu	show top part URL entry menu
    #	paste		should paste text in URL entry
    
    # on sub el
    def _on_button(self, event=None):
        self._send('start_stop', event)
    
    def _on_hd_entry(self, event, data):
        if event == 'key_enter':
            self._send('start_stop', data)
        # process sub el done
    
    def _on_url_entry(self, event, data):
        if event == 'key_enter':
            self._send('start_stop', data)
        elif event == 'mouse_right':
            self._send('show_menu', data)
        elif event == 'mouse_middle':
            self._send('paste', data)
        # process sub el done
    
    def start(self, parent):
        # save parent
        self.parent = parent
        # create UI
        self._create()
        self._set_el()
    
    def _create(self):
        hd = tk_base.EntryBox()
        self.p_hd = hd
        e = tk_base.EntryBox()
        self.p_e = e
        b = Button(self.parent, command=self._on_button, text=guis.ui_text['start_analyse'], style=self.button_style)
        self.p_b = b
        # set EntryBox
        hd.label_text = guis.ui_text['hd']
        hd.entry_width = guis.HD_ENTRY_WIDTH
        hd.label_font = self.hd_font
        hd.entry_font = self.hd_entry_font
        hd.label_style = self.hd_style
        hd.entry_style = self.hd_entry_style
        
        e.entry_font = self.entry_font
        e.entry_style = self.entry_style
        
        # pack it
        b.pack(side=RIGHT, fill=Y, expand=False)
        
        # create frames
        f = Frame(self.parent)
        self.tk_f.append(f)
        hd.start(f)
        f.pack(side=LEFT, fill=Y, expand=False)
        
        e.start(self.parent)
        
        # create UI done
    
    def _set_el(self):
        hd = self.p_hd
        e = self.p_e
        
        hd.callback = self._on_hd_entry
        e.callback = self._on_url_entry
    
    # end PartTop class

# body part
class PartBody(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        # NOTE font and style should be set
        self.text_color = guis.main_text_conf['color']
        self.text_background_color = guis.main_text_conf['background_color']
        self.text_size = guis.main_text_size
        self.text_cursor_color = guis.main_text_conf['cursor_color']
        
        self.text_font = None
        
        self.text = None	# tk_base.TextBox
    
    # to send event list
    #	show_main_menu
    
    # operations
    
    def enable(self):
        self.text.enable()
    
    def disable(self):
        self.text.disable()
    
    def get_text(self, flag='selected'):
        return self.text.get_text(flag=flag)
    
    def add_text(self, text='', flag='end', style_type=None):
        # get tag name
        tag_name = guis.MAIN_TEXT_STYLE_TO_TAG_LIST[style_type]
        # just add it
        self.text.add_text(text=text, flag=flag, tag=tag_name)
    
    def clear(self):
        self.text.clear()
    
    # on sub el
    
    def _on_text(self, event, data):
        # check event type
        if event == 'mouse_right':
            self._send('show_main_menu', data)
    
    def start(self, parent):
        # save parent
        self.parent = parent
        # create UI
        self._create()
        # set main text tag style
        guis.set_main_text_tag(self.text)
        # done
    
    def _create(self):
        t = tk_base.TextBox()
        self.text = t
        # set t
        t.text_color = self.text_color
        t.text_background_color = self.text_background_color
        t.text_font = self.text_font
        t.text_size = self.text_size
        t.cursor_color = self.text_cursor_color
        
        # start pack
        t.start(self.parent)
        
        # create UI done
    
    def _set_el(self):
        t = self.text
        t.callback = self._on_text
    
    # end PartBody class

# footer part
class PartFooter(tk_base.TkBaseObj):
    
    def __init__(self):
        super().__init__()
        
        # NOTE font and style should be set
        self.label_font = None
        self.entry_font = None
        self.label_style = 'TLabel'
        self.entry_style = 'TEntry'
        self.button_style = 'TButton'
        
        self.entry = None	# tk_base.EntryBox
        self.button = None	# change Button
    
    # operations
    def get_text(self):
        return self.entry.get_text()
    
    def set_text(self, text=''):
        self.entry.set_text(text)
    
    # to send event list
    #	change		main button click
    
    # on sub el
    def _on_button(self, event=None):
        self._send('change', event)
    
    def start(self, parent):
        # save parent
        self.parent = parent
        # create UI
        self._create()
        # done
    
    def _create(self):
        # create UI
        e = tk_base.EntryBox()
        b = Button(self.parent, command=self._on_button, text=guis.ui_text['change'], style=self.button_style)
        self.entry = e
        self.button = b
        # set EntryBox
        e.label_text = guis.ui_text['xunlei_dl_dir']
        e.label_font = self.label_font
        e.entry_font = self.entry_font
        e.label_style = self.label_style
        e.entry_style = self.entry_style
        
        # pack button
        b.pack(side=RIGHT, fill=Y, expand=False)
        # pack entry
        e.start(self.parent)
        
        # create UI done
    
    def _set_el(self):
        pass	# nothing to do
    
    # end PartFooter class

# end gui.py


