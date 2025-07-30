import unittest

from markdown_to_html import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        test = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        self.assertEqual(blocks, test)

    def test_block_to_block_type_heading(self):
        """test headings"""
        blocks = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "#### Heading 4",
            "##### Heading 5",
            "###### Heading 6",
            "# Heading\non\nmultiple\nlines",
            "#No space heading",
            "####### Too much heading 7",
        ]
        results = [block_to_block_type(i) for i in blocks]
        test = [
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
        ]
        self.assertListEqual(results, test)

    def test_block_to_block_type_code(self):
        """test code"""
        blocks = [
            "``` Code with spaces ```",
            "```Code no spaces```",
            "```Code\nmultiple\nlines```",
            "``Two tick code``",
            "````Four tick code````",
        ]
        results = [block_to_block_type(i) for i in blocks]
        test = [
            BlockType.CODE,
            BlockType.CODE,
            BlockType.CODE,
            BlockType.PARAGRAPH,
            BlockType.CODE,
        ]
        self.assertListEqual(results, test)

    def test_block_to_block_type_quote(self):
        """test quote"""
        blocks = [
            ">normal quote",
            ">multi line\n>quote",
            "not a quote",
            ">missing\nquote character"
        ]
        results = [block_to_block_type(i) for i in blocks]
        test = [
            BlockType.QUOTE,
            BlockType.QUOTE,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
        ]
        self.assertListEqual(results, test)

    def test_block_to_block_type_unordered_list(self):
        """test unordered list"""
        blocks = [
            "- one item list",
            "- multi\n- item\n- list",
            "-no\n-space\n-list",
            "- one\n- line\nmissing",
            "- leading\n - space",
        ]
        results = [block_to_block_type(i) for i in blocks]
        test = [
            BlockType.UNORDERED_LIST,
            BlockType.UNORDERED_LIST,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
        ]
        self.assertListEqual(results, test)

    def test_block_to_block_type_ordered_list(self):
        """test ordered list"""
        blocks = [
            "1. one item list",
            "1. multi\n2. item\n3. list",
            "1.no\n2.space\n3.list",
            "1. one\n2. line\nmissing",
            "1. leading\n 2. space",
            "1. list\n3. order\n2. out of",
        ]
        results = [block_to_block_type(i) for i in blocks]
        test = [
            BlockType.ORDERED_LIST,
            BlockType.ORDERED_LIST,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
        ]
        self.assertListEqual(results, test)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
