class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self):
        repr_list = []
        if self.tag:
            repr_list.append(f"tag: {self.tag}")
        if self.value:
            repr_list.append(f"value: {self.value}")
        if self.children:
            repr_list.append(f"children: {self.children}")
        if self.props is not None:
            repr_list.append(f"props: {self.props_to_html()}")
        return "\n".join(repr_list or ["None"])

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("error: LeafNode requires value data")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("error: LeafNode requires value")
        if self.tag is None:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
