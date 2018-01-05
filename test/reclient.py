# -*- coding:utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient
import threading
import ws4py.messaging
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
        self.riceSys.reconnection()

    def received_message(self, m):
        print type(m), m
        if hasattr(m, "data"):
            print type(m.data)
            self.riceSys.covert_feeds(m.data)
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


class Coin:
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

    def reconnection(self):
        self.__ws.connect()
        self.__ws.run_forever()

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

    def covert_feeds(self, data):
        feed = json.loads(data)[0]
        print "name:", feed["channel"]
        channel = feed["channel"].split("_")
        if channel[-1] == "ticker":
            coin_name = channel[-3:-1]
            print coin_name, ":".join(channel[-3:])
            self.set_feeds(":".join(channel[-3:]), feed["data"])
        elif channel[-1] == "depth":
            coin_name = channel[-3:-1]
            print coin_name
            self.set_feeds(":".join(channel[-3:]), feed["data"])
        elif channel[-1] == "deals":
            coin_name = channel[-3:-1]
            print coin_name
            self.set_feeds(":".join(channel[-3:]), feed["data"])
        elif channel[-1] == "10" or channel[-1] == "20" or channel[-1] == "20":
            coin_name = channel[-4:-2]
            print coin_name
            self.set_feeds(":".join(channel[-4:]), feed["data"])
        #1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 12hour, day, 3day, week
        elif channel[-1] == "1min" or channel[-1] == "3min":
            coin_name = channel[-4:-2]
            print coin_name
            self.set_feeds(":".join(channel[-4:]), feed["data"])

    def set_feeds(self, title, data):
        print "redis", title, data

    def get_feeds(self, title):
        print "title"

    #ltc_btc eth_btc etc_btc bch_btc btc_usdt eth_usdt ltc_usdt etc_usdt
    # bch_usdt etc_eth bt1_btc bt2_btc btg_btc qtum_btc hsr_btc neo_btc
    # gas_btc qtum_usdt hsr_usdt neo_usdt gas_usdt
    def covert_btc_usdt(self, data):
        print "data:", data






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
