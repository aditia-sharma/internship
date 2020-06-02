import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.lang import Builder


kv = Builder.load_file("home.kv")


class MyHomeApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyHomeApp().run()