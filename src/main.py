from textnode import (
    TextType,
    TextNode,
)

def main():
    text_node = TextNode("anchor text", TextType.BOLD, "www.text.com")
    print(text_node)


if __name__ == "__main__":
    main()
