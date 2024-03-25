from src.nodes.textnode import TextNode, split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", "text")
    print(split_nodes_delimiter([node], "`", "code"))
        
main()