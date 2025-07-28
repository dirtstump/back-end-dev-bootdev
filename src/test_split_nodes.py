import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_split_only_text(self):
        node = split_nodes_delimiter(
            [TextNode("Text 1", TextType.TEXT)],
            "**", TextType.BOLD
        )
        test = [TextNode("Text 1", TextType.TEXT)]
        self.assertEqual(node, test)

    def test_split_bold(self):
        node = split_nodes_delimiter(
            [TextNode("Text 1, **bold text**, Text 2", TextType.TEXT)],
            "**", TextType.BOLD
        )
        test = [
            TextNode("Text 1, ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", Text 2", TextType.TEXT)
        ]
        self.assertEqual(node, test)

    def test_split_bold_start_and_end(self):
        node = split_nodes_delimiter(
            [TextNode("**bold start**, Text 1, **bold end**", TextType.TEXT)],
            "**", TextType.BOLD
        )
        test = [
            TextNode("bold start", TextType.BOLD),
            TextNode(", Text 1, ", TextType.TEXT),
            TextNode("bold end", TextType.BOLD)
        ]
        self.assertEqual(node, test)

    def test_split_italic(self):
        node = split_nodes_delimiter(
            [TextNode("Text 1, _italic text_, Text 2", TextType.TEXT)],
            "_", TextType.ITALIC
        )
        test = [
            TextNode("Text 1, ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(", Text 2", TextType.TEXT)
        ]
        self.assertEqual(node, test)

    def test_split_code(self):
        node = split_nodes_delimiter(
            [TextNode("Text 1, `code text`, Text 2", TextType.TEXT)],
            "`", TextType.CODE
        )
        test = [
            TextNode("Text 1, ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(", Text 2", TextType.TEXT)
        ]
        self.assertEqual(node, test)

    def test_multiple_nodes(self):
        node = split_nodes_delimiter([
            TextNode("Text 1, `code text`, Text 2", TextType.TEXT),
            TextNode("Text 3, `code text`, Text 4", TextType.TEXT),
            TextNode("Text 5, `code text`, Text 6", TextType.TEXT),
            ], "`", TextType.CODE
        )
        test = [
            TextNode("Text 1, ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(", Text 2", TextType.TEXT),
            TextNode("Text 3, ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(", Text 4", TextType.TEXT),
            TextNode("Text 5, ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(", Text 6", TextType.TEXT)
        ]
        self.assertEqual(node, test)

    def test_non_text_node(self):
        node = split_nodes_delimiter([
            TextNode("Text 1, `code text`, Text 2", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("Text 3", TextType.TEXT),
            ], "`", TextType.CODE
        )
        test = [
            TextNode("Text 1, ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(", Text 2", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("Text 3", TextType.TEXT)
        ]
        self.assertEqual(node, test)

    def test_mismatched_delimiters(self):
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([
                TextNode("Text, **bold", TextType.TEXT)
            ], "**", TextType.BOLD)
