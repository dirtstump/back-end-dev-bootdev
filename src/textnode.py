from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "**bold**"
    ITALIC_TEXT = "_italic_"
    CODE_TEXT = "`code`"
    LINK_TEXT = "[link](url)"
    IMAGE_TEXT = "![image_link](url)"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
