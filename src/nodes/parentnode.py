from src.nodes.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("Missing tag in Parent Node")
        if children is None or len(children) == 0:
            raise ValueError("Children missing in Parent Node")
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        result = ""
        if self.props is None:
            result = f"<{self.tag}>"
        else:
            result = f"<{self.tag} {super().props_to_html()}>"
        for i in self.children:
            result += i.to_html()
        result += f"</{self.tag}>"
        return result
            