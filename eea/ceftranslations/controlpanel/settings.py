""" Control Panel
"""
from zope.component import queryUtility
from zope.interface import implementer
from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from eea.ceftranslations.interfaces import IEEACEFTranslationsSettings
from eea.ceftranslations.config import EEAMessageFactory as _


class EditForm(controlpanel.RegistryEditForm):
    """ Control panel edit form
    """

    schema = IEEACEFTranslationsSettings
    label = _(u"EEA CEFTranslations Settings")
    description = _(u"EEA CEFTranslations settings")


class ControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Control panel form wrapper
    """

    form = EditForm


@implementer(IEEACEFTranslationsSettings)
class ControlPanelAdapter(object):
    """ Settings adapter
    """

    def __init__(self, context):
        self.context = context
        self._settings = None

    def __getattr__(self, name):
        return getattr(self.settings, name, None)

    @property
    def settings(self):
        """ Settings
        """
        if self._settings is None:
            self._settings = queryUtility(
                IRegistry).forInterface(IEEACEFTranslationsSettings, None)
        return self._settings

    @property
    def enabled(self):
        """ Check if translations suggestions are disabled for current context
        """
        context_type = getattr(self.context, 'portal_type', None)
        enabled_types = self.settings.portalTypes if self.settings else None
        if isinstance(enabled_types, list) and context_type in enabled_types:
            return True
        return False
