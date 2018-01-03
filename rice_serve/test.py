# -*- coding:utf-8 -*-
__author__ = 'skill'

import websocket
import time
import sys
from threading import Thread

apiKey = "35be4183-e008-4c67-a338-e266d1884f4b"

secretKey = "B67300E9F703BAD1E36E4FC164FBB558"

ws_url = "wss://real.okex.com:10441/websocket"


def on_message(ws, message):
    print "message:", message


def on_error(ws, error):
    print "error:", error
    on_reconnection()


def on_reconnection(ws):
    run()


def on_close(ws):
    # ws.close()
    print "close!"


def on_open(ws):
    print "enter on_open!"
    def run(*args):
        # for item in range(3):
        # send_data = '''{'event':'addChannel','channel':'ok_sub_spot_usd_btc_depth'}'''
        # send_data = '''{'event':'addChannel','channel':'ok_sub_spot_ltc_btc_ticker'}'''
        send_data = '''{'event':'addChannel','channel':'ok_sub_spot_btc_usdt_ticker'}'''
        print "data:", send_data
        ws.send(send_data)
        print "send success: ", send_data
        time.sleep(1)
        # ws.close()
        print "Thread terminating..."
    Thread(target=run).start()


def run():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
    print "start..."


if __name__ == "__main__":
    run()