"""
Custom function for pdf handling
"""


# ----------------- documentation and dependencies settings ----------------- #
# # ... currently adopted from pandas init: https://github.com/pandas-dev/pandas/blob/master/pandas/__init__.py
# __docformat__ = "restructuredtext"

# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("PyPDF2", "tqdm", "pdfrw", "glob", "reportlab")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies


# ----------------- below here are function imports within pyosam ----------------- #
from .add_margin import add_margin
from .merge import merge
from .online_fetch import get_files, download_file
from .pdf2img import pdf2img 