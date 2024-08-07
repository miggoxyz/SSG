from textnode import TextNode


def main():
    node1 = TextNode("Hello", "text", "https://example.com")
    node2 = TextNode("Hello", "text", "https://example.com")
    print(node1 == node2)
    print(node1)
    print(node2)


main()
