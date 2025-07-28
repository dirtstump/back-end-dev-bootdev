import unittest

from textnode import TextNode, TextType
from split_nodes import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
