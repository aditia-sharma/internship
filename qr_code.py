from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv = Builder.load_file("home.kv")

class qr_codeApp(App):
    def build(self):
        return BoxLayout()


if __name__ == "__main__":
    qr_codeApp().run()