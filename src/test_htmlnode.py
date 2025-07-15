import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_write(self):
        node = HTMLNode(
            tag="tag",
            value="value",
            children="children",
            props={"key1": "link1", "key2": "link2"}
        )
        test = 'tag: tag\nvalue: value\nchildren: children\nprops:  key1="link1" key2="link2"'
        self.assertEqual(str(node), test)
    def test_write_tag(self):
        node = HTMLNode(tag="tag")
        test = 'tag: tag'
        self.assertEqual(str(node), test)
    def test_write_none(self):
        node = HTMLNode()
        test = "None"
        self.assertEqual(str(node), test)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "gref": "test"}).to_html()
        test = '<a href="https://www.google.com" gref="test">Click me!</a>'
        self.assertEqual(node, test)
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p")

if __name__ == "__main__":
    unittest.main()
