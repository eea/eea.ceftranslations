""" CEF translations module
"""
import logging
from zope.interface import Interface
from Products.Five import BrowserView
from eea.ceftranslations.interfaces import IEEACEFTranslationsSettings
try:
    from eea.versions.interfaces import IGetVersions
except ImportError:
    class IGetVersions(Interface):
        """ No versioning """


logger = logging.getLogger('eea.ceftranslations')


class Translations(BrowserView):
    """ Suggestions class """

    def __call__(self):
        """
        """

    def translation(self):
        """ """

    def call_translation(self):
        """ """


class TranslationsSettings(BrowserView):
    """ return parts of the registry settings
    """
    def enabled(self):
        """ return True if the translations package is enabled """
        return IEEACEFTranslationsSettings(self.context).enabled
