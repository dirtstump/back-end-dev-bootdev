import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Text 1", TextType.LINK, "www.test.com")
        node2 = TextNode("Text 1", TextType.LINK, "www.test.com")
        self.assertEqual(node, node2)
    def test_dif_types(self):
        node = TextNode("Text", TextType.ITALIC)
        node2 = TextNode("Text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_dif_text(self):
        node = TextNode("Text 1", TextType.BOLD)
        node2 = TextNode("Text 2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_dif_url(self):
        node = TextNode("Text 1", TextType.LINK, "www.test.com")
        node2 = TextNode("Text 1", TextType.LINK, "www.test2.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
