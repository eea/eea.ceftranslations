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


class TranslationCall(BrowserView):
    """ Call Translation class """

    def __call__(self):
        """
        """
        import ipdb;ipdb.set_trace()
        pass


class TranslationCallback(BrowserView):
    """ Translation class """

    def __call__(self):
        """
        """
        import ipdb;ipdb.set_trace()
        pass


class TranslationsSettings(BrowserView):
    """ return parts of the registry settings
    """
    def enabled(self):
        """ return True if the translations package is enabled """
        return IEEACEFTranslationsSettings(self.context).enabled
