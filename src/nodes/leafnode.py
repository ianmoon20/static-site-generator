from src.nodes.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        try:
            if self.tag is None:
                return self.value
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        except ValueError:
            raise ValueError
    