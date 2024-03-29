##########################################################################
#
#  Copyright (c) 2023, Hypothetical Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import functools
import imath

import Gaffer
import GafferUI


def __setColor(node, state):
    color = None
    if state == "Warning":
        Gaffer.Metadata.deregisterValue(node, "nodeGadget:color")
        Gaffer.Metadata.registerValue(node, "nodeGadget:color", imath.Color3f(0.75, 0.63, 0.0))
    elif state == "Error":
        Gaffer.Metadata.deregisterValue(node, "nodeGadget:color")
        Gaffer.Metadata.registerValue(node, "nodeGadget:color", imath.Color3f(0.75, 0.0, 0.0))
    elif state == "Passing":
        Gaffer.Metadata.deregisterValue(node, "nodeGadget:color")
        Gaffer.Metadata.registerValue(node, "nodeGadget:color", imath.Color3f(0.015, 0.75, 0.0))
    elif state == "Neutral":
        Gaffer.Metadata.deregisterValue(node, "nodeGadget:color")


def __appendNodeMenu(graphEditor, node, menuDefinition):
    menuDefinition.append("/IgorDivider", {"divider": True, "label": "Igor : Color"})
    menuDefinition.append("/Neutral", {"command": functools.partial(__setColor, node, "Neutral")})
    menuDefinition.append("/Warning", {"command": functools.partial(__setColor, node, "Warning")})
    menuDefinition.append("/Error", {"command": functools.partial(__setColor, node, "Error")})
    menuDefinition.append("/Passing", {"command": functools.partial(__setColor, node, "Passing")})


GafferUI.GraphEditor.nodeContextMenuSignal().connect(__appendNodeMenu, scoped=False)
