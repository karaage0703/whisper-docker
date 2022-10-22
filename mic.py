#!/usr/bin/env python
import PySimpleGUI as sg
import socket
import subprocess
import os

PORT = 7860
BUFFER_SIZE = 1024

process = None

def main():
    sg.theme('LightGreen3')

    # define the window layout
    layout = [[sg.Text('Voice to Text', size=(40, 1), justification='center', font='Helvetica 20')],
            [sg.Text('ろくおんていし', key='status')],
            [sg.Button('Record start', size=(10, 1), font='Helvetica 14'),
            sg.Button('Convert', size=(10, 1), font='Helvetica 14'),
            sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]]

    # create the window and show it without the plot
    window = sg.Window('Voice to Text',
                       layout, location=(800, 400))

    while True:
        event, values = window.read(timeout=20)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Record start':
            cmd = 'exec arecord -D plughw:1,0 -r 16000 -f S16_LE ./input.wav'
            process = subprocess.Popen(cmd, shell=True)
            window['status'].Update('ろくおんちゅう')

        elif event == 'Convert':
            window['status'].Update('ろくおんていし')
            if process == None:
                print('none')
            else:
                process.kill()
                process == None
                print('kill process')

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', PORT))
                data = 'JP'
                s.send(data.encode())
                print(s.recv(BUFFER_SIZE).decode())

main()
