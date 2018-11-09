from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread('ac013.JPG')
#lum_img = img[:, :, 0]
plt.imshow(img)#, cmap="nipy_spectral")
plt.colorbar()


class TestApp(App):
    title = "Kivy Garden Matplolib & imshow()"

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box


if __name__ == "__main__":
    TestApp().run()


# Reference: https://stackoverflow.com/questions/51860032/matplotlib-imshow-and-kivy