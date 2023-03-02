import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor4.html')

data = pd.read_csv('VisBokeh/thor_wwii.csv')
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'], format='%m/%d/%Y')
dataGrouped = data.groupby('MSNDATE')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()
dataSource = ColumnDataSource(dataGrouped)

#x_axis_label: a text label to put on the chart’s x-axis (optional)
p = figure(x_axis_type='datetime')

#the lists x and y containing the data
#legend_label: a string to label the line graph with (optional)
#line_width: define the line width (in pixels, optional)
p.line(x='MSNDATE', y='TOTAL_TONS', source=dataSource, color='green', legend_label = 'total explosion', line_width=2)
p.line(x='MSNDATE', y='TOTAL_IC', source=dataSource, color='blue', legend_label = 'flammable', line_width=2)
p.line(x='MSNDATE', y='TOTAL_HE', source=dataSource, color='red', legend_label = 'Strong explosion', line_width=2)
p.legend.click_policy = 'hide'


show(p)