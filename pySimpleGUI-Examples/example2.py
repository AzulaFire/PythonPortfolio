import PySimpleGUI as sg

def hello():
    print('hello')

frame_layout = [[sg.Multiline("", size=(80, 20), autoscroll=True,
    reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]]

layout = [
    [sg.Frame("Output console", frame_layout)],
    [sg.Push(), sg.Button("Say Hello")],
]
window = sg.Window("Title", layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Say Hello":
        hello()

window.close()