import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor3.html')

data = pd.read_csv('VisBokeh/thor_wwii.csv')
fData = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]
dataGrouped = fData.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()

dataSource = ColumnDataSource(dataGrouped)
countries = dataSource.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=countries)

# color map
cm = factor_cmap(field_name='COUNTRY_FLYING_MISSION', palette=Spectral3, factors=countries)

p.vbar_stack(source=dataSource, x='COUNTRY_FLYING_MISSION', width=0.7, color=Spectral3, stackers=['TONS_FRAG', 'TONS_IC', 'TONS_HE'], legend_label=['Parts', 'flammable', 'Strong explosion'])

""" h = HoverTool()ectral3, stackers=['TONS_FRAG', 'TONS_IC', 'TONS_HE'], legend_label=['Parts', 'flammable', 'Strong explosion
h.tooltips = [
    ('sum of explosives', 
     ' Aggregate strong segregation explosives @TONS_HE and Accumulation of incendiary substances @TONS_IC nad Number of pieces exploded @TONS_FRAG')
]
h.mode = 'vline'
p.add_tools(h) """

show(p)