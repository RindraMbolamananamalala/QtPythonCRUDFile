# -*- coding: utf-8 -*-

"""
shorts_view_.py: The python file dedicated to the Shorts "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead
from PRESENTATION.HMI.ui_Shorts import UI_Shorts
from PRESENTATION.VIEW.crud_file_view import CRUDFileView


def deduce_label_left_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Left Part of the Window's content.
    """
    try:
        line_from_pins = line_to_display.get_from_pins()
        line_from_pins_comment = line_to_display.get_from_pins_comment()
        line_to_pins = line_to_display.get_to_pins()
        line_to_pins_comment = line_to_display.get_to_pins_comment()
        content_to_return = "<html>" \
                                "<body>" \
                                    "<p>" \
                                        + line_from_pins + \
                                        "<BR>" \
                                            + "<span style=\" font-size: 18px;\">" \
                                                + "[" + line_from_pins_comment + "]" \
                                            + "</span>" \
                                        + "</BR>" \
                                        "<BR>" \
                                        "</BR>" \
                                    "</p>" \
                                    "<p>" \
                                        "<span>" \
                                            + line_to_pins\
                                        + "</span>" \
                                        + "<BR>" \
                                            + "<span style=\" font-size: 18px;\">" \
                                                + "[" + line_to_pins_comment+ "]" \
                                            + "</span>" \
                                        + "</BR>" \
                                    "</p>" \
                                "</body>" \
                            "</html>"
        return content_to_return
    except:
        return ""


class ShortsView(CRUDFileView):

    def set_window_ui(self, window_ui: UI_Shorts):
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_Shorts.

        :param window_ui: The UI_OpenWires to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> UI_Shorts:
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_Shorts.

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    def __init__(self, *args):
        # Calling the constructor of the Superclass in order to obtain the needed default behaviors
        super(ShortsView, self).__init__(*args)

        if len(args) == 1:
            # All the configurations have been managed during the call of the Superclass' Constructor
            pass

    def update_content(self, line_to_display: LineToRead) -> None:
        """
        Updating the current content of the Extra Wires - Shorts Window from a given Line of information.

        :param line_to_display: The line the information of which are to be displayed on the Open Wires Window
        :return:  None
        """
        try:
            # Left Part for the Pins
            self.get_window_ui().get_label_left_part().setText(deduce_label_left_part_content(line_to_display))
            # However, we need to store the original main information on the Pins in order to use them later (for the
            # WRITE).
            # We're gonna exploit the Left Label's Tooltip for that.
            pins_info = line_to_display.get_from_pins() + "[" + line_to_display.get_from_pins_comment() + "]" \
                        + "->" \
                        + line_to_display.get_to_pins() + "[" + line_to_display.get_to_pins_comment() + "]"
            self.get_window_ui().get_label_left_part().setToolTip(pins_info)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Update Process related to the Open Wires Window. "
            )
            raise


