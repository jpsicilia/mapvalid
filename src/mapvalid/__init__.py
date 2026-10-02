"""mapvalid: spatial validation and area of applicability for machine-learning maps.

The package is in early development. See the roadmap in README.md.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mapvalid")
except PackageNotFoundError:  # running from a source tree without installing
    __version__ = "0.0.0"

__all__ = ["__version__"]
