"""Make the src-layout package importable when humanize is not installed.

The project is normally installed (e.g. via tox) before running pytest, which
also generates ``src/humanize/_version.py`` through hatch-vcs. In environments
without network access an editable install is not possible, so fall back to
putting ``src`` on ``sys.path`` directly.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
