# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""Version helper for wheel builds."""

import pathlib
import re


def normalize_python_package_version(version: str) -> str:
    """Convert the fork suffix to a PEP 440 local version segment."""
    return re.sub(r"-0xble(?=\.|$)", "+0xble", version, count=1)

# Read version from .version file in project root
_version_file = pathlib.Path(__file__).parent.parent / ".version"
__raw_version__ = _version_file.read_text().strip()
__version__ = normalize_python_package_version(__raw_version__)
