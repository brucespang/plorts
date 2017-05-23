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
def style_axis(show_xaxis=False):
    plt.gca().xaxis.grid(show_xaxis)
    plt.gca().title.set_position([-0.04, 1.1])
    plt.gca().title.set_fontweight("bold")
    plt.gca().title.set_ha("left")
    plt.gca().xaxis.label.set_fontweight('medium')
    plt.gca().xaxis.label.set_fontstyle('italic')
    plt.gca().yaxis.set_label_coords(-0.04,1.01)
    plt.gca().yaxis.label.set_fontweight('medium')
    plt.gca().yaxis.label.set_fontstyle('italic')
    plt.gca().yaxis.label.set_ha('left')
    plt.gca().yaxis.label.set_rotation(0)
