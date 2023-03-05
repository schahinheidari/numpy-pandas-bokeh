from bokeh.palettes import Category20_16 # category of colors
from bokeh.models.widgets import CheckboxGroup, CheckboxButtonGroup
import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models.widgets import Slider, RangeSlider
from bokeh.layouts import column, row
from bokeh.models import Column
from bokeh.models import TabPanel

def histTab(data):

    def makeDataSet(dataSet, rs=-60, re=120, bin=10): #rs = range Start re= range end
        d = pd.DataFrame(columns=['proportion', 'left', 'right', 'f_proportion', 'f_interval', 'name', 'color'])
        r = re - rs
        for i, r_data in enumerate(dataSet):
            subset = data[data['name'] == r_data]
            arrHist, edge = np.histogram(subset['arr_delay'], bins = int(r / bin), range=(rs, re))
            arr_df = pd.DataFrame({
                'proportion': arrHist / np.sum(arrHist),
                'left': edge[:-1],
                'right': edge[1:]
            })
            arr_df['f_proportion'] = ['%0.5f' % p for p in arr_df['proportion']]
            arr_df['f_interval'] = ['%d to %d minutes' % (left, right) for left, right in zip(arr_df['left'], arr_df['right'])]
            arr_df['name'] = r_data
            arr_df['color'] = Category20_16[i]

            d = d.append(arr_df)
        d = d.sort_values(['name', 'left'])
        d = ColumnDataSource(d)
        return d

    def makePlot(dataSet):
        p = figure( title='delay on flight')
        p.quad(source=dataSet, bottom=0, top='proportion', left='left', right='right', color='color', fill_alpha=0.7, legend_label='name') # fill_alpha = resolution
        return p

    def update(attr, old, new):
        airLinesChecked = [chBox.labels[i] for i in chBox.active]
        ds = makeDataSet(airLinesChecked, rangeSlider.value[0], rangeSlider.value[1], slider.value) # ds = new data source
        src.data.update(ds.data)



    airLines = list(set(data['name'])) # when use 'set' could show unique name 
    airLines.sort()
    colors = list(Category20_16)
    colors.sort()

    chBox = CheckboxGroup(labels=airLines, active=[0, 1])
    chBox.on_change('active', update) # func Update

    slider = Slider(start=1, end=30, step=1, value=5, title='Histogram granularity') # decrease and increase bins in histogram
    slider.on_change('value', update)

    rangeSlider = RangeSlider(start=-60, end=180, value=(-60, 120), step=5, title='Interval delays')
    rangeSlider.on_change('value', update)

    initData = [chBox.labels[i] for i in chBox.active]
    src = makeDataSet(initData)

    p = makePlot(src) # plot or figure

    w = Column(chBox, slider, rangeSlider) # widget
    l = row(w, p) #layout

    tab = TabPanel(child=l, title='Histogram panel') #panel tab
    return tab