from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager

import threading, time


KV = """

MySM:

    Screen:
        name: 'splashscreen'
        BoxLayout:
            Label:
                font_size: "40sp"
                text: "SplashScreen"

    Screen:
        name: 'main'
        Label:
            font_size: "20sp"
            text: root.data

"""


class MySM(ScreenManager):
    data = StringProperty("Waiting")

    def __init__(self, **kwargs):
        super(MySM, self).__init__(**kwargs)
        threading.Thread(target=self.get_data).start()

    def get_data(self):
        time.sleep(5)   # 5 seconds doing whatever
        self.data = "something"
        self.current = "main"



class MyApp(App):

    def build(self):
        return Builder.load_string(KV)


MyApp().run()