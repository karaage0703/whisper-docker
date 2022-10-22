#!/usr/bin/env python
import whisper
import socket
PORT = 7860
BUFFER_SIZE = 1024

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', PORT))
        s.listen()

        whisper_model = whisper.load_model('base', download_root='./')

        print('Waiting for connection...')

        while True:
            (connection, client) = s.accept()
            try:
                print('Client connected', client)
                data = connection.recv(BUFFER_SIZE)
                print(data.upper().decode())
                connection.send(data.upper())

                if data.upper().decode() == 'AUTO':
                    print('start')
                    result = whisper_model.transcribe('input.wav')
                    print(result['text'])

                if data.upper().decode() == 'JP':
                    print('start')
                    result = whisper_model.transcribe('input.wav', verbose=True, language='ja')
                    print(result['text'])

                if data.upper().decode() == 'JP2EN':
                    print('start')
                    result = whisper_model.transcribe('input.wav', verbose=True, language='ja', task='translate')
                    print(result['text'])

            finally:
                connection.close()
