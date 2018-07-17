==============
EEA ceftranslations
==============
.. image:: http://ci.eionet.europa.eu/job/eea/job/eea.ceftranslations/job/master/badge/icon
  :target: http://ci.eionet.europa.eu/job/eea/job/eea.ceftranslations/job/master/display/redirect

Introduction
============

EEA CEF Translations is a Plone_ add-on which provides content translations based on an external service provided by the European Commission (CEF-AT).

.. contents::


Installation
============

zc.buildout
-----------
If you are using `zc.buildout`_ and the `plone.recipe.zope2instance`_
recipe to manage your project, you can do this:

* Update your buildout.cfg file:

  * Add ``eea.ceftranslations`` to the list of eggs to install
  * Tell the `plone.recipe.zope2instance`_ recipe to install a ZCML slug

  ::

    [instance]
    ...
    eggs =
      ...
      eea.ceftranslations

    zcml =
      ...
      eea.ceftranslations

* Re-run buildout, e.g. with::

  $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.


Getting started
===============

1. Go to **Site Setup > Add-ons** and install **EEA CEF Translations**
3. Customize settings via Site Setup > EEA CEF Translations Settings


Dependencies
============

`EEA CEF Translations`_ has the following dependencies:
  - zeep (a SOAP library required by the translation service)

Source code
===========

- `EEA on Github <https://github.com/eea/eea.ceftranslations>`_


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA CEF Translations (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details in License.txt

Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: http://www.eea.europa.eu/
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`buildout.wheel`: https://pypi.python.org/pypi/buildout.wheel
.. _Plone: https://plone.org
