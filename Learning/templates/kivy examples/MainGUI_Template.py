from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#  from kivy.graphics import *
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_string("""
#:import kivy kivy

<Separator@Widget>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
<HSeparator@Separator>:
    size_hint_y: None
    height: dp(2)
<VSeparator@Separator>:
    size_hint_x: None
    width: dp(2)

<MenuItem@Button>:
    size_hint_y: None
    height: 30

<MenuButton@Button>:
    size_hint_x: None
    width: self.texture_size[0] + 20

<MenuBar@BoxLayout>:
    orientation: 'horizontal'
    size_hint_y: None
    height: 30

<FileMenu>:
    MenuItem:
        text: 'Open'
    MenuItem:
        text: 'Save'
    MenuItem:
        text: 'Exit'
        on_press: root.clk_exit()

<AboutMenu>
    MenuItem:
        text: 'About'
        on_press: root.popup_about()

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
            MenuButton:
                id: fileMenuButton
                text: 'File'
            MenuButton:
                id: AboutMenuButton
                text: 'Help'

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 0
            Widget
            HSeparator
            Widget

        BoxLayout:
            id: mainArea
            orientation: 'vertical'
            Label:
                text: 'Main Area'

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 0
            Widget
            HSeparator
            Widget

        RelativeLayout:
            size_hint: 1, None
            size: 0, 0
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: 20

            canvas:
                Color:
                    rgba: 0, 0, 0, 0

                Rectangle:
                    pos: 0, 0
                    size: self.size
            BoxLayout:
                size_hint: None, None
                #size: self.minimum_size
                size: 0, 20
                pos_hint: {'left': 1, 'y': 0}
                spacing: 10

                Label:
                    size_hint: None, None
                    size: 75, 20
                    text_size: self.size
                    text: 'Info Bar:'
                Label:
                    size_hint: None, None
                    size: 200, 20
                    text_size: self.size
                    text: '--------------------------------------------'

            Label:
                pos_hint: {'right': 1}
                size_hint: None, None
                size: 150, 30
                text_size: self.size
                text: 'Example Template'

""")


class StartSplash:
    pass



class FileMenu(DropDown):
    def clk_exit(self):
        App().stop()
        Window.close()

    pass


class AboutMenu(DropDown):
    def popup_about(self):
        content = BoxLayout(orientation="vertical")
        popup = Popup(title="About software", size_hint=(None, None),
                      size=(400, 400), auto_dismiss=False, content=content)
        label = Label(text="Template software information")
        close_btn = Button(text="Close", pos_hint={"center_x": .5, "center_y": .9}, size_hint=(None, None),
                           size=(100, 50), on_press=popup.dismiss)
        content.add_widget(label)
        content.add_widget(close_btn)
        popup.open()


class MainScreen(Screen):
    file_menu = ObjectProperty()
    about_menu = ObjectProperty()

    def on_enter(self):
        self.file_menu = FileMenu()
        file_menu_button = self.ids['fileMenuButton']
        file_menu_button.bind(on_release=self.file_menu.open)
        self.about_menu = AboutMenu()
        about_menu_button = self.ids['AboutMenuButton']
        about_menu_button.bind(on_release=self.about_menu.open)


class InfoBar:
    pass


class ATemplateExample(App):
    screen_manager = ObjectProperty()

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name='main'))
        return self.screen_manager

    def main(self):
        self.screen_manager.current = 'main'


if __name__ == '__main__':
    ATemplateExample().run()
