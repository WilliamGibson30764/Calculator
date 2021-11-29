import PySimpleGUI as sg
import math

from PySimpleGUI.PySimpleGUI import B
import quad
from quad import code
from quad import quadratic_function
from quad import imaginary

import linear
from linear import linear

import bmath
from bmath import math

sg.theme('DarkAmber')
global ttext
ttext = ""
def cb(text):
    return sg.Button(text, size=(5,1))
layout = [  [sg.Text(ttext, key='-text-')],
            [cb('Quad'),cb('Linear'),cb('?')],
            [cb('1'),cb('2'), cb('3'), cb("+"), cb("/")],
            [cb('4'), cb('5'), cb('6'), cb("-"), cb("*")],
            [cb('7'), cb('8'), cb('9'), cb("="), cb("Clear")]
]
def gb(event):
    global ttext
    global text
    re = 0
    while re == 0:
        if event == "1":
            ttext = ttext+"1"
            text = 1
            re = 1
        if event == "2":
            ttext = ttext + "2"
            text = 2
        if event == "3":
            ttext = ttext+"3"
            text = 3
            re = 1
        if event == "4":
            ttext = ttext + "4"
            text = 4
            re = 1
        if event == "5":
            ttext = ttext + "5"
            text = 5
            re = 1
        if event == "6":
            ttext = ttext + "6"
            text = 6
            re = 1
        if event == "7":
            ttext = ttext+"7"
            text = 7
            re = 1
        if event == "8":
            ttext = ttext + "8"
            text = 8
            re = 1
        if event == "9":
            ttext = ttext + "9"
            text = 9
            re = 1
        if event == "+":
            ttext = ttext+ "+"
            re = 1
        if event == "-":
            ttext = ttext + "-"
            re = 1
        if event == "/":
            ttext = ttext + "/"
            re = 1
        if event == "*":
            ttext = ttext + "*"
            re = 1
        if event =="Clear":
            ttext = ""
        return text



win = sg.Window("Help me", layout)

while True:
    quad = 0
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "Help":
        break
    else:
        if event == "Quad":
            win['-text-'].update("What is A? ")
            event, values = win.read()
            a = gb(event)
            win['-text-'].update("What is B?")
            event, values = win.read()
            b = gb(event)
            win['-text-'].update("What is C?")
            event, values = win.read()
            c = gb(event)
            ttext = code(a,b,c)
        if event == "=":
            ttext = math(ttext)
        if event == "Linear":
            win['-text-'].update("What is A?")
            event, values = win.read()
            a = gb(event)
            win['-text-'].update("What is B?")
            event, values = win.read()
            b = gb(event)
            win['-text-'].update("What is C?")
            event, values = win.read()
            c = gb(event)
            win['-text-'].update("What is X?")
            event, values = win.read()
            x = gb(event)
            ttext = linear(a, b, c, x)
        else:
            gb(event)

        


        
    win['-text-'].update(ttext)
win.close
