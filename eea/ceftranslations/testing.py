# -*- coding: utf-8 -*-
""" testing module
"""
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
import eea.ceftranslations


class EEACEFTranslationsLayer(PloneSandboxLayer):
    """ EEA CEF Translations Layer """

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """ set up Zope"""
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=eea.ceftranslations)

    def setUpPloneSite(self, portal):
        """ set up Plone site """
        applyProfile(portal, 'eea.ceftranslations:default')

EEA_TRANSLATIONS_FIXTURE = EEACEFTranslationsLayer()

EEA_TRANSLATIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_TRANSLATIONS_FIXTURE,),
    name='EEACEFTranslationsLayer:IntegrationTesting'
)

EEA_TRANSLATIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EEA_TRANSLATIONS_FIXTURE,),
    name='EEACEFTranslationsLayer:FunctionalTesting'
)

EEA_TRANSLATIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EEA_TRANSLATIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EEACEFTranslationsLayer:AcceptanceTesting'
)
