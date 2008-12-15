*********************************
The :mod:`repoze.what` XML plugin
*********************************

.. module:: repoze.what.plugins.xml
    :synopsis: XML adapters plugin for repoze.what
.. moduleauthor:: Gustavo Narea <me@gustavonarea.net>

:Author: Gustavo Narea.
:Latest version: |release|

.. topic:: Overview

    The :mod:`repoze.what` XML plugin adds support to XML source adapters on
    this authorization framework.


How to install
==============

This package has no external dependencies and can be installed by running::
    
    easy_install repoze.what.plugins.xml

It has been tested under Python v2.5 and v2.6. It's not expected to work on
previous versions.


Adapters
========

.. module:: repoze.what.plugins.xml.adapters
    :synopsis: XML source adapters for repoze.what
.. moduleauthor:: Gustavo Narea <me@gustavonarea.net>

The XML plugin provides one group adapter and one permission adapter, which
receive one parameter: The XML file.

.. autoclass:: XMLGroupsAdapter

.. autoclass:: XMLPermissionsAdapter

They are both imported into the :mod:`repoze.what.plugins.xml` namespace, so
you can do::

    from repoze.what.plugins.xml import XMLGroupsAdapter, XMLPermissionsAdapter


Contents
========

.. toctree::
    :maxdepth: 2

    News

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

