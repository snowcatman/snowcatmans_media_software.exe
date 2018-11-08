import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
#   from kivy.uix.screenmanager import ScreenManager, Screen
#   from kivy.properties import ObjectProperty
#   from kivy.lang import Builder

#  ===========================================================================
#  Notes: This is unfinished code. The hole file is unfinished.
#  Notes: The idea is to make a window. set a timer, make changes so the window
#  Notes: is borderless and transparent and well as fades away. end timer close and end curent App window.
#   def startfadeout():
#       #  do something like learn what the function and rgs are for fadeout
#       print("should not see this")
#       pass
#
#    #  Window.size = (500, 300)
#    #  Window.borderless = True
#  ===========================================================================


def nothingness(whatever003):
    print('')
    pass


def closes(whatever001):
    App.get_running_app().stop()
    Window.close()
    pass


def mytimer(whatever002):
    timer = threading.Timer(10.0, nothingness)
    timer.start()
    closes
    pass


class MyApp(App):

    def build(self):
        mytimer(self)
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
