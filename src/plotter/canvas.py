import webbrowser
from pathlib import Path
from typing import Literal
from collections.abc import Sequence
import pandas as pd
import plotly.graph_objects as go
from .layout import Layout


class Canvas(pd.DataFrame):
    """
    Canvas().from_df(df).set_x(columns.timestamp)
    """

    def __init__(self, df: pd.DataFrame  | None = None,file_path=Path.cwd() / "canvas.html"):
        super().__init__()
        if df is not None:
            self.load(df)
        self.file_path = file_path
        self.layout = Layout()
        self.layouts: list[go.Layout] = []
        self.width = 800
        self.height = 600
        self.figs = []
        self.fig = go.Figure().set_subplots(specs=[[{"secondary_y": True}]])
        self.x = None
        self.setSubFig()
        self.updatelayout(self.layout)

    def load(self, df: pd.DataFrame ):
        self.__dict__.update(df.__dict__)

        return self

    def set_xname(self, x: str):
        self.x = x
        return self

    def setSubFig(self, fig=None, specs=[[{"secondary_y": True}]]):
        if fig is not None:
            self.fig = fig
            return self
        elif self.fig is None:

            self.fig = go.Figure().set_subplots(specs=specs)

        return self

    def setFig(self, fig=None):
        if fig is not None:
            self.fig = fig
            return self
        elif self.fig is None:
            self.fig = go.Figure()
        return self

    def updatelayout(self, _layout: dict):
        if self.fig is None:
            raise ValueError(
                "fig is None,please init 'fig' property by 'setFig' or setsubFig"
            )
        if len(_layout) > 0:
            self.layout.update(_layout)
            self.fig.update_layout(self.layout)

        return self

    def updatelayout_datetime(self, tickformat: str = "%y-%m-%d %H:%M:%S"):
        if self.fig is None:
            raise ValueError(
                "fig is None,please init 'fig' property by 'setFig' or setsubFig"
            )
        _layout = {
            "xaxis": {
                "tickformat": tickformat,
            }
        }
        self.updatelayout(_layout)

        return self

    def setaxis_style(
        self,
        axis: Literal["x", "y", "y2"] = "x",
        title=None,
        tickmode: Literal["auto"] | None = None,
        xtick: int | Sequence | None = None,
        ytick=None,
        tickformat: str | None = None,
    ):
        _layoutdict = {}
        if tickformat is not None:
            _layoutdict["tickformat"] = tickformat
        if tickmode == "auto":
            _layoutdict["tickmode"] = "auto"
            _layoutdict["nticks"] = xtick
        if title is not None:
            _layoutdict["title"] = title
        _layout = {}

        if axis == "x":
            _layout["xaxis"] = _layoutdict
        if axis == "y":
            _layout["yaxis"] = _layoutdict
        if axis == "y2":
            _layout["yaxis2"] = _layoutdict
        self.updatelayout(_layout)
        return self

    def lines(
        self, y: str, x: str | None = None, lines=None, name=None, secondary_y=False
    ):
        if x is None:
            x = self.x
        return self.scatter(
            x_name=x,
            y_name=y,
            mode="lines",
            lines=lines,
            secondary_y=secondary_y,
            name=name,
        )

    def linesmarks(
        self, y: str, x: str | None = None, lines=None, name=None, secondary_y=False
    ):
        return self.scatter(
            x_name=x,
            y_name=y,
            name=name,
            lines=lines,
            mode="lines+markers",
            secondary_y=secondary_y,
        )

    def _get_xdata(self, x_name: str):
        x_name = self.x if x_name is None else x_name
        if x_name in self.columns:
            return self[x_name]
        elif x_name == self.index.name:
            return self.index
        else:
            return self.index

    def scatter(
        self,
        y_name: str,
        x_name: str | None = None,
        lines=None,
        secondary_y=False,
        mode="markers",
        name=None,
        size=50,
    ):
        """
             line={
            "width": 3,
            "color": "rgba(255, 30, 186, 1)",
            "dash":  "dot"  # 短线组成的虚线 dash  dashdot,solid
        }
        """
        if self.fig is None:
            raise Exception("fig is None,please init 'fig' property by ")

        x = self._get_xdata(x_name)

        if name is None:
            name = y_name
        if lines is None:
            self.fig.add_scatter(
                x=x,
                y=self[y_name],
                mode=mode,
                name=name,
                secondary_y=secondary_y,
                marker_size=size,
            )
        else:
            self.fig.add_scatter(
                x=x,
                y=self[y_name],
                mode=mode,
                name=name,
                secondary_y=secondary_y,
                line=lines,
                marker_size=size,
            )
        return self

    def scatter3D(self, y: str, z: str, x: str | None = None, mode="markers"):
        if self.fig is None:
            self.fig = go.Figure()
        if x is None:
            x = self.x
        self.fig.add_scatter3d(x=self[x], y=self[y], z=self[z], mode=mode)
        return self

    def surface(self, y: str, z: str, x: str | None = None):
        if self.fig is None:
            self.fig = go.Figure()
        if x is None:
            x = self.x
        self.fig.add_surface(x=self[x], y=self[y], z=self[z])
        return self

    def open_html(self):

        url = str(self.file_path)
        if self.fig:
            self.fig.write_html(file=url)
        url = "file://" + url
        webbrowser.open(url, new=0)



