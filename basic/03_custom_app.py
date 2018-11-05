# -*- coding: utf-8 -*-

## https://kivy.org/doc/stable/guide/basic.html#quickstart
from kivy.app import App
import kivy
kivy.require('1.10.1')
## This class is used as a Base for our Root Widget (LoginScreen) defined later
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        # class LoginScreen, we override the method __init__() so
        # as to add widgets and to define their behavior:
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()
    #print(MyApp().username)