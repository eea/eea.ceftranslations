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
        from zeep import Client
        from zeep.wsse.username import UsernameToken
        client = Client(
            'https://webgate.ec.europa.eu/etranslation/si/WSEndpointHandlerService?WSDL',
            wsse=UsernameToken('Marine_EEA_20180706', 'xxxyyyzzz'))
        # todo get the password from ENV

        client.service.translate(
            {'priority': '5',
             'external-reference': '1',
             'caller-information': {'application': 'Marine_EEA_20180706',
                                    'username': 'dumitval'},
             'text-to-translate': 'Hausaufgabe',
             'source-language': 'DE',
             'target-languages': {'target-language': 'EN'},
             'domain': 'SPD',
             'requester-callback':
                 'https://wise-test.eionet.europa.eu/translation_callback',
             'destinations': {
                 'http-destination':
                     'https://wise-test.eionet.europa.eu/translation_callback'}
             })


class TranslationCallback(BrowserView):
    """ Translation class """

    def __call__(self):
        """
        """
        import pdb;pdb.set_trace()
        pass


class TranslationsSettings(BrowserView):
    """ return parts of the registry settings
    """
    def enabled(self):
        """ return True if the translations package is enabled """
        return IEEACEFTranslationsSettings(self.context).enabled
