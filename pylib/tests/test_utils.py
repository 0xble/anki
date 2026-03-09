# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki import buildinfo
from anki.utils import int_version
from anki.utils import int_version_to_str


def test_int_version_to_str():
    assert int_version_to_str(23) == "2.1.23"
    assert int_version_to_str(230900) == "23.09"
    assert int_version_to_str(230901) == "23.09.1"


def test_int_version_ignores_suffixes(monkeypatch):
    monkeypatch.setattr(buildinfo, "version", "25.09.2-0xble.1.0.0")
    assert int_version() == 250902
