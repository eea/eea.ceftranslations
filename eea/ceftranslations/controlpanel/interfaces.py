""" Control Panel Interfaces

   >>> portal = layer['portal']
   >>> sandbox = portal['sandbox']

"""
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import Interface
from zope import schema
from plone.autoform import directives as aform
from eea.ceftranslations.config import EEAMessageFactory as _


class IEEACEFTranslationsSettings(Interface):
    """ Settings

    >>> from eea.ceftranslations.interfaces import IEEACEFTranslationsSettings
    >>> IEEACEFTranslationsSettings(portal).portalTypes
    [u'Document']

    """
    aform.widget('portalTypes', CheckBoxFieldWidget)
    portalTypes = schema.List(
        title=_(u"Enable CEF translations"),
        description=_(u"Translations are enabled for the "
                      u"following content-types"),
        required=False,
        default=[u"Document"],
        value_type=schema.Choice(
            vocabulary=u"plone.app.vocabularies.ReallyUserFriendlyTypes")
    )
