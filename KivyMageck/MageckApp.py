from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os

class Login(Screen):
    pass
class LoginApp(App):
    #return Login()
    def build(self):
        return Button(text='Hello World')


if __name__ == '__main__':
    LoginApp().run()