from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            raise TypeError("TEXT type only, no nested inline text types")
        new_text = i.text.split(delimiter)
        for j in new_text:
            if len(j) < 1:
                continue
            if j % 2 == 0:
                new_nodes.append(TextNode(j, TextType.TEXT))
            new_nodes.append(TextNode(j, text_type))
    return new_nodes
