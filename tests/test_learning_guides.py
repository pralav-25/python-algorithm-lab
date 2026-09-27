"""Keep the worked examples synchronized with the public algorithms."""

import doctest
from pathlib import Path


def load_tests(loader, tests, pattern):
    """Run each Markdown lesson as a separately named doctest case."""
    guides = Path(__file__).resolve().parents[1] / "docs" / "guides"
    for guide in sorted(guides.glob("*.md")):
        tests.addTests(doctest.DocFileSuite(str(guide), module_relative=False))
    return tests
