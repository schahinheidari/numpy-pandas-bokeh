import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, TabPanel
from bokeh.models.widgets import TableColumn, DataTable

def tableTab(data):
    d = data.groupby('name')['arr_delay'].describe()
    d['mean'] = d['mean'].round(1)
    d['std'] = d['std'].round(1)
    d = d.reset_index()
    #d = d.reset_index().rename(columns={'name': 'name of airline', 'count': 'Number of flights','std': 'standard deviation', 'min': 'minimum of delay', 'mean': 'average of delay', 'max': 'maximum of delay'})

    c = ColumnDataSource(d)
    #https://docs.bokeh.org/en/latest/docs/reference/models/widgets.tables.html#bokeh.models.widgets.tables.DataTable
    flightsTable = DataTable(
        source = c,
        columns=[
            TableColumn(field='name', title='Airline'),
            TableColumn(field='count', title='Number of flights'),
            TableColumn(field='mean', title='Average of delay'),
            TableColumn(field='std', title='Standard deviation of delay'),
            TableColumn(field='min', title='Minimum of delay'),
            TableColumn(field='25%', title='25%'),
            TableColumn(field='50%', title='50%'),
            TableColumn(field='75%', title='75%'),
            TableColumn(field='max', title='Maximum of delay')
        ],
        width=1500, autosize_mode='force_fit', background='#a240a2'
    )
    tab = TabPanel(child=flightsTable, title='Summary of delays')
    return tab

    