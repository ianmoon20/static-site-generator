import unittest

from src.nodes.textnode import TextNode, text_node_to_html_node
from src.nodes.leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_no_props_eq(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_prop_eq(self):
        node = TextNode(None, "bold", "Test URL")
        node2 = TextNode(None, "bold", "Test URL")
        self.assertEqual(node, node2)
    
    def test_props_eq(self):
        node = TextNode(None, "bold", {"src": "Test URL"})
        node2 = TextNode(None, "bold", {"src": "Test URL"})
        self.assertEqual(node, node2)

    def test_text_text_node_to_html_node(self):
        node = text_node_to_html_node(TextNode("Hi", "text"))
        assert node.tag is None
        assert node.value == "Hi"
        assert node.props is None

    def test_bold_text_node_to_html_node(self):
        node = text_node_to_html_node(TextNode("Hi", "bold"))
        assert node.tag is "b"
        assert node.value == "Hi"
        assert node.props is None

if __name__ == "__main__":
    unittest.main()