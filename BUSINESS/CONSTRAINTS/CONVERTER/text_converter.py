# -*- coding: utf-8 -*-

"""
text_converter.py: The python file dedicated to any need of conversion related to Texts.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from bs4 import BeautifulSoup

from CONFIGURATIONS.logger import LOGGER


def html_content_to_simple_text(html_content: str):
    """
    Converts a content still written in HTML into a simple text.

    :param html_content: The HTML content to be converted.
    :return: The simple text version of the HTML content provided
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text()
    except Exception as exception:
        # At least one error has occurred, therefore, stop the writing process
        LOGGER.error(
            exception.__class__.__name__ + ": " + str(exception)
            + ". Can't go further with the Conversion Process. "
        )
        raise
