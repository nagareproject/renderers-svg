# Encoding: utf-8

# --
# Copyright (c) 2008-2020 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os

from nagare.renderers import xml
from nagare.renderers.svg import Renderer


def test_namespaces():
    s = Renderer()
    assert s.rect(s.line).tostring() == b'<rect xmlns="http://www.w3.org/2000/svg"><line/></rect>'

    s = Renderer()
    s.namespaces = None
    assert s.rect(s.line).tostring() == b'<rect><line/></rect>'

    s = Renderer()
    s.namespaces = {'svg': s.namespace}
    s.default_namespace = 'svg'
    assert s.rect(s.line).tostring() == b'<svg:rect xmlns:svg="http://www.w3.org/2000/svg"><svg:line/></svg:rect>'

    s = Renderer()
    x = xml.Renderer()
    root = x.content(x.section(s.rect(s.line)), x.section(s.rect(s.line)))
    assert root.tostring() == b'<content><section><rect xmlns="http://www.w3.org/2000/svg"><line/></rect></section><section><rect xmlns="http://www.w3.org/2000/svg"><line/></rect></section></content>'


def test_load():
    s = Renderer()
    root = s.fromfile(os.path.join(os.path.dirname(__file__), 'simple.svg'))
    assert root.xpath('svg') is not None
    assert root.xpath('svg//ellipse') is not None


def test_global():
    s = Renderer()
    with s.svg:
        s << s.ellipse(rx=100)

    assert s.root.tostring() == b'<svg xmlns="http://www.w3.org/2000/svg"><ellipse rx="100"/></svg>'
