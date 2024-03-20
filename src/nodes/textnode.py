from src.nodes.leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other) -> bool:
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    viable_text_types = {
        "text": lambda: LeafNode(None, text_node.text),
        "bold": lambda: LeafNode("b", text_node.text),
        "italic": lambda: LeafNode("i", text_node.text),
        "code": lambda: LeafNode("code", text_node.text),
        "link": lambda: LeafNode("a", text_node.text),
        "image": lambda: LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    }

    if text_node.text_type not in viable_text_types:
        raise ValueError(f"Text type ({text_node.text_type}) can not be converted into LeafNode")
    
    return viable_text_types[text_node.text_type]()