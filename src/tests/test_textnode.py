import unittest

from src.nodes.textnode import *
from src.nodes.leafnode import *

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
        assert node.tag == "b"
        assert node.value == "Hi"
        assert node.props == None
    
    def test_split_nodes_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertEqual(split_nodes_delimiter([node], "`", "code"), 
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ]
        )

        node = TextNode("This is text with two `code block` words `throughout it`", "text")
        self.assertEqual(split_nodes_delimiter([node], "`", "code"), 
            [
                TextNode("This is text with two ", "text"),
                TextNode("code block", "code"),
                TextNode(" words ", "text"),
                TextNode("throughout it", "code")
            ]
        )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])
    
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

if __name__ == "__main__":
    unittest.main()