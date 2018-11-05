#https://github.com/kivy-garden/garden.matplotlib/issues/50
import sys, os

import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivyagg")
from kivy.garden.matplotlib import FigureCanvasKivy, FigureCanvasKivyAgg

from matplotlib import pyplot as plt

import pandas
#import pandas.io.tests
import seaborn

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):

    def build(self):

        box = BoxLayout(orientation="horizontal")

        #df = pandas.read_csv(os.path.join(pandas.io.tests.__path__[0], "data", "iris.csv"))
        df = pandas.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
        print df

        seaborn.set_palette('bright')
        seaborn.set_style('whitegrid')
        seaborn.pairplot(data=df,
                         hue="Name",
                         kind="scatter",
                         diag_kind="hist",
                         x_vars=("SepalLength", "SepalWidth"),
                         y_vars=("PetalLength", "PetalWidth"))

        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        box.add_widget(FigureCanvasKivy(plt.gcf()))
        return box


if __name__ == "__main__":
    TestApp().run()