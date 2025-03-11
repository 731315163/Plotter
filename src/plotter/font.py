class Font(dict):
    def __init__(self, family=None, size=None, color=None):
        if family is not None:
            self.family = family
        if size is not None:
            self.size = size
        if color is not None:
            self.color = color

    @property
    def family(self):
        return self["family"]

    @family.setter
    def family(self, v):
        self["family"] = v
        return self

    @property
    def size(self):
        return self["size"]

    @size.setter
    def size(self, v):
        self["size"] = v

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val
