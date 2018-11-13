from kivy.app import App
from threading import Timer
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window


class Splash(App):

    def __init__(self, **kwargs):
        super(Splash, self).__init__(**kwargs)
        Clock.schedule_once(self.start_timer)

    def start_timer(self, dt):
        t = Timer(10, self.stop)
        t.start()             

    def build(self):
        Window.size = (500, 300)
        Window.borderless = True
        return Label(text='Welcome to snowcatmans media software')

if __name__ == '__main__':
    Splash().run()
