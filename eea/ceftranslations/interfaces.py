# -*- coding: utf-8 -*-
""" Module where all interfaces, events and exceptions live.
"""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from eea.ceftranslations.controlpanel.interfaces import \
    IEEACEFTranslationsSettings


class IEEACEFTranslationsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

__all__ = [
    IEEACEFTranslationsLayer.__name__,
    IEEACEFTranslationsSettings.__name__,
]
