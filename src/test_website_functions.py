"""tests for website functions"""
import unittest

from website_functions import (
        extract_title,
)

class TestWebsiteFunctions(unittest.TestCase):
    """test for website functions"""
    def test_extract_title(self):
        """test extract_title when there is a title"""
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

    def test_extract_title_none(self):
        """test extract_title when there is no title"""
        markdown = "no title here\nrandom new line\n## double header\n#no space"
        with self.assertRaises(ValueError):
            extract_title(markdown)
