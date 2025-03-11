from .font import Font


class Title(dict):
    def __init__(
        self, text: str, font: Font | None = None, standoff: float | None = None
    ):
        self.text = text
        if standoff is not None:
            self.standoff = standoff
        if font is not None:
            self.font = font

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, text):
        self["text"] = text

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, value: Font):
        self["font"] = value

    @property
    def standoff(self):
        return self["standoff"]

    @standoff.setter
    def standoff(self, value: float):
        self["standoff"] = value


class Axis(dict):

    def __init__(
        self,
        title: Title | None = None,
        showline=True,
        linecolor="#000000",
        showgrid=False,
        gridcolor="#000000",
        zeroline=False,
        zerolinecolor="#000000",
    ):
        if title is not None:
            self.title = title

        self.showline = showline
        self.linecolor = linecolor
        self.showgrid = showgrid
        self.gridcolor = gridcolor
        self.zeroline = zeroline
        self.zerolinecolor = zerolinecolor

    @property
    def showline(self):
        return self["showline"]

    @showline.setter
    def showline(self, v: bool):
        self["showline"] = v

    @property
    def linecolor(self):
        return self["linecolor"]

    @linecolor.setter
    def linecolor(self, val):
        self["linecolor"] = val
        return self

    @property
    def showgrid(self):
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val: bool):
        self["showgrid"] = val
        return self

    @property
    def gridcolor(self):
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    @property
    def zeroline(self):
        return self["zeroline"]

    @zeroline.setter
    def zeroline(self, val):
        self["zeroline"] = val
        return self

    @property
    def zerolinecolor(self):
        return self["zerolinecolor"]

    @zerolinecolor.setter
    def zerolinecolor(self, v):
        self["zerolinecolor"] = v
        return self

    @property
    def title(self):
        return self["title"]

    @title.setter
    def title(self, v: Title):
        self["title"] = v
    @property
    def tickformat(self):
        return self["tickformat"]
    
    @tickformat.setter
    def tickformat(self, v: str):
        self["tickformat"] = v
    def set_title(
        self, text: str, font: Font | None = None, standoff: float | None = None
    ):
        title = Title(text=text, font=font, standoff=standoff)
        self.title = title
        return self


class Xaxis(Axis):
    def __init__(self):
        return self


class Yaxis(Axis):
    def __init__(self):
        return self



