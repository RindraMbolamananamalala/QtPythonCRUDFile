import sys
import time

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow
from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow
from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.HMI.ui_Open_Wires import UI_OpenWires
from PRESENTATION.HMI.ui_Shorts import UI_Shorts
from PRESENTATION.HMI.ui_Additional_Information_Window import UI_AdditionalInformationWindow
from PRESENTATION.HMI.ui_Loading_Window import Ui_window_loading
from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.VIEW.open_wires_view import OpenWiresView
from PRESENTATION.VIEW.shorts_view import ShortsView
from PRESENTATION.CONTROLLER.crud_file_controller import CRUDFileController
from PRESENTATION.CONTROLLER.crud_file_event_handler import CRUDFileEventHandler

import threading


if __name__ == '__main__':
    application = QApplication(sys.argv)

    controller = CRUDFileController()

    # main_window = QMainWindow()
    # window = Ui_MainWindow(main_window)
    #
    # view = CRUDFileView(window)
    #
    # controller = CRUDFileController(view)
    #

    #file_event_handler = CRUDFileEventHandler(controller)

    #
    # controller.get_crud_file_view().get_main_window_ui().get_main_window().show()


    sys.exit(application.exec_())
