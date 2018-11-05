# kvnestedbox.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

########################################################################
class HBoxWidget(Widget):
    pass

########################################################################
class VBoxWidget(Widget):
    pass

########################################################################
class KVNestedBoxLayoutApp(App):
    """"""

    #----------------------------------------------------------------------
    def build(self):
        """"""
        return VBoxWidget()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = KVNestedBoxLayoutApp()
    app.run()