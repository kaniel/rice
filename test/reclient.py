# -*- coding:utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient
import threading
import time
import json

wss_url = "wss://real.okex.com:10441/websocket"
send_url = '''{'event':'addChannel','channel':'ok_sub_spot_btc_usdt_ticker'}'''
send_url1 = '''{'event':'addChannel','channel':'ok_sub_spot_btc_usdt_depth'}'''
send_url2 = '''{'event':'addChannel','channel':'ok_sub_spot_btc_usdt_kline_1min'}'''


class EchoClient(WebSocketClient):
    riceSys = None
    def opened(self):
        self.send(send_url)

        self.send(send_url2)
        # self.send('''{"event":"ping"}''')

    def closed(self, code, reason=None):
        print "Closed down", code, reason
        self.connect()
        print "reconnect..."
        self.run_forever()

    def received_message(self, m):
        print type(m), m
        if hasattr(m, "data"):
            print m.data
        # self.close()
        # receive_data = json.loads(m)
        if hasattr(m, "event"):
            print m.event
            if m["event"] != "pong":
                self.riceSys.__ws.close()
                self.riceSys.__ws.connect()
                # self.__ws.connect()
                print "reconnect..."
                self.riceSys.__ws.run_forever()



class Coin():
    def __init__(self):
        print "init Coin"
        self.__ws = EchoClient(wss_url)
        self.__ws.riceSys = self

    def run(self):
        t = threading.Thread(None, self.test_show)
        # t2 = threading.Thread(None, self.chect_connection)
        t.start()
        # t2.start()
        try:
            self.__ws.connect()
            print "connect..."
            # t2 = threading.Thread(None, self.chect_connection)
            # t2.start()
            self.__ws.run_forever()
            print "end...."
        except KeyboardInterrupt:
            self.__ws.close()

    def test_show(self):
        szTest = ""
        while szTest != "/exit":
            szTest = raw_input("")
            if "/p" in szTest:
                print self.__ws
                print self.__ws.riceSys
                print "pppppppppppp"
    # def chect_connection(self):
    #     time.sleep(10)
    #     while True:
    #         time.sleep(10)
    #         try:
    #             self.__ws.send('''{"event":"ping"}''')
    #         except KeyboardInterrupt:
    #             self.__ws.connect()
    #             self.__ws.run_forever()





def run_tornado():
    from tornado import ioloop
    from ws4py.client.tornadoclient import TornadoWebSocketClient
    class MyClient(TornadoWebSocketClient):
        def opened(self):
            self.send("hello")

        def closed(self, code, reason=None):
            print "Closed down", code, reason
            ioloop.IOLoop.instance().stop()

        def received_message(self, m):
            print m
            # self.close()

    ws = MyClient(wss_url)
    ws.connect()

    ioloop.IOLoop.instance().start()


def run_gevent():
    from gevent import monkey; monkey.patch_all()
    import gevent
    from ws4py.client.geventclient import WebSocketClient

    ws = WebSocketClient(wss_url)
    ws.connect()
    ws.send("hello")

    def incoming():
        while True:
            m = ws.receive()
            if m is not None:
                print m
            else:
                break
        ws.close()

    gevent.joinall([gevent.spawn(incoming)])


coin = Coin()
coin.run()
# run_tornado()
