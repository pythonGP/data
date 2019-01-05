import sys
from PyQt4 import QtGui, QtCore
class Hello_World(QtGui.QWidget):    
    def __init__(self, parent = None):
        super(Hello_World, self).__init__()
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Hello_World')
        self.button = QtGui.QPushButton("show 'Hello World'", self)
        self.button.move(20,20)
        self.lineEdit = QtGui.QLineEdit("",self)
        self.lineEdit.move(20,80)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),self.setText)
        
    def setText(self):
        self.lineEdit.setText("Hello World")
        
app = QtGui.QApplication()
widget = Hello_World()
widget.show()
sys.exit(app.exec_())



