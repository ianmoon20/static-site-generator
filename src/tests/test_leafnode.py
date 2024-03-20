import unittest

from src.nodes.leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_p_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),  "<p>This is a paragraph of text.</p>")
        
    
    def test_a_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),  "<a href=\"https://www.google.com\">Click me!</a>")

    def test_text_to_html(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")
if __name__ == "__main__":
    unittest.main()