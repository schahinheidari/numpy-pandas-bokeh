import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
output_file('thor.html')

data = pd.read_csv('VisBokeh/thor_wwii.csv').sample(500)
dataSource = ColumnDataSource(data)

p = figure()
p.circle(source=dataSource, x='AC_ATTACKING', y='TOTAL_TONS', color='green', size='TONS_IC') 
#size we could use any columns in csv or we could easy write number 
p.title.text = 'Air operations of World War II'
p.xaxis.axis_label = "The number of air forces"
p.yaxis.axis_label = 'Explosion volume'

h = HoverTool()
h.tooltips = [
    ('Date of attack', '@MSNDATE'),
    ('Aircraft name', '@AIRCRAFT_NAME'),
    ('Country flying mission', '@COUNTRY_FLYING_MISSION')
]
p.add_tools(h)

show(p)