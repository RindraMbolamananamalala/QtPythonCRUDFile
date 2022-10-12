# -*- coding: utf-8 -*-

"""
loading_window_view_.py: The python file dedicated to the Loading "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

from PRESENTATION.HMI.ui_Loading_Window import Ui_window_loading


class LoadingWindowView:

    def set_window_ui(self, window_ui: Ui_window_loading):
        self.window_ui = window_ui

    def get_window_ui(self) -> Ui_window_loading:
        return self.window_ui

    def __init__(self, loading_window: Ui_window_loading):
        self.set_window_ui(loading_window)
