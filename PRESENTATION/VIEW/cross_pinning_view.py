# -*- coding: utf-8 -*-

"""
cross_pinning_view.py: The python file dedicated to the Cross Pinning "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.VIEW.crud_file_view import CRUDFileView

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read_cross_pinning import LineToReadCrossPinning


def deduce_labels_left_part_content(line_to_display: LineToReadCrossPinning) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Labels at the Left Part of the Window's content.
    """
    try:
        i = 0
        content_to_return = ""
        for from_pin in line_to_display.get_from_pins():
            line_from_pins = from_pin
            line_from_pins_comment = line_to_display.get_from_pins_comment()[i]
            content_to_return = content_to_return \
                                    + "<html>" \
                                            "<body>" \
                                                "<p>" \
                                                    + line_from_pins \
                                                    + "<span style=\" vertical-align:sub;\">"\
                                                        + "[" + line_from_pins_comment + "]" \
                                                    + "</span>" \
                                                "</p>" \
                                            "</body>" \
                                        "</html>"
        return content_to_return
    except:
        return ""

def deduce_labels_middle_part_content(line_to_display: LineToReadCrossPinning) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Labels at the Middle Part of the Window's content.
    """
    try:
        i = 0
        content_to_return = ""
        for to_pin in line_to_display.get_to_pins():
            line_to_pins = to_pin
            line_to_pins_comment = line_to_display.get_to_pins_comment()[i]
            content_to_return = content_to_return \
                                + "<html>" \
                                      "<body>" \
                                          "<p>" \
                                            + line_to_pins \
                                            + "<span style=\" vertical-align:sub;\">" \
                                                + "[" + line_to_pins_comment + "]" \
                                            + "</span>" \
                                          "</p>" \
                                      "</body>" \
                                  "</html>"
        return content_to_return
    except:
        return ""

def deduce_labels_right_part_content(line_to_display: LineToReadCrossPinning) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Labels at the Right Part of the Window's content.
    """
    try:
        i = 0
        content_to_return = ""
        for splice in line_to_display.get_splices_list():
            line_splice = splice
            content_to_return = content_to_return \
                                + "<html>" \
                                      "<body>" \
                                          "<p>" \
                                                + splice + \
                                          "</p>" \
                                      "</body>" \
                                  "</html>"
        return content_to_return
    except:
        return ""


class CrossPinningView(CRUDFileView):

    def set_window_ui(self, window_ui: UI_CrossPinning):
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_CrossPinning.

        :param window_ui: The UI_CrossPinning to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> UI_CrossPinning:
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_CrossPinning.

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    def __init__(self, *args):
        # Calling the constructor of the Superclass in order to obtain the needed default behaviors
        super(CrossPinningView, self).__init__(*args)

        if len(args) == 1:
            # All the configurations have been managed during the call of the Superclass' Constructor
            pass

    def update_content(self, line_to_display: LineToReadCrossPinning) -> None:
        """
        Updating the current content of the Open Wires Window from a given Line of information.

        :param line_to_display: The line the information of which are to be displayed on the Open Wires Window
        :return:  None
        """
        try:
            # Left Part for the possible From Pins
            self.get_window_ui().get_label_left_part().setText(deduce_labels_left_part_content(line_to_display))
            # # However, we need to store the original main information on the Pins in order to use them later (for the
            # # WRITE).
            # # We're gonna exploit the Left Label's Tooltip for that.
            # pins_info = line_to_display.get_from_pins() + "[" + line_to_display.get_from_pins_comment() + "]" \
            #             + "->" \
            #             + line_to_display.get_to_pins() + "[" + line_to_display.get_to_pins_comment() + "]"
            # self.get_window_ui().get_label_left_part().setToolTip(pins_info)

            # Middle Part for possible To Pins
            self.get_window_ui().get_label_middle_part().setText(deduce_labels_middle_part_content(line_to_display))

            # Right part for the Splices
            self.get_window_ui().get_label_right_part().setText(deduce_labels_right_part_content(line_to_display))
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Update Process related to the Cross Pinning Window. "
            )
            raise
