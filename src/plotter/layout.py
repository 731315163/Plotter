import webbrowser
from pathlib import Path
from typing import Literal, overload

import pandas as pd
import plotly.express as exp
import plotly.graph_objects as go
import plotly.offline as plt


from .axis import Axis
from .font import Font
from .legend import Legend


class Layout(dict):
    def __init__(self):
        self.__dict__.update(default_layout.__dict__)

    def updateLegend(
        self,
        legend: Legend | None = None,
        legend_title_text: str | None = None,
        show: bool = True,
    ):
        if show:
            self["showlegend"] = True
        if legend is not None:
            self.update({"legend": legend})
        if legend_title_text is not None:
            self["legend_title_text"] = legend_title_text
        return self

    def updateMargin(self, left: float, right: float, top: float, bottom: float):
        self["margin"] = dict(l=left, r=right, t=top, b=bottom)
        return self
    @property
    def font(self):
        return self["font"]
    @font.setter
    def font(self, font: Font):
            self["font"] = font
  
    @property
    def xaxis(self):
        return self["xaxis"]
    @xaxis.setter
    def xaxis(self, x: Axis):
        self["xaxis"] = x
    @property
    def yaxis(self):
        return self["yaxis"]
    @yaxis.setter
    def yaxis(self, y: Axis):
        self["yaxis"] = y
    
    @property
    def yaxis2(self):
        return self["yaxis2"]
    @yaxis2.setter
    def yaxis2(self, y2: Axis):
        self["yaxis2"] = y2

  


default_layout = go.Layout(
    title_font=dict(size=20, color="rgb(37, 58, 79)"),
    xaxis=dict(
        title="X",
       
        tickfont=dict(size=24, color="rgb(37, 58, 79)"),
    ),
    yaxis=dict(
        title="Y",
        tickfont=dict(size=24, color="rgb(37, 58, 79)"),
    ),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.02),
    margin=dict(l=50, r=50, b=100, t=60),
    paper_bgcolor="rgb(243, 243, 243)",
    plot_bgcolor="rgb(243, 243, 243)",
)
