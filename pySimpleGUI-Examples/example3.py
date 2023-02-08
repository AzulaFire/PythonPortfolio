import PySimpleGUI as sg

def blank_frame():
    return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)

sg.theme('DarkGrey4')

layout_frame1 = [
    [blank_frame(), blank_frame()],
    [sg.Frame("Frame 3", [[blank_frame()]], pad=(5, 3), expand_x=True, expand_y=True, title_location=sg.TITLE_LOCATION_TOP)],
]

layout_frame2 = [[blank_frame()]]

layout = [
    [sg.Frame("Frame 1", layout_frame1, size=(280, 250)),
     sg.Frame("Frame 2", layout_frame2, size=(200, 250), title_location=sg.TITLE_LOCATION_TOP)],]

window = sg.Window("Title", layout, margins=(2, 2), finalize=True)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()