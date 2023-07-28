from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window

class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
       
class MainApp(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    MainApp().run()
