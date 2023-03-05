from random import random
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

p = figure(x_range=(0, 100), y_range=(0, 100))
res = p.text(x=[], y=[], text=[], text_color=[])
dataSource = res.data_source

button = Button(label= 'registration')
i = 0
def clickOnSubmit():
    global i
    newData = dict()
    newData['x'] = dataSource.data['x'] + [random() * 70 + 15] # we could use any number instead of 15
    newData['y'] = dataSource.data['y'] + [random() * 70 + 15]
    newData['text_color'] = dataSource.data['text_color'] + [RdYlBu3[i%3]]
    newData['text'] = dataSource.data['text'] + [str(random())]
    dataSource.data = newData
    i += 1

button.on_click(clickOnSubmit)

curdoc().add_root(column(button, p))