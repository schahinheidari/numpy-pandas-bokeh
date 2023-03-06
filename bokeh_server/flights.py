from histogram import histTab
from table import tableTab
from route import routeTab
from bokeh.io import curdoc
from bokeh.models import Tabs
from os.path import dirname, join
import pandas as pd


data = pd.read_csv("flights.csv", index_col=0).dropna() # null data remove row with dropna()


tabHistogram = histTab(data)
tabTable = tableTab(data)
tabRoute = routeTab(data)
tabs = Tabs(tabs=[tabHistogram, tabTable, tabRoute])
curdoc().add_root(tabs)
