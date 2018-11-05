# kvboxlayout.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

########################################################################
class KVMyHBoxLayout(BoxLayout):
    pass

########################################################################
class KVBoxLayoutApp(App):
    """"""

    #----------------------------------------------------------------------
    def build(self):
        """"""
        return KVMyHBoxLayout()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = KVBoxLayoutApp()
    app.run()
    