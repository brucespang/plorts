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

def set_color_palette(colors):
    matplotlib.rcParams.update({
        "axes.color_cycle": colors,
        "patch.facecolor": colors[0],
    })

def set_style():
    dark_gray = ".15"
    light_gray = ".8"

    style_dict = {
        "figure.facecolor": "white",
        "text.color": dark_gray,
        "axes.labelcolor": dark_gray,
        "legend.frameon": False,
        "legend.numpoints": 1,
        "legend.scatterpoints": 1,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.color": dark_gray,
        "ytick.color": dark_gray,
        "axes.axisbelow": True,
        "image.cmap": "Greys",
        "font.family": ["sans-serif"],
        "font.sans-serif": ["Arial", "Liberation Sans",
                            "Bitstream Vera Sans", "sans-serif"],
        "grid.linestyle": "-",
        "lines.solid_capstyle": "round",
        "axes.grid": True,
        "axes.facecolor": "white",
        "axes.edgecolor": light_gray,
        "axes.linewidth": 1,
        "grid.color": light_gray,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "xtick.minor.size": 0,
        "ytick.minor.size": 0,
    }
    matplotlib.rcParams.update(style_dict)

def set_context(scaling=1, font_base=12):
    base_context = {
        "font.size": 12/12*font_base,
        "axes.labelsize": 11/12*font_base,
        "axes.titlesize": 12/12*font_base,
        "xtick.labelsize": 10/12*font_base,
        "ytick.labelsize": 10/12*font_base,
        "legend.fontsize": 16/12*font_base,

        "grid.linewidth": 1,
        "lines.linewidth": 1.75,
        "patch.linewidth": .3,
        "lines.markersize": 7,
        "lines.markeredgewidth": 0,

        "xtick.major.width": 1,
        "ytick.major.width": 1,
        "xtick.minor.width": .5,
        "ytick.minor.width": .5,

        "xtick.major.pad": 7,
        "ytick.major.pad": 7,
    }

    context_dict = {k: v * scaling for k, v in base_context.items()}
    base_context["figure.figsize"] = [8*scaling, 5.5*scaling]

    matplotlib.rcParams.update(context_dict)
