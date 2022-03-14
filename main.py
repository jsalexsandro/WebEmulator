import json
from PyQt5.QtWidgets import QApplication
from src.App import WindowApp
import sys

command_line = sys.argv[1:]
use = False
permited_init = True

bundlerJSON = {
    "url":"http://localhost:3000",
    "width":300,
    "height":600
}

for i in command_line:
    i = i.lower()

    if (i == "--init" or i == "-i"):
        open("device.config","wt+",encoding="utf-8").write(
            json.dumps(bundlerJSON,indent=4)
        )
        print("Device Configs created!!")
        permited_init = False
        break

    if (i == "--use-config" or i == "-u"):
        print("Initial Config!")
        use = True
        break
    
if (permited_init == True):
    App = QApplication([])
    win = WindowApp(use)
    win.show()
    App.exec()