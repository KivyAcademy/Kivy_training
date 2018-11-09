import matplotlib as mpl
from kivy_matplotlib import MatplotFigure
from kivy.base import runTouchApp

# Make plot
fig = mpl.figure.Figure(figsize=(2, 2))
fig.gca().plot([1, 2, 3])

# MatplotFigure (Kivy widget)
fig_kivy = MatplotFigure(fig)

runTouchApp(fig_kivy)