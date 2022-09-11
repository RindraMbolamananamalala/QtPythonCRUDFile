import sys

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow
from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.CONTROLLER.crud_file_controller import CRUDFileController

if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = QMainWindow()
    window = Ui_MainWindow(main_window)

    view = CRUDFileView(window)

    controller = CRUDFileController(view, None)

    controller.get_crud_file_view().get_main_window_ui().get_main_window().show()

    sys.exit(application.exec_())
