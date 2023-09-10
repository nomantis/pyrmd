"""
Helper functions for dynamic versioning of the package.
"""

# mypy: ignore-errors
from setuptools.build_meta import *

def __getattr__(name: str) -> str:
    """Get attribute from object, with default."""
    if name == 'VERSION':
        return '0.0.1'
    raise AttributeError(f"Version helper doesn't provide the {name} attribute")
