# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008, Gustavo Narea <me@gustavonarea.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

"""The test suite for the adapters in the repoze.what XML plugin"""

import unittest, os
from shutil import copy

from repoze.what.adapters.testutil import GroupsAdapterTester, \
                                          PermissionsAdapterTester

from repoze.what.plugins.xml import XMLGroupsAdapter, XMLPermissionsAdapter

here = os.path.abspath(os.path.dirname(__file__))
fixtures = os.path.join(here, 'fixture')


class BaseXmlAdapterTester(unittest.TestCase):
    
    def _setup_xml_adapter(self):
        tmp_filename = self.filename + '.tmp'
        original = os.path.join(fixtures, self.filename)
        self.tmp_file = os.path.join(fixtures, tmp_filename)
        copy(original, self.tmp_file)
        # Setting up the XML adapter:
        self.adapter = self.adapter_class(self.tmp_file)
    
    def tearDown(self):
        os.remove(self.tmp_file)


class TestXMLGroupsAdapter(GroupsAdapterTester, BaseXmlAdapterTester):
    
    filename = 'groups.xml'
    
    adapter_class = XMLGroupsAdapter
    
    def setUp(self):
        super(TestXMLGroupsAdapter, self).setUp()
        self._setup_xml_adapter()
        


class TestXMLPermissionsAdapter(PermissionsAdapterTester,
                                BaseXmlAdapterTester):
    
    filename = 'permissions.xml'
    
    adapter_class = XMLPermissionsAdapter
    
    def setUp(self):
        super(TestXMLPermissionsAdapter, self).setUp()
        self._setup_xml_adapter()
