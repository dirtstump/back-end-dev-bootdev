"""Functions for splitting nodes into subnodes"""
from textnode import TextNode, TextType
from regex_nodes import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split TEXT nodes based on a delimiter"""
    new_nodes = []
    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
            continue
        new_text = i.text.split(delimiter)
        if len(new_text) % 2 == 0:
            raise SyntaxError("Mismatched delimiters, invalid Markdown syntax")
        for j, j_text in enumerate(new_text):
            if len(j_text) < 1:
                continue
            if j % 2 == 0:
                new_nodes.append(TextNode(j_text, TextType.TEXT))
                continue
            new_nodes.append(TextNode(j_text, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    """Split nodes for image nodes"""
    new_nodes = []
    # loop through each node (i) passed to function
    for i in old_nodes:
        # if node is not TEXT, append and jump to next
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
            continue
        # find links in node text
        new_links = extract_markdown_images(i.text)
        # if no links, append and jump to next
        if not new_links:
            new_nodes.append(i)
            continue
        # loop through each link (j) in new_links
        for j in new_links:
            # split text at first instance of j
            pre_split, post_split = i.text.split(f"![{j[0]}]({j[1]})", 1)
            # if text before link, append as TEXT, otherwise don't append empty string
            if pre_split:
                new_nodes.append(TextNode(pre_split, TextType.TEXT))
            # append link (image) after pre_ and before post_
            new_nodes.append(TextNode(j[0], TextType.IMAGE, j[1]))
            # set i to be text following j and loop
            i.text = post_split
        # if trailing text, append as TEXT
        if post_split:
            new_nodes.append(TextNode(post_split, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    """Split TEXT nodes into sub nodes if they contain markdown"""
    new_nodes = []
    # loop through each node (i) passed to function
    for i in old_nodes:
        # if node is not TEXT, append and jump to next
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
            continue
        # find links in node text
        new_links = extract_markdown_links(i.text)
        # if no links, append and jump to next
        if not new_links:
            new_nodes.append(i)
            continue
        # loop through each link (j) in new_links
        for j in new_links:
            # split text at first instance of j
            pre_split, post_split = i.text.split(f"[{j[0]}]({j[1]})", 1)
            # if text before link, append as TEXT, otherwise don't append empty string
            if pre_split:
                new_nodes.append(TextNode(pre_split, TextType.TEXT))
            # append link (image) after pre_ and before post_
            new_nodes.append(TextNode(j[0], TextType.LINK, j[1]))
            # set i to be text following j and loop
            i.text = post_split
        # if trailing text, append as TEXT
        if post_split:
            new_nodes.append(TextNode(post_split, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    """Split markdown text into text nodes"""
    nodes = [TextNode(text.replace("\n", " "), TextType.TEXT)]
    delims = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]
    # split for each delimitor
    for i in delims:
        nodes = split_nodes_delimiter(nodes, i[0], i[1])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
