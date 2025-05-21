from __future__ import division

import os

import matplotlib as mpl

from . import palettes
from .legend import *
from .plotting import *
from .style import *

dirname = os.path.dirname(os.path.abspath(__file__))
mpl.style.core.USER_LIBRARY_PATHS.append(dirname)
mpl.style.core.reload_library()
