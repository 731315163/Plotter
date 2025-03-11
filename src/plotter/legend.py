from typing import Literal

from .font import Font


class Legend(dict):
    def __init__(
        self,
        x: float | None,
        y: float | None,
        font: Font | None = None,
        xanchor: Literal["left", "right"] = "left",
        yanchor: Literal["top", "bottom"] = "top",
    ):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if font is not None:
            self.font = font
        self.xanchor = xanchor
        self.yanchor = yanchor

    @property
    def x(self):
        return self["x"]

    @x.setter
    def x(self, v: float):
        self["x"] = v
        return self

    @property
    def y(self):
        return self["y"]

    @y.setter
    def y(self, val: float):
        self["y"] = val
        return self

    @property
    def xanchor(self):
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, v: Literal["left", "right"]):
        self["xanchor"] = v
        return self

    @property
    def yanchor(self):
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, v: Literal["top", "bottom"]):
        self["yanchor"] = v
        return self

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, v: Font):
        f = self.get("font")
        if f is None:
            self["font"] = v
        else:
            self["font"].update(v)

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, v):
        self["bgcolor"] = v

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, v):
        self["bordercolor"] = v

    @property
    def borderwidth(self):
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, v: float):
        self["borderwidth"] = v
