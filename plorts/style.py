# Most of this is lifted from Seaborn (https://stanford.edu/~mwaskom/software/seaborn/)
#
# Copyright (c) 2012-2013, Michael L. Waskom
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the {organization} nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import division
import matplotlib
import matplotlib.pyplot as plt

# Does a bunch of styling stuff that needs to be done manually instead of in the
# rcparams
def style_axis(show_xaxis=False, label_fontweight='medium', label_fontstyle='italic'):
    ax = plt.gca()

    ax.xaxis.grid(show_xaxis)    
    ax.xaxis.label.set_fontweight(label_fontweight)
    ax.xaxis.label.set_fontstyle(label_fontstyle)
    
    # position the y label at the top left, left-aligned with the ticks.
    left_in_axis = [0, 1]
    left_in_display = ax.transAxes.transform(left_in_axis)
    left_label_in_display = [left_in_display[0] - ax.yaxis.get_tick_space() * ax.figure.dpi/72.,
                             left_in_display[1] + ax.xaxis.get_tick_space() * ax.figure.dpi/72.]
    left_label_in_axis = ax.transAxes.inverted().transform(left_label_in_display)

    ax.yaxis.set_label_coords(*left_label_in_axis)
    ax.yaxis.label.set_fontweight(label_fontweight)
    ax.yaxis.label.set_fontstyle(label_fontstyle)
    ax.yaxis.label.set_ha('left')
    ax.yaxis.label.set_va('bottom')
    ax.yaxis.label.set_rotation(0)

    # position the y label at the top left, left-aligned with the ticks.
    title_in_display = [left_in_display[0] - ax.yaxis.get_tick_space() * ax.figure.dpi/72.,
                        left_label_in_display[1] + ax.xaxis.get_tick_space() * ax.figure.dpi/72.]
    title_in_axis = ax.transAxes.inverted().transform(title_in_display)
    ax.title.set_position(title_in_axis)
    ax.title.set_fontweight("bold")
    ax.title.set_ha("left")
    ax.title.set_ha("left")
    
    plt.tight_layout()
