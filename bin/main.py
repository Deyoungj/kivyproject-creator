import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs"))



import platform
from kivy.core.window import Window
from app import NameApp


Window.size  = (320,600)



# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


        


if __name__ == '__main__':
    import libs.uix.builder
    NameApp().run()