import sys

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow

if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = QMainWindow()
    window = Ui_MainWindow(main_window)
    window.get_main_window().show()

    sys.exit(application.exec_())
