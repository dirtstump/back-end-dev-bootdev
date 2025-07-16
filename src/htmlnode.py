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
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode requires value")
        if not self.tag:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires tag")
        if not self.children:
            raise ValueError("ParentNode requires children")

        return f"<{self.tag}>{"".join([i.to_html() for i in self.children])}</{self.tag}>"
