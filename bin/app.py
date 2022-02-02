from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from libs.uix.root import Root

""""""""""""""""""""""import screen"""""""""""""""
from libs.uix.baseclass.home_screen import HomeScreen

""""""""""""""""""""""""""""""""""""""""""""""""""




class NameApp(MDApp):
    
    def build(self):
        screen_manager = Root()
        screen_manager.add_widget(HomeScreen(name='home_scrn'))
        return screen_manager