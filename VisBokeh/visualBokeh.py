from bokeh.plotting import figure, output_file, show
output_file('bokeh.html')

x1 = [5, 6, 9, 10, 100, 130, 141]
x2 = [8, 10, 18, 15, 30, 100, 101]

p = figure()
p.line(x1, x2, color='blue', legend_label='line')
p.circle(x1, x2, color='green', legend_label='circle')
p.legend.click_policy = 'hide'

show(p)



