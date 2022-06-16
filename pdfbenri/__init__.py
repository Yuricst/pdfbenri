"""
pdfbenri

Custom module for PDF handling. Bundling couple of PDF-handling packages: 
- PyPDF2 (https://pythonhosted.org/PyPDF2/)
- pdfrw (https://pypi.org/project/pdfrw/)
- pdf2image (https://github.com/Belval/pdf2image)
"""


# ----------------- documentation and dependencies settings ----------------- #
# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("PyPDF2", "tqdm", "pdfrw", "glob", "reportlab", "shutil", "pdf2image")
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
from .rotate import rotate
from .select_pages import select_pages