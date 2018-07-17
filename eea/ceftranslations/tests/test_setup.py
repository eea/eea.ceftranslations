# -*- coding: utf-8 -*-
""" Setup tests for this package.
"""
import unittest

from plone import api

from eea.ceftranslations.testing import EEA_CEFTRANSLATIONS_INTEGRATION_TESTING  # noqa


class TestSetup(unittest.TestCase):
    """Test that eea.ceftranslations is properly installed."""

    layer = EEA_CEFTRANSLATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eea.ceftranslations is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'eea.ceftranslations'))

    def test_browserlayer(self):
        """Test that IEEACEFTranslationsLayer is registered."""
        from eea.ceftranslations.interfaces import (
            IEEACEFTranslationsLayer)
        from plone.browserlayer import utils
        self.assertIn(IEEACEFTranslationsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    """Test that eea.ceftranslations is properly uninstalled."""

    layer = EEA_TRANSLATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['eea.ceftranslations'])

    def test_product_uninstalled(self):
        """Test if eea.ceftranslations is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'eea.ceftranslations'))

    def test_browserlayer_removed(self):
        """Test that IEEACEFTranslationsLayer is removed."""
        from eea.ceftranslations.interfaces import \
            IEEACEFTranslationsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEEACEFTranslationsLayer, utils.registered_layers())
