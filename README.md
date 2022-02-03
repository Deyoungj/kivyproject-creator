# kivy_project-creator


## Features
* Ready-to-start a new project with just a single command.
* After Creating the project, it provides a file named `hot_reloader.py` that already setuped [`kaki`](https://github.com/tito/kaki/) for hot reload.
* Creates `buildozer.spec` that already filled up.
* Gives better source code management (Folder Structure 👇).
```
project_name (Base Project Files)
|____libs (Code files)
| |____uix (UI files)
| | |____baseclass (PY files)
| | |____kv (KV files)
| | |____components (Custom UIX)
| |____applibs (Custom Modules files)
|____assets (Images and Font files)
```

### Dependencies
- [Python](https://www.python.org/) 3.6+
- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Buildozer](https://github.com/kivy/buildozer)
- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.2.dev0 (from master branch)
- [kaki](https://github.com/tito/kaki) for hotreloader

### Installation
```
git clone https://github.com/Deyoungj/kivyMD_project-creator
cd Kivy_Project_Creator/bin
pip install -r requirements.txt 
```
## Linux

### Setup
Add kivy_Project_Creator/bin to `PATH`
open your Terminal and type `nano ~/.bashrc`
Copy and paste this in the file

```
export KIVY=$HOME/Kivy_Project_Creator
export PATH=$KIVY/bin:$PATH
```

### Commands
To create a `Project`
```
kivy-app create <Directory>
```
To run with `hot_reloader.py`
```
kivy-app run -r
```
To run with `main.py`
```
kivy-app run
```
for more commands type `kivy-app --help` or `kivy-app -help`
