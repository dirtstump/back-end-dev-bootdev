import unittest

from website_functions import (
        extract_title,
)

class TestWebsiteFunctions(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
test text
# Title
## other header
# not title
more text
"""
        title = extract_title(markdown)
        test = "Title"
        self.assertEqual(title, test)
