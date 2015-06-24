#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qt_test1.py, 201506241235

# import
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# class

# MainWin, main window
class MainWin(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # attributes
        
        # UI widgets
        self.line_input = None	# QLineEdit
        self.button_submit = None	# QPushButton
        
        # create UI
        self._create()
        # init done
    
    def _create(self):
        
        l = QLabel('Name: ')
        
        li = QLineEdit()
        self.line_input = li
        
        b = QPushButton('&Submit')
        self.button_submit = b
        
        # create layout
        layout1 = QVBoxLayout()
        layout1.addWidget(l)
        layout1.addWidget(li)
        layout1.addWidget(b)
        
        main_layout = QGridLayout()
        main_layout.addLayout(layout1, 0, 1)
        
        # set default layout
        self.setLayout(main_layout)
        # set window title
        self.setWindowTitle('Hello, Qt ! ')
        
        # add event listener
        b.clicked.connect(self._on_submit_button)
        
        # create UI done
    
    def _on_submit_button(self):
        name = self.line_input.text()
        # DEBUG info
        print('DEBUG: got input name \"' + name + '\"')
        
        if name != '':
            QMessageBox.information(self, 'msgbox title test', 'body \n test\n  a')
    
    # end MainWin class

# star test
def test():
    import sys
    
    a = QApplication(sys.argv)
    # DEBUG info
    print('DEBUG: create QApplication with arg ' + str(sys.argv))
    
    w = MainWin()
    print('DEBUG: created MainWin')
    
    w.show()
    print('DEBUG: show main window')
    
    print('DEBUG: starting main loop')
    exit_code = a.exec_()
    print('DEBUG: mainloop ended')
    
    print('DEBUG: will now exit ' + str(exit_code))
    sys.exit(exit_code)
    
    # test done

if __name__ == '__main__':
    test()

# end qt_test1.py


