import PySimpleGUI as sg

menu_def = [['&File', ['&Settings', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1', 'Command &2',
                              '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]

right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

column1 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))]]
column2 = [[sg.Button("Start"), sg.Button("Stop")],
           [sg.Button("Select all")],
           [sg.Button("Unselect all")],
           [sg.Checkbox("Save active", default=False, key="-SAVE-")]]
column4 = [[sg.Text("Temp water")],
           [sg.Button("Water heater power")],
           [sg.Checkbox("Combined", default=True, key="-HEATER-")]]
column5 = [[sg.Text("Temp steam")],
           [sg.Text("Preasure")]]
column6 = [[sg.Button("Steam heater power")],
           [sg.Image(source="desktopapp/mediafiles/1.png", key="schematic")],
           [sg.Stretch() ,sg.Button("Emergency stop", button_color='red')]]

layout1 = [
    [sg.Column(column1), 
     sg.Column(column2),
     sg.Column(column4),
     sg.Column(column5),
     sg.Column(column6)],
]