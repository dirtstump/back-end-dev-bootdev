def markdown_to_blocks(markdown):
    blocks = markdown.split("/n/n")
    blocks = [b.strip() for b in blocks]
    blocks = list(filter(None, blocks))
    return blocks
