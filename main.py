import sys
import time

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow
from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow
from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.HMI.ui_Loading_Window import Ui_window_loading
from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.CONTROLLER.crud_file_controller import CRUDFileController
from PRESENTATION.CONTROLLER.crud_file_event_handler import CRUDFileEventHandler


if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = QMainWindow()

    cross_pinning_window = UI_CrossPinning(main_window)
    cross_pinning_window.get_main_window().show()

    # main_window = QMainWindow()
    # window = Ui_MainWindow(main_window)
    #
    # view = CRUDFileView(window)
    #
    # controller = CRUDFileController(view)
    #
    # file_event_handler = CRUDFileEventHandler(controller)
    #
    # controller.get_crud_file_view().get_main_window_ui().get_main_window().show()


    sys.exit(application.exec_())
