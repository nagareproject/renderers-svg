# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""The SVG renderer
"""

from nagare.renderers.xml import XmlRenderer, TagProp


ANIMATION_ADDITION_ATTRIBUTES = {'additive', 'accumulate'}
ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES = {'attributeType', 'attributeName'}
ANIMATION_EVENT_ATTRIBUTES = {'onbegin', 'onend', 'onload', 'onrepeat'}
ANIMATION_TIMING_ATTRIBUTES = {'begin', 'dur', 'end', 'min', 'max', 'restart', 'repeatCount', 'repeatDur', 'fill'}
ANIMATION_VALUE_ATTRIBUTES = {
    'calcMode', 'values', 'keyTimes', 'keySplines', 'from', 'to', 'by', 'autoReverse',
    'accelerate', 'decelerate'
}
CONDITIONAL_PROCESSING_ATTRIBUTES = {'externalResourcesRequired', 'requiredExtensions', 'requiredFeatures', 'systemLanguage'}
CORE_ATTRIBUTES = {'id', 'xml:base', 'xml:lang', 'xml:space', 'tabindex'}
DOCUMENT_EVENT_ATTRIBUTES = {'onabort', 'onerror', 'onresize', 'onscroll', 'onunload', 'onzoom'}
FILTER_PRIMITIVE_ATTRIBUTES = {'height', 'result', 'width', 'x', 'y'}
GRAPHICAL_EVENT_ATTRIBUTES = {
    'onactivate', 'onclick', 'onfocusin', 'onfocusout', 'onload', 'onmousedown', 'onmousemove', 'onmouseout',
    'onmouseover', 'onmouseup'
}
PRESENTATION_ATTRIBUTES = {
    'alignment-baseline', 'baseline-shift', 'clip', 'clip-path', 'clip-rule', 'color', 'color-interpolation',
    'color-interpolation-filters', 'color-profile', 'color-rendering', 'cursor', 'direction', 'display',
    'dominant-baseline', 'enable-background', 'fill', 'fill-opacity', 'fill-rule', 'filter', 'flood-color',
    'flood-opacity', 'font-family', 'font-size', 'font-size-adjust', 'font-stretch', 'font-style', 'font-variant',
    'font-weight', 'glyph-orientation-horizontal', 'glyph-orientation-vertical', 'image-rendering', 'kerning',
    'letter-spacing', 'lighting-color', 'marker-end', 'marker-mid', 'marker-start', 'mask', 'opacity', 'overflow',
    'pointer-events', 'shape-rendering', 'stop-color', 'stop-opacity', 'stroke', 'stroke-dasharray',
    'stroke-dashoffset', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit', 'stroke-opacity', 'stroke-width',
    'text-anchor', 'text-decoration', 'text-rendering', 'unicode-bidi', 'visibility', 'word-spacing', 'writing-mode'
}
TRANSFER_FUNCTION_ATTRIBUTES = {'type', 'tableValues', 'slope', 'intercept', 'amplitude', 'exponent', 'offset'}
XLINK_ATTRIBUTES = {
    'xlink:href', 'xlink:type', 'xlink:role', 'xlink:arcrole', 'xlink:title', 'xlink:show',
    'xlink:actuate'
}
RUNTIME_SYNCHRONISATION_ATTRIBUTES = {
    'syncBehavior', 'syncBehaviorDefault', 'syncTolerance', 'syncToleranceDefault',
    'syncMaster'
}
GLOBAL_EVENT_ATTRIBUTES = {
    'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 'oncuechange', 'ondblclick',
    'ondrag', 'ondragend', 'ondragenter', 'ondragexit', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop',
    'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'oninput', 'oninvalid', 'onkeydown',
    'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown',
    'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel',
    'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreset', 'onresize', 'onscroll',
    'onseeked', 'onseeking', 'onselect', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate',
    'ontoggle', 'onvolumechange', 'onwaiting'
}
STYLE_ATTRIBUTES = {'class', 'style'}
NAVIGATION_ATTRIBUTES = {
    'nav-next', 'nav-prev', 'nav-up', 'nav-up-right', 'nav-right', 'nav-down-right', 'nav-down', 'nav-down-left',
    'nav-left', 'nav-up-left'
}


class Renderer(XmlRenderer):
    doctype = '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
    content_type = 'image/svg+xml'
    namespace = 'http://www.w3.org/2000/svg'

    def __init__(self, parent=None, *args, **kw):
        super(Renderer, self).__init__(parent, *args, **kw)

        self.namespaces = {None: self.namespace}

    a = TagProp('a', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform'}
    ))
    altGlyph = TagProp('altGlyph', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired'}
    ))
    altGlyphDef = TagProp('altGlyphDef', CORE_ATTRIBUTES)
    altGlyphItem = TagProp('altGlyphItem', CORE_ATTRIBUTES)
    animate = TagProp('animate', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        ANIMATION_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        ANIMATION_VALUE_ATTRIBUTES |
        ANIMATION_ADDITION_ATTRIBUTES |
        {'externalResourcesRequired', 'attributeName', 'attributeType', 'from', 'to', 'dur', 'repeatCount'}
    ))
    animateColor = TagProp('animateColor', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        ANIMATION_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        ANIMATION_VALUE_ATTRIBUTES |
        ANIMATION_ADDITION_ATTRIBUTES |
        {'externalResourcesRequired', 'by', 'from', 'to'}
    ))
    animateMotion = TagProp('animateMotion', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        ANIMATION_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        ANIMATION_VALUE_ATTRIBUTES |
        ANIMATION_ADDITION_ATTRIBUTES |
        {'externalResourcesRequired', 'calcMode', 'path', 'keyPoints', 'rotate', 'origin'}
    ))
    animateTransform = TagProp('animateTransform', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        ANIMATION_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        ANIMATION_VALUE_ATTRIBUTES |
        ANIMATION_ADDITION_ATTRIBUTES |
        {'externalResourcesRequired', 'by', 'from', 'to', 'type'}
    ))
    audio = TagProp('audio', (
        RUNTIME_SYNCHRONISATION_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        {'xlink:href', 'type'}
    ))
    circle = TagProp('circle', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'cx', 'cy', 'r'}
    ))
    clipPath = TagProp('clipPath', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'clipPathUnits'}
    ))
    color_profile = TagProp('color-profile', (
        CORE_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'local', 'name', 'rendering-intent', 'xlink:href'}
    ))
    cursor = TagProp('cursor', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'externalResourcesRequired', 'x', 'y', 'xlink:href'}
    ))
    defs = TagProp('defs', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform'}
    ))
    desc = TagProp('desc', CORE_ATTRIBUTES | {'class', 'style'})
    discard = TagProp('discard', CONDITIONAL_PROCESSING_ATTRIBUTES | CORE_ATTRIBUTES | {'begin', 'href'})
    ellipse = TagProp('ellipse', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'cx', 'cy', 'rx', 'ry'}
    ))
    feBlend = TagProp('feBlend', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'in2', 'mode'}
    ))
    feColorMatrix = TagProp('feColorMatrix', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'type', 'values'}
    ))
    feComponentTransfer = TagProp('feComponentTransfer', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in'}
    ))
    feComposite = TagProp('feComposite', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'in2', 'operator', 'k1', 'k2', 'k3', 'k4'}
    ))
    feConvolveMatrix = TagProp('feConvolveMatrix', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {
            'class', 'style', 'in', 'order', 'kernelMatrix', 'divisor', 'bias',
            'targetX', 'targetY', 'edgeMode', 'kernelUnitLength', 'preserveAlpha'
        }
    ))
    feDiffuseLighting = TagProp('feDiffuseLighting', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'surfaceScale', 'diffuseConstant', 'kernelUnitLength'}
    ))
    feDisplacementMap = TagProp('feDisplacementMap', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'in2', 'scale', 'xChannelSelector', 'yChannelSelector'}
    ))
    feDistantLight = TagProp('feDistantLight', CORE_ATTRIBUTES | {'azimuth', 'elevation'})
    feDropShadow = TagProp('feDropShadow', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'stdDeviation', 'dx', 'dy'}
    ))
    feFlood = TagProp('feFlood', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'flood-color', 'flood-opacity'}
    ))
    feFuncA = TagProp('feFuncA', CORE_ATTRIBUTES | TRANSFER_FUNCTION_ATTRIBUTES)
    feFuncB = TagProp('feFuncB', CORE_ATTRIBUTES | TRANSFER_FUNCTION_ATTRIBUTES)
    feFuncG = TagProp('feFuncG', CORE_ATTRIBUTES | TRANSFER_FUNCTION_ATTRIBUTES)
    feFuncR = TagProp('feFuncR', CORE_ATTRIBUTES | TRANSFER_FUNCTION_ATTRIBUTES)
    feGaussianBlur = TagProp('feGaussianBlur', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'stdDevation'}
    ))
    feImage = TagProp('feImage', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'preserveAspectRatio', 'xlink:href'}
    ))
    feMerge = TagProp('feMerge', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style'}
    ))
    feMergeNode = TagProp('feMergeNode', CORE_ATTRIBUTES | {'in'})
    feMorphology = TagProp('feMorphology', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'operator', 'radius'}
    ))
    feOffset = TagProp('feOffset', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in', 'dx', 'dy'}
    ))
    fePointLight = TagProp('fePointLight', CORE_ATTRIBUTES | {'x', 'y', 'z'})
    feSpecularLighting = TagProp('feSpecularLighting', (
        CORE_ATTRIBUTES,
        PRESENTATION_ATTRIBUTES,
        FILTER_PRIMITIVE_ATTRIBUTES,
        {'class', 'style', 'in', 'surfaceScale', 'specularConstant', 'specularExponent', 'kernelUnitLength'}
    ))
    feSpotLight = TagProp('feSpotLight', (
        CORE_ATTRIBUTES |
        {'x', 'y', 'z', 'pointsAtX', 'pointsAtY', 'pointsAtZ', 'specularExponent', 'limitingConeAngle'}
    ))
    feTile = TagProp('feTile', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'in'}
    ))
    feTurbulence = TagProp('feTurbulence', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        FILTER_PRIMITIVE_ATTRIBUTES |
        {'class', 'style', 'baseFrequency', 'numOctaves', 'seed', 'stitchTiles', 'type'}
    ))
    filter = TagProp('filter', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'x', 'y', 'width', 'height',
            'filterRes', 'filterUnits', 'primitiveUnits', 'xlink:href'
        }
    ))
    font = TagProp('font', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'horiz-origin-x',
            'horiz-origin-y', 'horiz-adv-z', 'vert-origin-x', 'vert-origin-y',
            'vert-adv-z'
        }
    ))
    font_face = TagProp('font-face', (
        CORE_ATTRIBUTES |
        {
            'font-family', 'font-style', 'font-variant', 'font-weight', 'font-stretch',
            'font-size', 'unicode-range', 'units-per-em', 'panose-1', 'stemv', 'stemh',
            'slope', 'cap-height', 'x-height', 'accent-height', 'ascent', 'descent', 'widths',
            'bbox', 'ideographic', 'alphabetic', 'mathematical', 'hanging', 'v-ideographic',
            'v-alphabetic', 'v-mathematical', 'v-hanging', 'underline-position',
            'underline-thickness', 'strikethrough-position', 'strikethrough-thickness',
            'overline-position', 'overline-thickness'
        }
    ))
    font_face_format = TagProp('font-face-format', CORE_ATTRIBUTES | {'string'})
    font_face_name = TagProp('font-face-name', CORE_ATTRIBUTES | {'name'})
    font_face_src = TagProp('font-face-src', CORE_ATTRIBUTES)
    font_face_uri = TagProp('font-face-uri', CORE_ATTRIBUTES | XLINK_ATTRIBUTES | {'xlink:href'})
    foreignObject = TagProp('foreignObject', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'x', 'y', 'width', 'height'}
    ))
    g = TagProp('g', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform'}
    ))
    glyph = TagProp('glyph', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'd', 'horiz-adv-x', 'vert-origin-x', 'vert-origin-y',
            'vert-adv-y', 'unicode', 'glyph-name', 'orientation', 'arabic-form', 'lang'
        }
    ))
    glyphRef = TagProp('glyphRef', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'x', 'y', 'dx', 'dy', 'glyphRef', 'format', 'xlink:href'}
    ))
    hatch = TagProp('hatch', (
        CORE_ATTRIBUTES |
        GLOBAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        STYLE_ATTRIBUTES |
        {'x', 'y', 'pitch', 'rotate', 'hatchUnits', 'hatchContentUnits', 'transform', 'href'}
    ))
    hatchpath = TagProp('hatchpath', (
        CORE_ATTRIBUTES |
        GLOBAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        STYLE_ATTRIBUTES |
        {'d', 'offset'}
    ))
    hkern = TagProp('hkern', CORE_ATTRIBUTES | {'u1', 'g1', 'u2', 'g2', 'k'})
    image = TagProp('image', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'transform', 'x', 'y', 'width',
            'height', 'xlink:href', 'preserveAspectRatio'
        }
    ))
    line = TagProp('line', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'x1', 'x2', 'y1', 'y2'}
    ))
    linearGradient = TagProp('linearGradient', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'gradientUnits',
            'gradientTransform', 'x1', 'y1', 'x2', 'y2', 'spreadMethod', 'xlink:href'
        }
    ))
    marker = TagProp('marker', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'viewBox',
            'preserveAspectRatio', 'transform', 'markerUnits', 'refX', 'refY',
            'markerWidth', 'markerHeight', 'orient'
        }
    ))
    mask = TagProp('mask', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'maskUnits', 'maskContentUnits',
            'x', 'y', 'width', 'height'
        }
    ))
    metadata = TagProp('metadata', CORE_ATTRIBUTES)
    missing_glyph = TagProp('missing-glyph', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'd', 'horiz-adv-x', 'vert-origin-x',
            'vert-origin-y', 'vert-adv-y'
        }
    ))
    mpath = TagProp('mpath', (
        CORE_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'externalResourcesRequired', 'xlink:href'}
    ))
    path = TagProp('path', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'd', 'pathLength'}
    ))
    pattern = TagProp('pattern', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'viewBox', 'patternUnits',
            'patterContentUnits', 'patternTransform', 'x', 'y', 'width', 'height', 'xlink:href',
            'preserveAspectRatio'
        }
    ))
    polygon = TagProp('polygon', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'points'}
    ))
    polyline = TagProp('polyline', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'points'}
    ))
    radialGradient = TagProp('radialGradient', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'gradientUnits',
            'gradientTransform', 'cx', 'cy', 'r', 'fx', 'fy', 'spreadMethod',
            'xlink:href'
        }
    ))
    rect = TagProp('rect', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'x', 'y', 'width', 'height', 'rx', 'ry'}
    ))
    script = TagProp('script', (
        CORE_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'externalResourcesRequired', 'type', 'xlink:href'}
    ))
    solidColor = TagProp('solidColor', (
        CORE_ATTRIBUTES |
        GLOBAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        STYLE_ATTRIBUTES
    ))
    solidcolor = TagProp('solidcolor', (
        CORE_ATTRIBUTES |
        GLOBAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        STYLE_ATTRIBUTES
    ))
    stop = TagProp('stop', (
        CORE_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'offset', 'stop-color', 'stop-opacity'}
    ))
    style = TagProp('style', CORE_ATTRIBUTES | {'type', 'media', 'title'})
    svg = TagProp('svg', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        DOCUMENT_EVENT_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'version', 'baseProfile', 'x', 'y',
            'width', 'height', 'preserveAspectRatio', 'contentScriptType', 'contentStyleType',
            'viewBox'
        }
    ))
    switch = TagProp('switch', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'allowReorder'}
    ))
    symbol = TagProp('symbol', (
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'preserveAspectRatio', 'viewBox'}
    ))
    tbreak = TagProp('tbreak')
    text = TagProp('text', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'transform', 'x', 'y', 'dx',
            'dy', 'text-anchor', 'rotate', 'textLength', 'lengthAdjust'
        }
    ))
    textArea = TagProp('textArea', NAVIGATION_ATTRIBUTES | {'x', 'y', 'width', 'height', 'editable', 'focusable'})
    textPath = TagProp('textPath', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'startOffset', 'method', 'spacing', 'xlink:href'}
    ))
    title = TagProp('title', CORE_ATTRIBUTES | {'class', 'style'})
    tref = TagProp('tref', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'xlink:href'}
    ))
    tspan = TagProp('tspan', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        {
            'class', 'style', 'externalResourcesRequired', 'x', 'y', 'dx', 'dy', 'rotate',
            'textLength', 'lengthAdjust'
        }
    ))
    use = TagProp('use', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        GRAPHICAL_EVENT_ATTRIBUTES |
        PRESENTATION_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        {'class', 'style', 'externalResourcesRequired', 'transform', 'x', 'y', 'width', 'height', 'xlink:href'}
    ))
    video = TagProp('video', (
        NAVIGATION_ATTRIBUTES |
        RUNTIME_SYNCHRONISATION_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        {
            'x', 'y', 'width', 'height', 'xlink:ref', 'preserveAspectRatio', 'type', 'transformBehavior',
            'overlay', 'initialVisibility', 'focusable'
        }
    ))
    view = TagProp('view', (
        CORE_ATTRIBUTES |
        {'externalResourcesRequired', 'viewBox', 'preserveAspectRatio', 'zoomAndPan', 'viewTarget'}
    ))
    vkern = TagProp('vkern', CORE_ATTRIBUTES | {'u1', 'g1', 'u2', 'g2', 'k'})
    set = TagProp('set', (
        CONDITIONAL_PROCESSING_ATTRIBUTES |
        CORE_ATTRIBUTES |
        ANIMATION_EVENT_ATTRIBUTES |
        XLINK_ATTRIBUTES |
        ANIMATION_ATTRIBUTE_TARGET_ATTRIBUTES |
        ANIMATION_TIMING_ATTRIBUTES |
        {'externalResourcesRequired', 'to'}
    ))
