import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_none_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        test = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node, test)

    def test_parent_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
