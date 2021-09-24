from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class _Card(QtWidgets.QWidget):
    pass

class ElementCard(QtWidgets.QWidget):
    def __init__(self,steps=5,*args,**kwargs):
        super(ElementCard,self).__init__(*args, **kwargs)