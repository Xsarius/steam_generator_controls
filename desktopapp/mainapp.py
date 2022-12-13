import PySimpleGUI as sg
from emergency import emergency
from settings import settingstab
from controls import controlbuttons
from layouts import layout_mainapp

window = sg.Window(title="Steam generator controller", layout=layout_mainapp.layout1, margins=(50,50))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if values["-SAVE-"]:
        controlbuttons.activeSave()

    if values["-HEATER-"] == True:
        controlbuttons.setCombinedHeater()

    elif values["-HEATER-"] == False:
        controlbuttons.unsetCombinedHeater()

    if event in ('Emergency stop'):
        emergency.emergencyStop()

    elif event in ('Settings'):
        settingstab.second_window()

    elif event in ('Select all'):
        controlbuttons.selectAll()

    elif event in ('Unselect all'):
        controlbuttons.unselectAll()

    elif event in ('Stop'):
        controlbuttons.stopGeneration()

    elif event in ('Start'):
        controlbuttons.startGeneration()

window.close()