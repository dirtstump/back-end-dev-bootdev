from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
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
