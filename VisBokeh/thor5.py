import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor5.html')

data = pd.read_csv('VisBokeh/thor_wwii.csv')
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'], format='%m/%d/%Y')
dataGrouped = data.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()

dataSource = ColumnDataSource(dataGrouped)
p = figure(x_axis_type='datetime')
p.multi_line(x='MSNDATE', y='TOTAL_TONS', source=dataSource, color='green', legend_label = 'total explosion', line_width=2)
p.multi_line(x='MSNDATE', y='TOTAL_IC', source=dataSource, color='blue', legend_label = 'flammable', line_width=2)
p.multi_line(x='MSNDATE', y='TOTAL_HE', source=dataSource, color='red', legend_label = 'Strong explosion', line_width=2)
p.legend.click_policy = 'hide'


show(p)