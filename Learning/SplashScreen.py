from kivy.app import App
from threading import Timer
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window


class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        Clock.schedule_once(self.start_timer)

    def start_timer(self, dt):
        t = Timer(30, self.stop)
        t.start()             

    def build(self):
        Window.size = (500, 300)
        Window.borderless = True
        return Label(text='version .01')

if __name__ == '__main__':
    MyApp().run()
