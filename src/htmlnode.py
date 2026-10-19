class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)