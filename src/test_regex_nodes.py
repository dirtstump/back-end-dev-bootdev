import unittest

from regex_nodes import extract_markdown_links, extract_markdown_images


class TestSplitNodes(unittest.TestCase):
    def test_link(self):
        node = extract_markdown_links(
            "outside text [link text](actual link) outside text"
        )
        test = [("link text", "actual link")]
        self.assertEqual(node, test)
