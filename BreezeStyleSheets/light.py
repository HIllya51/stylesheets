try:
    from PyQt5.QtCore import QFile, QTextStream, QIODevice
except:
    from PyQt6.QtCore import QFile, QTextStream, QIODevice
from . import breeze_resources


def stylesheet():
    file = QFile(":/light/stylesheet.qss")
    file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text)
    stream = QTextStream(file)
    return stream.readAll()
