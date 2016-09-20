import sys
from datetime import datetime, date, time, timedelta
import calendar
from PyQt4 import QtGui

def fecha():
    x = datetime.now()
    if x.month <= 9:
        y = datetime(x.year, 9, 15)
    else:
        y = datetime(x.year + 1, 9, 15)
    b.setText("    "+str(y - x)+"\n"+"para el 15 de septiembre")
    b.move(110,20)

app = QtGui.QApplication(sys.argv)
a = QtGui.QWidget()
b = QtGui.QLabel(a)
heroes = str.format("Hidalgo y Costilla\n"+"       Jose Maria Morelos y Pavon\n"+"      Vicente Guerrero\n"+"       Josefa Ortiz")
b.setText(heroes)
a.setGeometry(150,150,500,200)
b.move(50,25)
a.setWindowTitle("!Viva Mexico!")
a.setWindowIcon(QtGui.QIcon('bandera.jpg'))
btn = QtGui.QPushButton('Aprietame', a)
btn.setToolTip('Ya dame click xD')
btn.clicked.connect(fecha)
btn.resize(btn.sizeHint())
btn.move(200, 100)
a.show()
sys.exit(app.exec_())
