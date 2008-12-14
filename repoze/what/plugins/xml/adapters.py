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

"""The repoze.what groups and permission adapters for XML sources"""

from repoze.what.adapters import BaseSourceAdapter, SourceError

__all__ = ['XMLGroupsAdapter', 'XMLPermissionsAdapter']


class _BaseXMLAdapter(BaseSourceAdapter):
    
    def __init__(self, file, **kwargs):
        self.file = file
        self.is_writable = True
        super(_BaseXMLAdapter, self).__init__(**kwargs)


class XMLGroupsAdapter(_BaseXMLAdapter):
    pass


class XMLPermissionsAdapter(_BaseXMLAdapter):
    pass
