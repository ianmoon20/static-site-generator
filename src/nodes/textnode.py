from src.nodes.leafnode import LeafNode
import re

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

def split_nodes_delimiter(old_nodes, delimiter, text_type, default_text_type="text"):
    results = []

    for node in old_nodes:
        if not isinstance(node, TextNode):
            results.append(node)
            continue

        if node.text.count(delimiter) % 2 == 1:
            raise ValueError("Unmatched delimiter detected: ensure every opening delimiter has a corresponding closing delimiter")
        
        texts = node.text.split(delimiter)

        for textIndex in range(len(texts)):
            if len(texts[textIndex]) == 0:
                continue
            
            determined_type = text_type if textIndex % 2 == 1 else default_text_type
            results.append(TextNode(texts[textIndex], determined_type))

    return results

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)