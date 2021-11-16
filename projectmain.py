import PySimpleGUI as sg
sg.theme('DarkAmber')
text = ""
def cb(text):
    return sg.Button(text, size=(5,1))
layout = [  [sg.Text(text, key='-text-')],
            [cb('1'),cb('2'), cb('3'), cb("+"), cb("/")],
            [cb('4'), cb('5'), cb('6'), cb("-"), cb("*")],
            [cb('7'), cb('8'), cb('9'), cb("Enter")]
]
win = sg.Window("Help me", layout)

while True:

    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "Help":
        break
    if event == "1":
        text = text+"1"
    if event == "2":
        text = text + "2"
    if event == "3":
        text = text+"3"
    if event == "4":
        text = text + "4"
    if event == "5":
        text = text + "5"
    if event == "6":
        text = text + "6"
    if event == "7":
        text = text+"7"
    if event == "8":
        text = text + "8"
    if event == "9":
        text = text + "9"
        
    win['-text-'].update(text)
win.close