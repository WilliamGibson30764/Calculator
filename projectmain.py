import PySimpleGUI as sg
import math
import quad
from quad import code
from quad import quadratic_function
from quad import imaginary

sg.theme('DarkAmber')
global ttext
ttext = ""
def cb(text):
    return sg.Button(text, size=(5,1))
layout = [  [sg.Text(ttext, key='-text-')],
            [cb('Quad'),cb('Linear'),cb('Expo')],
            [cb('1'),cb('2'), cb('3'), cb("+"), cb("/")],
            [cb('4'), cb('5'), cb('6'), cb("-"), cb("*")],
            [cb('7'), cb('8'), cb('9'), cb("=")]
]
def gb(event):
    global ttext
    global text
    while len(ttext) < len(ttext) + 1:
        if event == "1":
            ttext = ttext+"1"
            text = 1
        if event == "2":
            ttext = ttext + "2"
            text = 2
        if event == "3":
            ttext = ttext+"3"
            text = 3
        if event == "4":
            ttext = ttext + "4"
            text = 4
        if event == "5":
            ttext = ttext + "5"
            text = 5
        if event == "6":
            ttext = ttext + "6"
            text = 6
        if event == "7":
            ttext = ttext+"7"
            text = 7
        if event == "8":
            ttext = ttext + "8"
            text = 8
        if event == "9":
            ttext = ttext + "9"
            text = 9
        if event == "+":
            ttext = ttext+"+"
        if event == "-":
            ttext = ttext + "-"
        if event == "/":
            ttext = ttext + "/"
        if event == "*":
            ttext = ttext+"*"
        if event == "=":
            ttext = ttext + "="
        return text



win = sg.Window("Help me", layout)

while True:
    quad = 0
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "Help":
        break
    else:
        if event == "Quad":
            ttext = ""
            a = gb(event)
            b = gb(event)
            c = gb(event)
            code(a,b,c)
        else:
            gb(event)


        
    win['-text-'].update(ttext)
win.close
