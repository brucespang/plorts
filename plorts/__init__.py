from __future__ import division

from . import palettes
from .style import *
from .plotting import *
from .legend import *

import matplotlib as mpl
import os
dirname = os.path.dirname(os.path.abspath(__file__))
mpl.style.core.USER_LIBRARY_PATHS.append(dirname)
mpl.style.core.reload_library()
