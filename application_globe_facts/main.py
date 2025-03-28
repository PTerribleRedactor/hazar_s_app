from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder

class MainWindow(MDScreen):
    pass

class PlayWindow(MDScreen):
    pass

class QuestionWindow(MDScreen):
    pass

class MapsWindow(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class GlobeInfoApp(MDApp):
    def build(self):
        return Builder.load_file("GlobeInfo.kv")

GlobeInfoApp().run()
