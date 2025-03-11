import pytest
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
from src.plotter import Canvas


@pytest.fixture
def data():
    return {
        "timestamp": pd.date_range("2023-01-01", periods=5),
        "value": [1, 2, 3, 4, 5],
    }


@pytest.fixture
def df(data):
    return pd.DataFrame(data)


@pytest.fixture
def canvas(df):
    return Canvas(df)


def test_init_with_df(canvas: Canvas, df: pd.DataFrame):
    assert canvas.columns.tolist() == df.columns.tolist()


def test_init_without_df():
    canvas = Canvas()
    assert canvas.empty


def test_load(canvas, df):
    canvas.load(df)
    assert canvas.columns.tolist() == df.columns.tolist()


def test_set_xname(canvas):
    canvas.set_xname("timestamp")
    assert canvas.x == "timestamp"


def test_setSubFig(canvas):
    fig = go.Figure()
    canvas.setSubFig(fig)
    assert canvas.fig == fig


def test_setFig(canvas):
    fig = go.Figure()
    canvas.setFig(fig)
    assert canvas.fig == fig


def test_updatelayout(canvas):
    layout = {"title": "Test Layout"}
    canvas.updatelayout(layout)
    assert canvas.fig.layout.title.text == "Test Layout"


def test_updatelayout_datetime(canvas):
    canvas.updatelayout_datetime("%Y-%m-%d")
    assert canvas.fig.layout.xaxis.tickformat == "%Y-%m-%d"


def test_setaxis_style(canvas):
    canvas.setaxis_style("x", title="X Axis")
    assert canvas.fig.layout.xaxis.title.text == "X Axis"


def test_lines(canvas):
    canvas.set_xname("timestamp").lines("value")
    assert len(canvas.fig.data) == 1
    canvas.open_html()


def test_linesmarks(canvas):
    canvas.set_xname("timestamp").linesmarks("value")
    assert len(canvas.fig.data) == 1


def test_scatter(canvas):
    canvas.set_xname("timestamp").scatter("value")
    assert len(canvas.fig.data) == 1


def test_scatter3D(canvas):
    canvas.scatter3D("value", "value", "timestamp")
    assert len(canvas.fig.data) == 1


def test_surface(canvas):
    canvas.surface("value", "value", "timestamp")
    assert len(canvas.fig.data) == 1





def test_updatelayout_exception(canvas):
    canvas.fig = None
    with pytest.raises(ValueError):
        canvas.updatelayout({"title": "Test Layout"})


def test_updatelayout_datetime_exception(canvas):
    canvas.fig = None
    with pytest.raises(ValueError):
        canvas.updatelayout_datetime("%Y-%m-%d")


def test_scatter_exception(canvas):
    canvas.fig = None
    with pytest.raises(Exception):
        canvas.scatter("value")