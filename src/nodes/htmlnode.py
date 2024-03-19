class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        try:
            for key in self.props.keys():
                result += f"{key}=\"{self.props[key]}\" "
            #Removing last space
            result = result[:-1]
        except AttributeError:
            print("Props was empty")
        return result
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"