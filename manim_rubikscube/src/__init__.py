from .cube import *
from .cube_animations import *

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

try:
    __version__ = importlib_metadata.version(__name__)
except:
    __version__ = "0.1.0"
