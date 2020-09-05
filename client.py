import websocket
import _thread as thread
import time
import ssl
import json

image = ''


def on_message(ws, message):
    print(message)


def on_error(ws, message):
    print(message)


def on_close(ws):
    print('### closed ##')


def on_open(ws):
    def run(*args):
        for i in range(0, 1):
            time.sleep(1)
            ws.send(json.dumps({
                'id': 'Hello',
                'image': image,
                'items': [
                    {
                        'name': 'Chocolate',
                        'amount': 4500
                    }
                ]
            }))
        time.sleep(1)
        print('thread terminating')

    thread.start_new_thread(run, ())


if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://localhost:8100/ws/chat/ramada/', on_message=on_message, on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False}, )
