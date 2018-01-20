# -*- coding: utf-8 -*-
#
from __future__ import print_function

from .__about__ import (
    __author__,
    __email__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __maintainer__,
    __status__,
    )

from . import ciehcl
from . import cielab
from . import cielch
from . import cieluv
from . import illuminants
from . import observers
from . import srgb1
from . import xyy
from . import xyz
# pylint: disable=wildcard-import
from .tools import *

# try:
#     import pipdate
# except ImportError:
#     pass
# else:
#     if pipdate.needs_checking(__name__):
#         print(pipdate.check(__name__, __version__))
