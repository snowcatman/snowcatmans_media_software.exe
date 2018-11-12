#  Email: snowcatman@gmail.com To: Shawn Quintal Subject: Splash Screens
#  URL of resting file: github under the snowcatmans media software
from kivy.app import App
from threading import Timer
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# remember i am new to this too. As you can tell i am useing Kivy 
# for python here. For the moment the module file creates a 
# boarderless window that say's hello world and then closes 
# after about 30 secounds.


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
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()

#  ===============================================================
#  Notes: This is a template. The idea is to create a window. Make 
#  it borderless and transparent as well as fades away. Set a
#  timer to close current window. I have yet to empliment fading
#  or transparency. But I figure I could do this later. As I am 
#  attempting to learn about how to create code that works in 
#  multible operating system envirnments. Thank You.
#  ===============================================================
