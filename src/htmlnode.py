class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        prop_string = " "
        if self.props == None:
            return None
        for prop in self.props:
            prop_string = prop_string + f"{prop}=\"{self.props[prop]}\" "
        return prop_string
    
    def __repr__(self):
        print(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode does not have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{(self.props_to_html(),"")[self.props_to_html() == None]}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode does not have a tag")
        if self.children == None:
            raise ValueError("ParentNode is missing children")
        html = f"<{self.tag}{(self.props_to_html(),"")[self.props_to_html() == None]}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html