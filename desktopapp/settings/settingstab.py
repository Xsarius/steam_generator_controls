import PySimpleGUI as sg

def saveOptions():
    print('save options test')

def discardOptionsChanges():
    print('discard changes test')

def second_window():

    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.Save(), sg.Button('Discard'), sg.OK()]]

    window = sg.Window('Second Form', layout)
    while True:
        event, values = window.read()

        if event in ('OK'):
            break

        elif event in ('Save'):
            saveOptions()

        elif event in ('Discard'):
            discardOptionsChanges()

    window.close()