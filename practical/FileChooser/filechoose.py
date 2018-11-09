"""Simple widget to display a matplolib figure in kivy"""
from kivy.uix.widget import Widget
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backend_bases import NavigationToolbar2
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.base import EventLoop
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import math

class GUI(BoxLayout):

    file_path = StringProperty("Currently No File")


    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        self.load_file_popup = load_file_popup(load=self.load)

    def load(self, selection):
        self.file_path = str(selection[0])
        self.load_file_popup.dismiss()


class load_file_popup(Popup):

    load = ObjectProperty()

