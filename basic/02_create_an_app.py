# -*- coding: utf-8 -*-

## https://kivy.org/doc/stable/guide/basic.html#quickstart
import kivy
# It’s required that the base Class of your App inherits from the App class.
# It’s present in the kivy_installation_dir/kivy/app.py.
kivy.require('1.10.1')
from kivy.app import App
# One important thing to note here is the way packages/classes are laid out.
# The uix module is the section that holds the user interface elements
# like layouts and widgets.
from kivy.uix.label import Label

# This is where we are defining the Base Class of our Kivy App. You should
# only ever need to change the name of your app MyApp in this line.
class MyApp(App):
    def build(self):
        # Here we initialize a Label with text ‘Hello World’ and return its
        # instance. This Label will be the Root Widget of this App.
        return Label(text = "Hello World")

# Now on to the portion that will make our app run
if __name__ == "__main__":
    # Here the class MyApp is initialized and its run() method called.
    # This initializes and starts our Kivy application.
    MyApp().run()

## Run the app

## $ python main.py