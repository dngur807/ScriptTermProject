# -*- coding: euc-kr -*-
import module

from PyQt5.QtWidgets import QApplication , QDialog 

class MainWindow(QDialog , module.UI_Dialog):
    def __init__(self , parent = None):
        super(MainWindow , self).__init__(parent)

        self.setupUI(self);
        
if __name__ == '__main__':
    import sys;
    app = QApplication(sys.argv);
    form = MainWindow();
    form.show();

    sys.exit(app.exec_());