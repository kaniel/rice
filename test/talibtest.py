# -*- coding:utf-8 -*-

print "sss"

import talib
import numpy
import time
import pandas

close = numpy.random.random(3)
print close
output = talib.SMA(close)
print "output:", output

start = time.clock()
mc = talib.SMA(close, timeperiod=2)
end = time.clock()
print "time:", end - start, type(mc[-1]), mc
start = time.clock()
df = pandas.DataFrame(close, columns=["close"])
# print df
# print "-------------------"
# print df.head()
# print "-------------------"
ds = df.rolling(2).mean()
end = time.clock()
print "\ntime:1", end - start, ds


a = numpy.array([1, -1, 1, -1, 1, -1], dtype='float')
rsi = talib.RSI(a, timeperiod=2)
print rsi


import time

st = time.localtime(1350816710)

print time.strftime("%Y-%m-%d %H:%M:%S", st)

st = time.localtime(1516081380000/1000)
print time.strftime("%Y-%m-%d %H:%M:%S", st)

st = time.localtime(1516081440000/1000)
print time.strftime("%Y-%m-%d %H:%M:%S", st)

st = time.localtime(1516081500000/1000)
print time.strftime("%Y-%m-%d %H:%M:%S", st)

import datetime
print datetime.datetime.now()
millis = int(round(time.time()) * 1000)
print millis
st = time.localtime(millis/1000)
print time.strftime("%Y-%m-%d %H:%M:%S", st)

data = '''[["1516081380000","13017.511","13044.9996","13017.511","13044.9996","26.91334702"], \
           ["1516081440000","13044.9996","13044.9997","13044.9996","13044.9997","12.79976362"], \
           ["1516081500000","13044.9996","13044.9997","13025.559","13025.5591","18.54048606"], \
           ["1516081560000","13025.5591","13025.5591","13012.0563","13020.8959","14.15875998"], \
           ["1516081620000","13018.9051","13025.5589","13018.9051","13025.5587","3.9323276"], \
           ["1516081680000","13025.5587","13029.9999","13025.5587","13029.9998","16.72394996"], \
           ["1516081740000","13029.9998","13029.9999","13025.5588","13025.566","13.2417794"], \
           ["1516081800000","13025.5662","13029.8652","13025.5588","13025.5588","33.63893916"], \
           ["1516081860000","13025.5588","13025.5589","13025.5588","13025.5588","14.78475912"], \
           ["1516081920000","13025.5588","13025.5589","13025.5588","13025.5588","2.9114972"], \
           ["1516081980000","13025.5589","13025.5589","13025.5588","13025.5589","3.6523503"], \
           ["1516082040000","13025.5589","13025.5589","13025.5588","13025.5589","1.65434074"], \
           ["1516082100000","13025.5589","13037.5917","13025.5588","13037.5916","2.85013936"], \
           ["1516082160000","13037.5916","13037.5917","13037.5916","13037.5916","3.99276476"], \
           ["1516082220000","13037.5917","13040.1305","13037.5916","13040.1304","9.69847152"], \
           ["1516082280000","13040.1305","13040.1305","13040.1303","13040.1303","9.18640722"], \
           ["1516082340000","13040.1304","13040.1304","13025.57","13037.2001","51.43755246"], \
           ["1516082400000","13038.8334","13050.7144","13038.8334","13050.7144","33.07667104"], \
           ["1516082460000","13050.7144","13086.005","13050.7144","13072.1283","10.71310916"], \
           ["1516082520000","13057.1718","13069.493","13057.1718","13069.493","8.24413636"]]'''


data = '''[["1516085400000","0.01379","0.01379","0.01371614","0.0137899","58.72669144"],["1516085460000","0.01367977","0.01367977","0.01352799","0.01352799","300.06164706"],["1516085520000","0.01352799","0.01366108","0.01352799","0.01366107","25.27772642"],["1516085580000","0.01366102","0.01366111","0.01366098","0.01366111","65.45389138"],["1516085640000","0.01366","0.01366111","0.01365999","0.01366111","142.35465322"],["1516085700000","0.01366111","0.01378999","0.0136002","0.01378999","115.51216144"],["1516085760000","0.01360057","0.01360057","0.01360056","0.01360056","9.8"],["1516085820000","0.01378941","0.01378941","0.01362775","0.01378909","36.7343832"],["1516085880000","0.01378901","0.01378901","0.01378901","0.01378901","0.12604112"],["1516085940000","0.01378838","0.0137884","0.01378822","0.01378822","35.72186312"],["1516086000000","0.01361447","0.01377805","0.01361447","0.01377759","12.12532466"],["1516086060000","0.01377751","0.01377751","0.01377741","0.01377741","2.90324216"],["1516086120000","0.01377686","0.01377686","0.01377686","0.01377686","3.4461989"],["1516086180000","0.01360209","0.0137765","0.01360209","0.01361005","72.8601515"],["1516086240000","0.01361009","0.01377589","0.013555","0.01361014","466.05894804"],["1516086300000","0.01377582","0.01377588","0.0136102","0.01377565","438.38483164"],["1516086360000","0.01361046","0.0137756","0.01361046","0.01377534","17.30278526"],["1516086420000","0.01377491","0.01377491","0.01377491","0.01377491","0.33416752"],["1516086480000","0.01375052","0.01375052","0.01375051","0.01375051","0.46619984"],["1516086540000","0.01375051","0.01375051","0.01375051","0.01375051","0"]]'''

if isinstance("sdfa", str):
    print "str"
else:
    print "not str"

import json
from pandas import Series, DataFrame
k_data = json.loads(data)
print type(k_data), k_data
close = list()
# s_data = Series(index=["time", "open", "high", "low", "close", "scale"])
# series_d = dict()
d_time = list()
high = list()
open = list()
low = list()
close_s = list()
scale = list()
for item in k_data:
    # print type(item)
    if isinstance(item, list):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(item[0])/1000))
        print item
        close.append(float(item[4]))
        d_time.append(float(item[0]))
        open.append(float(item[1]))
        high.append(float(item[2]))
        low.append(float(item[3]))
        close_s.append(float(item[4]))
        scale.append(float(item[5]))
        # s_data.append(float(item[4]))
    else:
        print "not list"
print "-" * 30
data_1 = ["1516086600000", "0.01375051", "0.01375051", "0.01375051", "0.01375051", "0"]
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
close.append(float(data_1[4]))
# s_data.append(float(data_1[4]))
d_time.append(float(data_1[0]))
open.append(float(data_1[1]))
high.append(float(data_1[2]))
low.append(float(data_1[3]))
close_s.append(float(data_1[4]))
scale.append(float(data_1[5]))

data_2 = ["1516086600000","0.01372999","0.01372999","0.01372999","0.01372999","8.92727964"]
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
close.append(float(data_1[4]))
# s_data.append(float(data_2[4]))
d_time.append(float(data_2[0]))
open.append(float(data_2[1]))
high.append(float(data_2[2]))
low.append(float(data_2[3]))
close_s.append(float(data_2[4]))
scale.append(float(data_2[5]))

data_3 = ["1516086660000","0.01372999","0.01372999","0.01372999","0.01372999","0"]
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
close.append(float(data_3[4]))
# s_data.append(float(data_3[4]))
d_time.append(float(data_3[0]))
open.append(float(data_3[1]))
high.append(float(data_3[2]))
low.append(float(data_3[3]))
close_s.append(float(data_3[4]))
scale.append(float(data_3[5]))

data_dict = dict()
data_dict["time"] = numpy.array(d_time, dtype='float')
data_dict["open"] = numpy.array(open, dtype='float')
data_dict["high"] = numpy.array(high, dtype='float')
data_dict["low"] = numpy.array(low, dtype='float')
data_dict["close"] = numpy.array(close_s, dtype='float')
data_dict["volume"] = numpy.array(scale, dtype='float')
print "data_dict:", data_dict

print type(close), type(close[0]), close[0], close
closed = numpy.array(close, dtype='float')
print "clolsed array:", type(closed), closed
# s_data = Series(close, index=["time", "open", "high", "low", "close", "scale"])
# print "series:", s_data
ds = DataFrame(data_dict, columns=["time", "open", "high", "low", "close", "volume"])
print "date_frmae:", type(ds), ds
print "close:", ds.close
# neo_btc
input_data = numpy.asarray(data_dict["close"], dtype='float')
print type(input_data), type(input_data[0]), input_data[0], input_data

close_m = numpy.random.random(30)
close_b = list(close_m)
close_c = numpy.array(close_b, dtype='float')

upper, middle, lower = talib.BBANDS(closed, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
# upper, middle, lower = talib.BBANDS(closed, matype=talib.MA_Type.T3)
print "1", "-" * 30
print "upper:", upper
print "middle:", middle
print "lower:", lower

close_m = [1, 3, 4, 2, 3, 5, 7, 9, 8, 5, 7, 10, 11, 12, 12, 13, 11, 10, 11, 12.5, 12]
print type(close_m), type(close_m[0]), close_m[0], close_m
close_b = list(close_m)
print type(close_b), close_b
close_c = numpy.array(close_m, dtype='float')
print type(close_c), close_c
# print "sma:", talib.SMA(close_m)
# upper, middle, lower = talib.BBANDS(close_m, matype=talib.MA_Type.T3)
upper, middle, lower = talib.BBANDS(close_c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
print "2", "-" * 30
print "upper:", upper
print "middle:", middle
print "lower:", lower
