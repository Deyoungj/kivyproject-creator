from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory
import os
from kivy.core.window import Window
from libs.uix.root import Root
from libs.uix.baseclass.home_screen import HomeScreen



Window.size = (320, 600)


def kivy_file(kv_file):
    kivy_path = os.getcwd()+'/libs/uix/kv_files/'
    return os.path.join(str(kivy_path),str(kv_file))




class Live(App, MDApp):

    CLASSES = {
        "Root":"libs.uix.root",
        "HomeScreen":"libs.uix.baseclass.home_screen",
        
    }

    AUTORELOADER_PATHS = [
        (".",{'recursive': True})
    ]


    KV_FILES =[

       kivy_file('home.kv')
        
        
    ]



    def build_app(self, first=False):
        print('test2')
        screen_manager = Factory.Root()
        screen_manager.add_widget(HomeScreen(name='home_screen'))
        return screen_manager




if __name__ == '__main__':

    Live().run()
