"""functions for converting raw markdown to html"""
import re
from enum import Enum
from htmlnode import ParentNode, LeafNode
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    """types of blocks from md"""
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    """break markdown file into blocks"""
    blocks = markdown.split("\n\n")
    blocks = [b.strip() for b in blocks]
    blocks = list(filter(None, blocks))
    return blocks

def block_to_block_type(block):
    """find md block type"""
    # make sure block has contents
    if not block:
        raise ValueError("error: empty block")
    # check for heading (leading  "#")
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    # check for code (leading "```" and ending "```")
    if re.match(r"(?:^`{3})[\s\S]+(?:`{3}$)", block):
        return BlockType.CODE
    # break block into lines for following tests
    lines = block.split("\n")
    # check if each line starts with ">"
    if all(re.match(r"^>",i) for i in lines):
        return BlockType.QUOTE
    # check if each line starts with "- "
    if all(re.match(r"^- ",i) for i in lines):
        return BlockType.UNORDERED_LIST
    # check if each line starts with "#. " where # increments each line
    if all(re.match(f"{i[0]}. ", i[1]) for i in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    """turns a raw markdown into a series of HTML nodes"""
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = block_type_to_tag(block, block_type)
        children = text_to_children(block, block_type)
        nodes.append(ParentNode(tag, children))
    return ParentNode("div", nodes)

def text_to_children(block, block_type):
    """takes block and block_type and returns children nodes"""
    # special cases for code and lists
    # code: no formatting inside of code block, <code> nested in <pre>
    if block_type == BlockType.CODE:
        return [LeafNode("code", block[3:-3].lstrip())]
    # lists: each line needs <li> and formatting
    if block_type in (BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST):
        list_items = block.split("\n")
        nodes = []
        for i in list_items:
            _, i = i.split(" ", 1)
            nodes.append(ParentNode("li", text_to_children(i, BlockType.PARAGRAPH)))
        return nodes
    # all other block_types:
    if block_type == BlockType.QUOTE:
        block = block.lstrip("> ")
        block = block.replace("> ", "")
    if block_type == BlockType.HEADING:
        block = block.lstrip("#")
        block = block.replace(" ", "", 1)
    textnodes = text_to_textnodes(block)
    children = []
    for i in textnodes:
        children.append(text_node_to_html_node(i))
    return children

def block_type_to_tag(block, block_type):
    """takes a block type (and block for heading number) and returns corresponding tag"""
    match block_type:
        case block_type.PARAGRAPH:
            return "p"
        case block_type.HEADING:
            return f"h{len(block)-len(block.lstrip('#'))}"
        case block_type.CODE:
            return "pre"
        case block_type.QUOTE:
            return "blockquote"
        case block_type.UNORDERED_LIST:
            return "ul"
        case block_type.ORDERED_LIST:
            return "ol"
    raise ValueError(f"invalid block type: {block_type}")
