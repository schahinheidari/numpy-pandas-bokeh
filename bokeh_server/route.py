import pandas as pd
import numpy as np
from bokeh.palettes import Category20_16 # category of colors
from bokeh.models.widgets import CheckboxGroup, CheckboxButtonGroup, Slider, RangeSlider, Select
from bokeh.models import ColumnDataSource, Column, TabPanel
from bokeh.plotting import figure
from bokeh.layouts import column, row
from itertools import chain
from bokeh.models import FuncTickFormatter


def routeTab(data):

    def makeDataSet(origin, dest):
        subset = data[(data['origin'] == origin) & (data['dest'] == dest)]
        airLines = list(set(subset['name']))
        xs = []
        ys = []
        dic = {}

        for i, j in enumerate(airLines):
            airLineFlights = subset[subset['name'] == j] # airline flights data
            xs.append(list(airLineFlights['arr_delay'])) # We list so as not to get into problem
            ys.append([i for _ in range(len(airLineFlights))]) # _ means is None
            dic[i] = j
        
        xs = list(chain(*xs)) #By using chain, all the lists are placed flat together [[1,2,3],[2,5]] -> [1,2,3,2,5]
# "*" is the "splat" operator: It takes an iterable like a list as input, and expands it into actual positional arguments in the function call.
        ys = list(chain(*ys))

        return ColumnDataSource(data={'x': xs, 'y': ys}), dic

    def makePlot(src, origInit, destInit, dic):
        p = figure(background_fill_color='#CAB2D6')
        p.circle('x', 'y', source=src, size=10, fill_color="orange", line_color="green")
        p.yaxis[0].ticker.desired_num_ticks = len(dic)
        p.yaxis.formatter = FuncTickFormatter(
            code="""
            var labels = %s;
            return labels[tick];
            """ % dic
        )
        return p

    def update(attr, old, new):
        origin = os.value
        dest = ds.value
        newSrc, newDic = makeDataSet(origin, dest)
        src.data.update(newSrc.data)
        p.yaxis[0].ticker.desired_num_ticks = len(newDic)
        p.yaxis.formatter = FuncTickFormatter(
            code="""
            var labels = %s;
            return labels[tick];
            """ % newDic
        )
        #FuncTickFormatter was deprecated in Bokeh 3.0.0 and will be removed, use CustomJSTickFormatter instead.

    origins = list(set(data['origin'])) # when use 'set' could show unique departure 
    dests = list(set(data['dest'])) # when use 'set' could show unique destination 
    
    os = Select(title='departures', value='LGA', options=origins)    #origin select
    ds = Select(title='destination', value='MIA', options=dests)    #destination select
    os.on_change('value', update)
    ds.on_change('value', update)

    origInit = os.value
    destInit = ds.value

    src, dic = makeDataSet(origInit, destInit) # source and dictionary

    p = makePlot(src, origInit, destInit, dic) #plot

    w = Column(os, ds) #widget box
    l = row(w, p) #layout
    tab = TabPanel(child=l, title='departure/destination')
    return tab