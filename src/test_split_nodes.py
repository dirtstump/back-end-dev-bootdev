import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def split_only_text(self):
        node = split_nodes_delimiter(
            [TextNode("Text 1", TextType.TEXT)],
            "**", TextType.BOLD
        )
        test = TextNode("Text 1", TextType.TEXT)
        self.assertEqual(node, test)
