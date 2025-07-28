import unittest

from regex_nodes import extract_markdown_links, extract_markdown_images


class TestSplitNodes(unittest.TestCase):
    def test_links(self):
        node = extract_markdown_links(
            "outside text [link text](actual link) outside text"
        )
        test = [("link text", "actual link")]
        self.assertEqual(node, test)

    def test_multiple_links(self):
        node = extract_markdown_links(
            "[link one](actual link) outside text [link two](actual link) middle text [link three](actual link)"
        )
        test = [
            ("link one", "actual link"),
            ("link two", "actual link"),
            ("link three", "actual link"),
        ]
        self.assertEqual(node, test)

    def test_links_ignore_images(self):
        node = extract_markdown_links(
            "outside text [link text](actual link) middle text ![alt text](image link) outside text"
        )
        test = [("link text", "actual link")]
        self.assertEqual(node, test)

    def test_links_empty(self):
        node = extract_markdown_links(
            "outside text []() outside text"
        )
        test = [("", "")]
        self.assertEqual(node, test)

    def test_images(self):
        node = extract_markdown_images(
            "outside text ![alt text](actual link) outside text"
        )
        test = [("alt text", "actual link")]
        self.assertEqual(node, test)

    def test_multiple_images(self):
        node = extract_markdown_images(
            "![link one](actual link) outside text ![link two](actual link) middle text ![link three](actual link)"
        )
        test = [
            ("link one", "actual link"),
            ("link two", "actual link"),
            ("link three", "actual link"),
        ]
        self.assertEqual(node, test)

    def test_images_ignore_links(self):
        node = extract_markdown_images(
            "outside text [link text](actual link) middle text ![alt text](image link) outside text"
        )
        test = [("alt text", "image link")]
        self.assertEqual(node, test)
