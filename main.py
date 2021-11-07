import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from dmxrelayconfigurator.ui.windows.mainwindow import MainWindow


def dark():
    """
    Sets the UI Colorsheme to Dark

    :return: None
    """
    dark_palette = QPalette(QColor(53, 53, 53))
    qApp.setPalette(dark_palette)

def initialiseLogging():
    pass
    #logengine.LOG_FORMAT = config.LOG_FORMAT
    #logengine.LOG_TO_CONSOLE = config.LOG_TO_CONSOLE


if __name__ == "__main__":
    try:
        initialiseLogging()

        app = QApplication(sys.argv)
        window = MainWindow()
        dark()
        app.setStyle('Fusion')

        window.show()
        app.exec_()

    except Exception as ex:
        print(ex)
#endregion